import factory
import project.models as models
from random import randint
from faker import Faker
fake = Faker()


class PersonFactory(factory.Factory):

    class Meta:
        model = models.person.Person

    name  = fake.name()
    email = fake.email()
    age   = randint(10, 99)
