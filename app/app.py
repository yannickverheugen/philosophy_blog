from flask import Flask
from app.articles.routes import articles_bp
from app.simple_pages.routes import blueprint as simple_pages_bp
from app.extensions.database import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    app.register_blueprint(articles_bp)
    app.register_blueprint(simple_pages_bp)

def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)