from project.tests.test_base import BaseTestCase
from project.tests.factories import PersonFactory
from project.models.person import Person
from project import db
import json
from expects import *


class TestPeopleApi(BaseTestCase):
    def test_get(self):
        PersonFactory.create(name="John Doe")
        db.session.commit()
        response = self.client.get("/people/")

        expect("John Doe" in response.data).to(be_true)

    def test_post(self):
        person_attributes = PersonFactory.attributes()
        person_attributes["name"] = "Bob Nolan"

        # Set up the data for posting the person

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self.client.post("/people/", data=json.dumps(person_attributes), headers=headers)

        # Check for the person in the database
        person = Person.query.filter_by(name='Bob Nolan').first()
        expect(person).not_to(equal(None))

    def test_put(self):
        person = PersonFactory.create()
        db.session.commit()
        person_attributes = PersonFactory.attributes()
        person_attributes["name"] = "Bob updated"

        response = self.client.put("/people/%s/" % person.id, data=json.dumps(person_attributes),
                        content_type='application/json')
        print response
        # Check for the person in the database
        person = Person.query.first()
        expect(person.name).to(equal("Bob updated"))

    def test_delete(self):
        person = PersonFactory.create()
        db.session.commit()

        self.client.delete("/people/%s/" % person.id)

        # Make sure the person is not in the database
        person_count = Person.query.count()
        expect(person_count).to(equal(0))
