from flask.ext.testing import TestCase

from project import app, db


class BaseTestCase(TestCase):
    """A base test case for flask."""

    def create_app(self):
        app.config.from_object('project.config.TestConfiguration')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
