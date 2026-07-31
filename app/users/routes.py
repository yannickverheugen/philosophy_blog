from flask import Blueprint, redirect, render_template, request, url_for
from app.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, redirect, render_template, request, session, url_for

blueprint = Blueprint('users', __name__)

@blueprint.get('/register')
def get_register():
  return render_template('users/register.html')

@blueprint.post('/register')
def post_register():
  try:
    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    password_confirmation = request.form.get('password_confirmation', '')

    if not username:
      raise Exception('Please enter a username.')
    if password != password_confirmation:
      raise Exception('The password confirmation must match the password.')
    elif User.query.filter_by(email=email).first():
      raise Exception('The email address is already registered.')

    user = User(
      username=username,
      email=email,
      password=generate_password_hash(password)
    )
    user.save()

    session['user_id'] = user.id

    return redirect(url_for('articles.list_articles'))
  except Exception as error_message:
    error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
    return render_template('users/register.html', error=error)

@blueprint.get('/login')
def get_login():
  return render_template('users/login.html')

@blueprint.post('/login')
def post_login():
  try:
    user = User.query.filter_by(email=request.form.get('email')).first()

    if not user:
      raise Exception('No user with the given email address was found.')
    elif not check_password_hash(user.password, request.form.get('password')):
      raise Exception('The password does not appear to be correct.')
    
    session['user_id'] = user.id
    return redirect(url_for('articles.list_articles'))
    
  except Exception as error_message:
    error = error_message or 'An error occurred while logging in. Please verify your email and password.'
    return render_template('users/login.html', error=error)

@blueprint.get('/logout')
def logout():
  return 'User logged out'