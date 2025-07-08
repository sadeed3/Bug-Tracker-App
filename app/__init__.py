from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Config settings
    app.config['SECRET_KEY'] = 'dev-key'  # Replace with a secure key later
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app
