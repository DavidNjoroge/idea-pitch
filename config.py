import os


class Config:
    '''
    General configurations
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    production configuration child class

    args:
        config: the parent class
    '''
    pass
# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://chutha:chutha@localhost/watchlist_test'
#

class DevConfig(Config):
    '''
    Development configuration child class

    args:
        config: the parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://chutha:chutha@localhost/ideas'

    DEBUG = True

config_options={
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
