"""Routes for processing submitted form data."""

from flask import Blueprint, request
from .models import Contact

blueprint = Blueprint('forms', __name__)

@blueprint.route('/contact', methods=['POST'])
def contact_post():
    """Validate the contact form and persist the submitted message."""
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    message = request.form.get('user_message')

    if not name or not email or not message:
        return "Missing required fields", 400

    contact = Contact(
        name=name,
        email=email,
        message=message
        )
    contact.save()
    
    return f'Thank you {name} for your message: "{message}". We will contact you at {email}.'