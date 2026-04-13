from flask import Blueprint, redirect, render_template

posts_data = {
    'the-unexamined-life': {'title': 'The Unexamined Life', 'author': 'Socrates', 'content': 'The unexamined life is not worth living. We must question everything we think we know.'},
    'the-allegory-of-the-cave': {'title': 'The Allegory of the Cave', 'author': 'Plato', 'content': 'Imagine prisoners chained in a cave, only seeing shadows on the wall. What if one broke free?'},
    'the-golden-mean': {'title': 'The Golden Mean', 'author': 'Aristotle', 'content': 'Virtue lies in finding the balance between excess and deficiency.'},
    'know-thyself': {'title': 'Know Thyself', 'author': 'Socrates', 'content': 'True wisdom begins with self-knowledge. Only by understanding ourselves can we understand the world.'},
    'theory-of-forms': {'title': 'Theory of Forms', 'author': 'Plato', 'content': 'The physical world is merely a shadow of the true reality of perfect, eternal Forms.'},
}

articles_bp = Blueprint('articles', __name__)

# Route for individual articles
@articles_bp.route('/articles/<slug>')
def article(slug):
    post = posts_data.get(slug)
    if not post:
        return redirect('/articles')
    return render_template('article.html', post=post)

# List all articles route
@articles_bp.route('/articles')
def list_articles():
    return render_template('articles/articles.html', posts_data=posts_data)
