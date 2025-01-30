from app.blueprints.cards import bp
from app.models.card import Card
from app.models.deck import Deck
from flask import request, jsonify, Response, render_template, redirect, url_for
from app.extensions import db


@bp.route("/decks/<int:deck_id>/cards", methods=["GET", "POST"])
def cards(deck_id):
    if request.method == "GET":
        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        deck = db.session.query(Deck).order_by(order_by).limit(limit).get(deck_id)
        return render_template("cards.html", deck=deck.serialize())

    if request.method == "POST":
        front = request.form.get("front")
        back = request.form.get("back")

        card = Card.from_string(front, back, deck_id)

        db.session.add(card)
        db.session.commit()

        return redirect(
            url_for("decks_blueprint.cards_blueprint.cards", deck_id=deck_id)
        )


@bp.route("/decks/<int:deck_id>/cards/<int:card_id>/", methods=["GET", "POST", "PUT"])
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

    if request.method == "GET":
        return jsonify(card.serialize())

    if request.method == "POST":
        if request.form.get("_method") == "DELETE":
            db.session.delete(card)
            db.session.commit()

            return redirect(
                url_for("decks_blueprint.cards_blueprint.cards", deck_id=deck_id)
            )

    if request.method == "PUT":
        body = request.get_json()

        card.front = body.get("front", card.front)
        card.back = body.get("back", card.back)

        db.session.commit()

        return Response(status=204)
