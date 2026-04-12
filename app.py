from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config.from_object('config')

# Define routes for the application

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Articles page route
@app.route('/articles')
def articles():
    return render_template('articles.html')

# Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Topics page route
@app.route('/topics')
def topics():
    return render_template('topics.html')

@app.route('/contact', methods=['POST'])
def contact_post():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    message = request.form.get('user_message')
    return f'Thank you {name} for your message: "{message}". We will contact you at {email}.'

if __name__ == '__main__':
    app.run()