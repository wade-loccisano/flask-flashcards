from flask import Blueprint

bp = Blueprint("decks_blueprint", __name__)

from app.blueprints.decks import routes
