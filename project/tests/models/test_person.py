from project.tests.test_base import BaseTestCase
from project.models.person import Person
from project import db


class Tests(BaseTestCase):
    def test_model(self):
        x = Person(name='John Doe', age=25, email='johndoe@gmail.com')
        db.session.add(x)
        db.session.commit()
        person = Person.query.filter_by(name='John Doe').first()

        self.assertTrue(person.name == "John Doe")
