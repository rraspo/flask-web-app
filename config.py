# config.py

class Config(object):
    """
    Common configurations
    """
    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development configuration
    """
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configuration
    """
    DEBUG = False

class TestingConfig(Config):
    """
    Production configuration
    """
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}