from flask import Blueprint, redirect, render_template
from .models import Article

articles_bp = Blueprint('articles', __name__)

# Route for individual articles
@articles_bp.route('/articles/<slug>')
def article(slug):
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        return redirect('/articles')
    return render_template('article.html', article=article)

# List all articles route
@articles_bp.route('/articles')
def list_articles():
    all_articles = Article.query.all()
    return render_template('articles/articles.html', articles=all_articles)
