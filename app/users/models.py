"""Database model for application users."""

from app.extensions.database import db

class User(db.Model):
    """Store user credentials and the articles they authored."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    articles = db.relationship('Article', backref='author')