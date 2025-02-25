from flask import Blueprint

bp = Blueprint("auth_blueprint", __name__)

from app.blueprints.auth import routes
