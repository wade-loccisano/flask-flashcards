from app.blueprints.study import bp
from app.models.deck import Deck
from flask import request, jsonify, Response, render_template, redirect, url_for
from app.extensions import db


@bp.route("/decks/<int:deck_id>/study", methods=["GET"])
def study(deck_id):
    if request.method == "GET":
        deck = db.session.query(Deck).get(deck_id)
        return render_template("study.html", deck=deck.serialize())
