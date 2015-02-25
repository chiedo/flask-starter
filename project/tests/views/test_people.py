from project.tests.test_base import BaseTestCase
from project.tests.factories import PersonFactory
from project.models.person import Person
from project import db
import json


class Tests(BaseTestCase):
    def test_get(self):
        PersonFactory.create(name="John Doe")
        db.session.commit()
        response = self.client.get("/people/")
        assert "John Doe" in response.data

    def test_post(self):
        person_attributes = PersonFactory.attributes()
        person_attributes["name"] = "Bob Nolan"

        # Set up the data for posting the person
        person_data = {"person": person_attributes}

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self.client.post("/people/", data=json.dumps(person_data), headers=headers)

        # Check for the person in the database
        person = Person.query.filter_by(name='Bob Nolan').first()
        assert(person is not None)
