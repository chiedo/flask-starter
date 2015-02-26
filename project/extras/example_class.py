"""
**************************
Example Class
**************************

A class with pretty much useless functions solely for the purpose of testing.
"""


class ExampleClass:
    def __init__(self, name, description):
        """ Initializes the example class
        Parameters
        ----------
        name : string
            The name of this example.
        description : string
            The description of this example.
        """
        self.name = name
        self.description = description

    def name_and_description(self):
        """Returns the name and the description
        """
        return self.name + " - " + self.description

    def person_details(self, person):
        """Returns the details for a person
        Parameters
        ----------
        person : object
            The person who's details to return
        """
        return person.name + " - " + person.email + " - " + person.age_str()

    def adult_details(self, person):
        """Returns the details for a person if the individual is an adult
        Parameters
        ----------
        person : object
            The person who's details to return
        """
        if(person.adult()):
            return self.person_details(person)
        else:
            return "child"
