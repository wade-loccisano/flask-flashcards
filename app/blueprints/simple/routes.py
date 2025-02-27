from app.blueprints.simple import bp
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.extensions.seed import seed_database
from app.resources.forms.signup import SignUpForm
from app.extensions import db
from app.models.deck import Deck


@bp.route("/")
def index():
    if current_user and current_user.is_authenticated:
        decks = db.session.query(Deck).filter_by(user_id=current_user.id).all()

        serialized_decks = {}
        for deck in decks:
            serialized_decks[deck.name] = deck.serialize()

        return render_template(
            "decks.html", decks=decks, serialized_decks=serialized_decks
        )
    form = SignUpForm()
    return render_template("signup.html", form=form)


@bp.route("/seed", methods=["POST"])
@login_required
def seed():
    if request.method == "GET":
        user_id = current_user.id
        seed_database(user_id)
        return redirect(url_for("decks_blueprint.decks"))
