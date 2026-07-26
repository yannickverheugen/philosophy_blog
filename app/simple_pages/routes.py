from flask import Blueprint, render_template, request

blueprint = Blueprint('simple_pages', __name__)

# Home page route
@blueprint.route('/')
def index():
    return render_template('index.html')

# About page route
@blueprint.route('/about')
def about():
    return render_template('about.html')

# Contact page route
@blueprint.route('/contact')
def contact():
    return render_template('contact.html')

# Topics page route
@blueprint.route('/topics')
def topics():
    return render_template('topics.html')
