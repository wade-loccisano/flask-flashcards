from flask import Blueprint

bp = Blueprint("add_blueprint", __name__)

from app.blueprints.add import routes
