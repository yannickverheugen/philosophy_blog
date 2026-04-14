from dotenv import load_dotenv
import os
from os import environ

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
DEBUG = True
ARTICLES_PER_PAGE = 10