from flask import Flask
from flask_migrate import Migrate
from app.blueprints.decks.routes import DecksApiEndpoint
from app.extensions import db
from app.utils.exceptions import BadRequestException, bad_request
from config import app_config
from flask_restful import Api

template_dir = "./templates"
static_dir = "./resources/styles"


def create_app():
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object(app_config)

    from app.models.__mixins__ import TimestampMixin
    from app.models.card import Card
    from app.models.deck import Deck

    db.init_app(app)
    migrate = Migrate(app, db)

    api = Api(app)

    api.add_resource(DecksApiEndpoint, "/api/DecksApiEndpoint")

    from app.blueprints.simple import bp as simple_bp
    from app.blueprints.add import bp as add_bp
    from app.blueprints.decks import bp as decks_bp
    from app.blueprints.cards import bp as cards_bp
    from app.blueprints.study import bp as study_bp

    app.register_blueprint(simple_bp)
    app.register_blueprint(add_bp)
    decks_bp.register_blueprint(cards_bp)
    decks_bp.register_blueprint(study_bp)

    app.register_blueprint(decks_bp)

    @app.errorhandler(BadRequestException)
    def bad_request_exception(e):
        return bad_request(e)

    return app
