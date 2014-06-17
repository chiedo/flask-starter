from webapp.tests import BaseTestCase
from person.models import Person
from app import db


class PersonTests(BaseTestCase):
    def test_create_person(self):
        x = Person(name='John Doe', age=25, email='johndoe@gmail.com')
        db.session.add(x)
        db.session.commit()
        person = Person.query.filter_by(name='John Doe').first()

        self.assertTrue(person.name == "John Doe")
