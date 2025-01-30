from app.blueprints.decks import bp
from app.models.deck import Deck
from flask import request, jsonify, Response, render_template, redirect, url_for
from app.extensions import db


@bp.route("/decks", methods=["GET", "POST"])
# @marshal_with(Deck.get_fields())
# @login_required
def decks():
    # get user id
    if request.method == "GET":
        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        decks = db.session.query(Deck).order_by(order_by).limit(limit).all()
        json = jsonify([deck.serialize() for deck in decks])

        return render_template("decks.html", decks=decks)

    if request.method == "POST":
        name = request.form.get("name")

        deck = Deck.from_string(name)

        db.session.add(deck)
        db.session.commit()

        # 201
        return redirect(url_for("decks_blueprint.decks"))


@bp.route("/decks/<id>/", methods=["GET", "POST", "PUT"])
def deck(id):
    deck = db.session.query(Deck).get(id)
    if deck is None:
        response = f"Deck:{id} not found."
        return Response(response=response, status=404)

    # consider just using decks/id/cards
    if request.method == "GET":
        return jsonify(deck.serialize())

    if request.method == "POST":
        if request.form.get("_method") == "DELETE":
            db.session.delete(deck)
            db.session.commit()

            return redirect(url_for("decks_blueprint.decks"))
            # no content
            # return Response(status=204)

    if request.method == "PUT":
        body = request.get_json()

        deck.name = body.get("name", deck.name)

        db.session.commit()

        # no content
        return Response(status=204)

    # if request.method == "DELETE":
    #     db.session.delete(deck)
    #     db.session.commit()

    #     # no content
    #     return Response(status=204)


# copy deck
