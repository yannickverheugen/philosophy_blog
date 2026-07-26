"""Routes for listing, viewing, and creating articles."""

from slugify import slugify
from flask import Blueprint, redirect, render_template, request, current_app, url_for
from .models import Article

articles_bp = Blueprint('articles', __name__)

def make_unique_slug(base_slug):
    """Generate a unique article slug by appending a counter when needed."""
    slug = base_slug
    counter = 1

    while Article.query.filter_by(slug=slug).first() is not None:
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug

@articles_bp.route('/articles/<slug>')
def article(slug):
    """Render a single article page or redirect back to the list."""
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        return redirect('/articles')
    return render_template('article.html', article=article)

@articles_bp.route('/articles')
def list_articles():
    """Render the paginated article list."""
    page_number = request.args.get('page', 1, type=int)
    print('=> Page number:', page_number)
    article_pagination = Article.query.paginate(page=page_number, per_page=current_app.config['ARTICLES_PER_PAGE'])
    return render_template('articles/articles.html', articles=article_pagination)

@articles_bp.route('/articles/create', methods=['GET'])
def create_article():
    """Render the article creation form."""
    return render_template('articles/create.html')

@articles_bp.route('/articles/create', methods=['POST'])
def article_post():
    """Validate article input, save it, and redirect to the list view."""
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    author_id = request.form.get('author_id', '').strip()

    if not title or not content or not author_id:
        return "Missing required fields", 400

    base_slug = slugify(title)
    slug = make_unique_slug(base_slug)

    article = Article(
        title=title,
        content=content,
        author_id=int(author_id),
        slug=slug
    )
    article.save()

    return redirect(url_for('articles.list_articles'))