from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

# Accessing the DB through Flask
# to create a DB for tests -> SQLALCHEMY_TEST_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_test
#Factory function that builds our app
#None -> So we can default to our regular DB
def create_app(test_config = None):
    #_name_ store the name of the module we're in
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    #Configure SQLAlchemy
    if not test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "TEST_SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from app.models.game import Game
    from app.models.player import Player

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    # from .routes import example_bp
    # app.register_blueprint(example_bp)

    from .routes import games_bp
    app.register_blueprint(games_bp)

    from .routes import players_bp
    app.register_blueprint(players_bp)


    CORS(app)
    return app
