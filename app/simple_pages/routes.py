"""Routes for the static informational pages."""

from flask import Blueprint, render_template, request

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@blueprint.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@blueprint.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

@blueprint.route('/topics')
def topics():
    """Render the topics page."""
    return render_template('topics.html')
