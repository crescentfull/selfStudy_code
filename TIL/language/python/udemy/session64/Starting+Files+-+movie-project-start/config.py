from dotenv import load_dotenv, find_dotenv

# load_dotenv()
load_dotenv(find_dotenv())

import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MOVIE_DB_API_KEY = os.getenv('MOVIE_DB_API_KEY')

# class MovieKey:
#     MOVIE_DB_API_KEY = os.getenv('MOVIE_DB_API_KEY')