from app.blueprints.decks import bp
from app.models.deck import Deck
from flask import request, jsonify, Response, render_template, redirect, url_for
from app.extensions import db
from app.utils.decorators import validate_json
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user


@bp.route("/decks", methods=["GET", "POST"])
@validate_json(ignore_methods=["GET"])
@login_required
def decks():
    if request.method == "GET":
        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        decks = (
            db.session.query(Deck)
            .filter_by(user_id=current_user.id)
            .order_by(order_by)
            .limit(limit)
            .all()
        )

        serialized_decks = {}
        for deck in decks:
            serialized_decks[deck.name] = deck.serialize()

        return render_template(
            "decks.html", decks=decks, serialized_decks=serialized_decks
        )

    if request.method == "POST":
        name = request.form.get("name").strip()

        deck = Deck.from_string(name, current_user.id)

        db.session.add(deck)
        db.session.commit()

        return redirect(url_for("decks_blueprint.decks"))


class DecksApiEndpoint(Resource):
    def __init__(self):
        self.post_args = reqparse.RequestParser()
        self.post_args.add_argument(
            "name",
            type=str,
            help="You must include a name string with this post request.",
            required=True,
        )

    def get(self):
        return {
            "message": "this is a respons from the get request",
        }


@bp.route("/decks/<id>/", methods=["GET", "POST", "PUT"])
@validate_json(ignore_methods=["GET"])
@login_required
def deck(id):
    deck = db.session.query(Deck).get(id)
    if deck is None:
        response = f"Deck:{id} not found."
        return Response(response=response, status=404)

    if request.method == "GET":
        return jsonify(deck.serialize())

    if request.method == "POST":
        if request.form.get("_method") == "DELETE":
            db.session.delete(deck)
            db.session.commit()

            return redirect(url_for("decks_blueprint.decks"))

    if request.method == "PUT":
        name = request.form.get("name").strip()

        deck.name = name

        db.session.commit()

        # no content
        return Response(status=204)

    # if request.method == "DELETE":
    #     db.session.delete(deck)
    #     db.session.commit()

    #     # no content
    #     return Response(status=204)


# copy deck
