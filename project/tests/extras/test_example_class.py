from project.tests.test_base import BaseTestCase
from project.extras.example_class import ExampleClass
from mock import Mock
from pretend import stub


class TestExampleClass(BaseTestCase):
    def test_name_and_description(self):
        x = ExampleClass("Name", "Description")
        assert(x.name_and_description() == "Name - Description")

    def test_person_details(self):
        x = ExampleClass("Name", "Description")
        # An example using a stub instead of an actual person to prevent the need for hitting the database
        # for no reason
        person = stub(name="Jack Bauer", email="mike@ctu.gov", age_str=lambda: "21")
        assert(x.person_details(person) == "Jack Bauer - mike@ctu.gov - 21")

    def test_adult_details_with_adult(self):
        x = ExampleClass("Name", "Description")
        person = Mock()
        person.name = "Bob"
        person.email = "bob@bob.com"
        person.age_str = Mock(return_value="22")
        person.adult = Mock(return_value=True)

        # An example using a mock instead of an actual person to prevent the need for hitting the database
        # for no reason. And also to validate that the check for the user being an adult was first checked
        assert(x.adult_details(person) == "Bob - bob@bob.com - 22")
        assert(person.adult.call_count == 1)

        # Make sure that the adult function was called
        person.adult.assert_called()

    def test_adult_details_with_child(self):
        x = ExampleClass("Name", "Description")
        person = Mock()
        person.adult = Mock(return_value=False)

        # An example using a mock instead of an actual person to prevent the need for hitting the database
        # for no reason. And also to validate that the check for the user being an adult was first checked
        assert(x.adult_details(person) == "child")

        # Make sure that the adult function was called
        person.adult.assert_called()
        assert(person.adult.call_count == 1)
