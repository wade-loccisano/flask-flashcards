from app.blueprints.simple import bp
from flask import render_template
from app.extensions.seed import seed_database


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/seed")
def seed():
    seed_database()
    return "Db Seeded"
