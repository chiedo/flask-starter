from webapp.tests.test_base import BaseTestCase
from webapp.models.person import Person
from webapp import db


class Tests(BaseTestCase):
    def test_model_create(self):
        x = Person(name='John Doe', age=25, email='johndoe@gmail.com')
        db.session.add(x)
        db.session.commit()
        person = Person.query.filter_by(name='John Doe').first()

        self.assertTrue(person.name == "John Doe")
