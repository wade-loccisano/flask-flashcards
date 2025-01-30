from flask import Blueprint

bp = Blueprint("simple_blueprint", __name__)

from app.blueprints.simple import routes
