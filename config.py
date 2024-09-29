import os
class Config:
    API_KEY = 'AIzaSyBnjHnK9lBu1LMFZTefvKYPA5gETCXffKU'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False