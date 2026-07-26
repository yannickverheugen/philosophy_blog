from slugify import slugify
from flask import Blueprint, redirect, render_template, request, current_app, url_for
from .models import Article

articles_bp = Blueprint('articles', __name__)

def make_unique_slug(base_slug):
    slug = base_slug
    counter = 1

    while Article.query.filter_by(slug=slug).first() is not None:
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug

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

# Create article page route
@articles_bp.route('/articles/create', methods=['GET'])
def create_article():
    return render_template('articles/create.html')

# Create article form submission route
@articles_bp.route('/articles/create', methods=['POST'])
def article_post():
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