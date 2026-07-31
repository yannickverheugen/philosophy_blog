"""Application factory and extension registration for the Flask app."""

from flask import Flask
from app.articles.routes import articles_bp
from app.simple_pages.routes import blueprint as simple_pages_bp
from app.users.routes import blueprint as users_bp
from app.extensions.database import db, migrate
from . import articles, users
from app.forms.routes import blueprint as forms_bp

def create_app():
    """Create and configure the Flask application instance."""
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    """Register all blueprints used by the application."""
    app.register_blueprint(articles_bp)
    app.register_blueprint(simple_pages_bp)
    app.register_blueprint(forms_bp)
    app.register_blueprint(users_bp)

def register_extensions(app: Flask):
    """Initialize Flask extensions against the application instance."""
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)