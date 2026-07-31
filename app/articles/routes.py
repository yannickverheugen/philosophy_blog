"""Routes for listing, viewing, creating, editing, and deleting articles."""

from slugify import slugify
from flask import Blueprint, abort, current_app, redirect, render_template, request, session, url_for
from .models import Article
from app.users.models import User

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


def _get_article_for_current_user(slug):
    """Return the article if the current user owns it, otherwise stop the request."""
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('users.get_login'))

    article = Article.query.filter_by(slug=slug).first()
    if not article:
        return redirect(url_for('articles.list_articles'))

    if article.author_id != user_id:
        abort(403)

    return article

@articles_bp.route('/articles')
def list_articles():
    """Render the paginated article list."""
    page_number = request.args.get('page', 1, type=int)
    print('=> Page number:', page_number)
    article_pagination = Article.query.paginate(page=page_number, per_page=current_app.config['ARTICLES_PER_PAGE'])
    return render_template('articles/articles.html', articles=article_pagination)

@articles_bp.route('/articles/create', methods=['GET'])
def create_article():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('users.get_login'))
    return render_template('articles/create.html')

@articles_bp.route('/articles/create', methods=['POST'])
def article_post():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('users.get_login'))

    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()

    if not title or not content:
        return "Missing required fields", 400

    base_slug = slugify(title)
    slug = make_unique_slug(base_slug)

    article = Article(
        title=title,
        content=content,
        author_id=int(user_id),
        slug=slug
    )
    article.save()

    return redirect(url_for('articles.list_articles'))


@articles_bp.route('/articles/<slug>/edit', methods=['GET'])
def edit_article(slug):
    article = _get_article_for_current_user(slug)
    if hasattr(article, 'status_code'):
        return article

    return render_template('articles/edit.html', article=article)


@articles_bp.route('/articles/<slug>/edit', methods=['POST'])
def update_article(slug):
    article = _get_article_for_current_user(slug)
    if hasattr(article, 'status_code'):
        return article

    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()

    if not title or not content:
        return "Missing required fields", 400

    article.title = title
    article.content = content
    article.save()

    return redirect(url_for('articles.article', slug=article.slug))


@articles_bp.route('/articles/<slug>/delete', methods=['POST'])
def delete_article(slug):
    article = _get_article_for_current_user(slug)
    if hasattr(article, 'status_code'):
        return article

    article.delete()
    return redirect(url_for('articles.list_articles'))