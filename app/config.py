from dotenv import load_dotenv
import os
from os import environ

load_dotenv()

database_url = environ.get('DATABASE_URL', '').strip()

# Render or legacy providers may expose postgres://, but SQLAlchemy expects postgresql://
if database_url.startswith('postgres://'):
	database_url = database_url.replace('postgres://', 'postgresql://', 1)

# Local fallback so app boot does not fail when DATABASE_URL is not set
SQLALCHEMY_DATABASE_URI = database_url or 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
DEBUG = True
ARTICLES_PER_PAGE = 10