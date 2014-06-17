# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfiguration(object):
    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    # Leave as a slash if served locally
    STATIC_URL = "/"


class TestConfiguration(BaseConfiguration):
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # + os.path.join(BASE_DIR, 'test.db')
