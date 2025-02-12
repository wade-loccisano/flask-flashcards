from app.blueprints.add import bp
from app.models.card import Card
from app.models.deck import Deck
from flask import request, jsonify, Response, render_template, redirect, url_for
from app.extensions import db
from app.utils.decorators import validate_json
from flask_restful import Resource, reqparse


@bp.route("/add", methods=["GET"])
def add():
    if request.method == "GET":
        return render_template("add.html")


@bp.route("/add/<int:id>/", methods=["GET", "POST"])
@validate_json()
def add_card(id):
    deck = db.session.query(Deck).get(id)
    if deck is None:
        response = f"Deck:{id} not found."
        return Response(response=response, status=404)

    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":
        front = request.form.get("front")
        back = request.form.get("back")

        card = Card.from_string(front, back, id)

        db.session.add(card)
        db.session.commit()

        return 200
        # return redirect(
        #     url_for("decks_blueprint.cards_blueprint.cards", deck_id=deck_id)
        # )
