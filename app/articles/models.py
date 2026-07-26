"""Database model for published articles."""

from app.extensions.database import db, CRUDMixin

class Article(db.Model, CRUDMixin):
    """Store the article content, metadata, and author relationship."""
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)