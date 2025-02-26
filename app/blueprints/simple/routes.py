from app.blueprints.simple import bp
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.extensions.seed import seed_database


@bp.route("/")
def index():
    return render_template("login.html")


@bp.route("/seed", methods=["POST"])
@login_required
def seed():
    if request.method == "GET":
        user_id = current_user.id
        seed_database(user_id)
        return redirect(url_for("decks_blueprint.decks"))
