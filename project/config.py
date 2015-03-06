# Define the application directory
import os
from datetime import datetime
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

try:
    environment = os.environ['FLASK_ENV']
except KeyError:
    environment = "development"


class BaseConfiguration(object):
    """This is the base configuration for the app. Any of these configurations may be
    overridden by configurations that extend it"""

    try:
        SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % (
            os.environ["MYSQL_USER"],
            os.environ["MYSQL_PASS"],
            os.environ["MYSQL_HOSTNAME"],
            os.environ["MYSQL_DATABASE"]
        )
    except KeyError:
        pass

    SQLALCHEMY_ECHO = False
    DATABASE_CONNECT_OPTIONS = {}
    THREADS_PER_PAGE = 4  # Application threads. 2 Per core
    CSRF_ENABLED = True  # Enable protection agains *Cross-site Request Forgery (CSRF)
    try:
        CSRF_SESSION_KEY = os.environ['FLASK_CSRF_SESSION_KEY']  # Use a secure, unique and absolutely secret key
        SECRET_KEY = os.environ['FLASK_SECRET_KEY']  # Secret key for signing cookies
    except KeyError:
        CSRF_SESSION_KEY = ""
        SECRET_KEY = ""
    STATIC_URL = '/static/'  # Could be S3 Bucket or something else
    YEAR = datetime.now().year

    # Environment specific configs
    if(environment != 'production'):
        # Enable debugging
        DEBUG = True


class TestConfiguration(BaseConfiguration):
    """Will be used for running the tests. Sqlite in memory will make the tests execute much faster"""
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
