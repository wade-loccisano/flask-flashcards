from flask import Blueprint

bp = Blueprint("browse_blueprint", __name__)

from app.blueprints.browse import routes
