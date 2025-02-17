from app.blueprints.browse import bp
from app.models.card import Card
from app.models.deck import Deck
from flask import request, jsonify, Response, render_template, redirect, url_for
from app.extensions import db
from app.utils.decorators import validate_json
from flask_restful import Resource, reqparse


@bp.route("/browse", methods=["GET", "POST"])
def browse():
    if request.method == "GET":
        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        cards = db.session.query(Card).order_by(order_by).limit(limit).all()

        return render_template("browse.html", cards=cards)

    if request.method == "POST":
        id = request.form.get("deck")
        cardId = request.form.get("card")
        front = request.form.get("front")
        back = request.form.get("back")

        card = Card.from_string(front, back, id)

        db.session.add(card)
        db.session.commit()

        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        decks = db.session.query(Deck).order_by(order_by).limit(limit).all()

        return render_template("add.html", decks=decks, deckId=id)
