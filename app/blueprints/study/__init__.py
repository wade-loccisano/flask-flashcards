from flask import Blueprint

bp = Blueprint("study_blueprint", __name__)

from app.blueprints.study import routes
