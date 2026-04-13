from flask import Flask
from app.articles.routes import articles_bp
from app.simple_pages.routes import blueprint as simple_pages_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    app.register_blueprint(articles_bp)
    app.register_blueprint(simple_pages_bp)