from flask import Blueprint, request
from .models import Contact

blueprint = Blueprint('forms', __name__)

# Contact form submission route
@blueprint.route('/contact', methods=['POST'])
def contact_post():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    message = request.form.get('user_message')

    if not name or not email or not message:
        return "Missing required fields", 400

    # Save the contact message to the database
    contact = Contact(
        name=name,
        email=email,
        message=message
        )
    contact.save()
    
    return f'Thank you {name} for your message: "{message}". We will contact you at {email}.'