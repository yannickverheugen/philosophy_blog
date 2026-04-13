from flask import Blueprint, redirect, render_template, url_for, request

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
    return render_template('simple_pages/index.html')

# About page route
@blueprint.route('/about')
def about():
    return render_template('simple_pages/about.html')

# Articles page route
@blueprint.route('/articles')
def articles():
    return render_template('simple_pages/articles.html')

# Contact page route
@blueprint.route('/contact')
def contact():
    return render_template('simple_pages/contact.html')

# Topics page route
@blueprint.route('/topics')
def topics():
    return render_template('simple_pages/topics.html')

# Contact form submission route
@blueprint.route('/contact', methods=['POST'])
def contact_post():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    message = request.form.get('user_message')
    return f'Thank you {name} for your message: "{message}". We will contact you at {email}.'