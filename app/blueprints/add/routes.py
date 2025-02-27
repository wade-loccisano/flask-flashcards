from app.blueprints.add import bp
from app.models.card import Card
from app.models.deck import Deck
from flask import request, render_template
from flask_login import login_required, current_user
from app.extensions import db


@bp.route("/add", methods=["GET", "POST"])
@login_required
def add():
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

        if not decks or len(decks) == 0:
            deck = Deck.from_string("Default Deck")
            db.session.add(deck)
            db.session.commit()

        decks = (
            db.session.query(Deck)
            .filter_by(user_id=current_user.id)
            .order_by(order_by)
            .limit(limit)
            .all()
        )

        return render_template("add.html", decks=decks, deckId=decks[0].id)

    if request.method == "POST":
        id = request.form.get("deck")
        front = request.form.get("front").strip()
        back = request.form.get("back").strip()

        card = Card.from_string(front, back, id)

        db.session.add(card)
        db.session.commit()

        limit = request.args.get("limit", None)
        order_by = request.args.get("order_by", None)

        decks = (
            db.session.query(Deck)
            .filter_by(user_id=current_user.id)
            .order_by(order_by)
            .limit(limit)
            .all()
        )

        return render_template("add.html", decks=decks, deckId=id)
