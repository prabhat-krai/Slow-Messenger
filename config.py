class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'rememberthis'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

class Dev(BaseConfig):
    DEBUG = True
    
class Prod(BaseConfig):
    DEBUG = False