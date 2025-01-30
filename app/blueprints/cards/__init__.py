from flask import Blueprint

bp = Blueprint("cards_blueprint", __name__)

from app.blueprints.cards import routes
