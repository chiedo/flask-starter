# Define the application directory
import os
from datetime import datetime
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
environment = os.environ['FLASK_ENV']


class BaseConfiguration(object):
    """This is the base configuration for the app. Any of these configurations may be
    overridden by configurations that extend it"""

    if(environment == 'development'):
        # Enable debugging
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1/flask_app_default"
        SQLALCHEMY_ECHO = False
        DATABASE_CONNECT_OPTIONS = {}
        THREADS_PER_PAGE = 2  # Application threads. 2 Per core
        CSRF_ENABLED = True  # Enable protection agains *Cross-site Request Forgery (CSRF)*
        CSRF_SESSION_KEY = "ENTER"  # Use a secure, unique and absolutely secret key for signing the data.
        SECRET_KEY = "ENTER"  # Secret key for signing cookies
        STATIC_URL = '/static/'  # Could be S3 Bucket or something else
        YEAR = datetime.now().year
    if(environment == 'staging'):
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = "ENTER"
        DATABASE_CONNECT_OPTIONS = {}
        THREADS_PER_PAGE = 4
        CSRF_ENABLED = True
        CSRF_SESSION_KEY = "ENTER"
        SECRET_KEY = "ENTER"
        STATIC_URL = '/static/'
        YEAR = datetime.now().year
    elif(environment == 'production'):
        DEBUG = False
        SQLALCHEMY_DATABASE_URI = "ENTER"
        DATABASE_CONNECT_OPTIONS = {}
        THREADS_PER_PAGE = 4
        CSRF_ENABLED = True
        CSRF_SESSION_KEY = "ENTER"
        SECRET_KEY = "ENTER"
        STATIC_URL = '/static/'
        YEAR = datetime.now().year


class TestConfiguration(BaseConfiguration):
    """Will be used for running the tests. Sqlite in memory will make the tests execute much faster"""
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
