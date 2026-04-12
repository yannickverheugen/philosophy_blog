from flask import Flask, redirect, url_for
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return '"<a href="/about">About Page</a>"'

@app.route('/about')
def about():
    return redirect(url_for('about_page'))

@app.route('/about-me')
def about_me():
    return redirect(url_for('https://codecookies.xyz'))

if __name__ == '__main__':
    app.run()