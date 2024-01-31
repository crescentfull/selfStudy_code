from dotenv import load_dotenv, find_dotenv

# load_dotenv()
load_dotenv(find_dotenv())

import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    MOVIE_DB_API_KEY = os.getenv('MOVIE_DB_API_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False