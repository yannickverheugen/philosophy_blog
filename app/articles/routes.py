from flask import Blueprint, redirect, render_template, request, current_app
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
    page_number = request.args.get('page', 1, type=int)
    print('=> Page number:', page_number)
    article_pagination = Article.query.paginate(page=page_number, per_page=current_app.config['ARTICLES_PER_PAGE'])
    return render_template('articles/articles.html', articles=article_pagination)
