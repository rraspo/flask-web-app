# config.py

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configuration
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configuration
    """

    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}