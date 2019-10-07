import os

key = os.urandom(33)

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

class Dev(BaseConfig):
    DEBUG = True

class Prod(BaseConfig):
    DEBUG = False