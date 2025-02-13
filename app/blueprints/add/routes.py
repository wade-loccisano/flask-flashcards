from app.blueprints.add import bp
from app.models.card import Card
from app.models.deck import Deck
from flask import request, jsonify, Response, render_template, redirect, url_for
from app.extensions import db
from app.utils.decorators import validate_json
from flask_restful import Resource, reqparse


@bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        decks = db.session.query(Deck).order_by(order_by).limit(limit).all()

        return render_template("add.html", decks=decks, deckId=decks[0].id)

    if request.method == "POST":
        id = request.form.get("deck")
        front = request.form.get("front")
        back = request.form.get("back")

        card = Card.from_string(front, back, id)

        db.session.add(card)
        db.session.commit()

        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        decks = db.session.query(Deck).order_by(order_by).limit(limit).all()

        return render_template("add.html", decks=decks, deckId=id)


# @bp.route("/add", methods=["POST"])
# @validate_json()
# def add_card(id):
#     print("hi lol")
#     deck = db.session.query(Deck).get(id)
#     if deck is None:
#         response = f"Deck:{id} not found."
#         return Response(response=response, status=404)

#     if request.method == "POST":
#         front = request.form.get("front")
#         back = request.form.get("back")

#         card = Card.from_string(front, back, id)

#         db.session.add(card)
#         db.session.commit()

#         return 200
