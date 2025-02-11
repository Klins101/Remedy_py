from decouple import config
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = config(
        'SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    DEBUG = True
    TESTING = False


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass
