from app.blueprints.browse import bp
from app.models.card import Card
from app.models.deck import Deck
from flask import request, jsonify, Response, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.extensions import db
from app.utils.decorators import validate_json
from flask_restful import Resource, reqparse


@bp.route("/browse", methods=["GET", "POST"])
@login_required
def browse():
    if request.method == "GET":
        cards = (
            db.session.query(Card)
            .join(Deck)
            .filter(Deck.user_id == current_user.id)
            .add_columns(Deck.name)
            .all()
        )

        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        decks = (
            db.session.query(Deck)
            .filter_by(user_id=current_user.id)
            .order_by(order_by)
            .limit(limit)
            .all()
        )

        return render_template(
            "browse.html", cards=cards, decks=decks, selected_deck_id=None
        )

    if request.method == "POST":
        id = request.form.get("deckId")
        cardId = request.form.get("cardId")
        front = request.form.get("front").strip() if request.form.get("front") else ""
        back = request.form.get("back").strip() if request.form.get("back") else ""
        selected_deck_id = request.form.get("deck-select-input")

        if not selected_deck_id:
            id = None

        if request.form.get("_method") == "DELETE":
            card = db.session.query(Card).filter(Card.id == cardId).first()
            db.session.delete(card)
            db.session.commit()

            cards = (
                db.session.query(Card)
                .join(Deck)
                .filter(Deck.user_id == current_user.id)
                .all()
            )

            limit = request.args.get("limit", None)
            order_by = request.args.get("order_by", None)

            decks = (
                db.session.query(Deck)
                .filter_by(user_id=current_user.id)
                .order_by(order_by)
                .limit(limit)
                .all()
            )

            return render_template(
                "browse.html", cards=cards, decks=decks, selected_deck_id=id
            )

        if not cardId:
            card = Card.from_string(front, back, id)
            db.session.add(card)
            db.session.commit()
        else:
            card = db.session.query(Card).filter(Card.id == cardId).first()
            card.front = front
            card.back = back
            db.session.commit()

        cards = (
            db.session.query(Card)
            .join(Deck)
            .filter(Deck.user_id == current_user.id)
            .all()
        )

        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        decks = (
            db.session.query(Deck)
            .filter_by(user_id=current_user.id)
            .order_by(order_by)
            .limit(limit)
            .all()
        )

        return render_template(
            "browse.html", cards=cards, decks=decks, selected_deck_id=id
        )


@bp.route("/browse/decks/<int:deck_id>/cards/<int:card_id>/", methods=["POST"])
@login_required
def card(deck_id, card_id):
    card = (
        db.session.query(Card)
        .filter(
            Card.id == card_id,
            Card.deck_id == deck_id,
        )
        .first()
    )

    if card is None:
        response = f"Card: {card_id} not found."
        return Response(response=response, status=404)

    if request.method == "POST":
        if request.form.get("_method") == "DELETE":
            db.session.delete(card)
            db.session.commit()

            cards = (
                db.session.query(Card)
                .join(Deck)
                .filter(Deck.user_id == current_user.id)
                .all()
            )

            limit = request.args.get("limit", None)
            order_by = request.args.get("order_by", None)

            decks = (
                db.session.query(Deck)
                .filter_by(user_id=current_user.id)
                .order_by(order_by)
                .limit(limit)
                .all()
            )

            return render_template(
                "browse.html", cards=cards, decks=decks, selected_deck_id=id
            )
