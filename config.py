import os

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_UR") 
class Config:
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATA_BASE_URI")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI_PROD")


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI_TEST")


config_selector = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestConfig,
}