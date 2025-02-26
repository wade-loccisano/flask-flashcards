from app.models.user import User
from app.extensions import db
from app.extensions.seed import seed_database
from app.blueprints.auth import bp
from datetime import datetime
from flask import request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required


@bp.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")  # min4
        password = request.form.get("password")  # min8

        user = User.query.filter_by(username=username).first()
        if not user:
            return redirect(url_for("auth_blueprint.signup"))

        if check_password_hash(user.password_hash, password):
            user.last_login = datetime.now()
            db.session.commit()
            login_user(user)
            return redirect(url_for("decks_blueprint.decks"))


@bp.route("/auth/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        username = request.form.get("username")  # min4
        password = request.form.get("password")  # min8

        # ADD CAPTCHA

        user = User.query.filter_by(username=username).first()
        if user:
            return redirect(url_for("auth_blueprint.login"))

        hashed_password = generate_password_hash(password)
        user = User(username=username, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()

        seed_database(user.id)

        if check_password_hash(user.password_hash, password):
            user.last_login = datetime.now()
            db.session.commit()
            login_user(user)
            return redirect(url_for("decks_blueprint.decks"))


@bp.route("/auth/logout", methods=["POST"])
def logout():
    if request.method == "POST":
        logout_user()
        return redirect(url_for("simple_blueprint.index"))
