from flask import Blueprint, redirect, render_template, url_for, request

blueprint = Blueprint('forms', __name__)

# Contact form submission route
@blueprint.route('/contact', methods=['POST'])
def contact_post():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    message = request.form.get('user_message')
    return f'Thank you {name} for your message: "{message}". We will contact you at {email}.'