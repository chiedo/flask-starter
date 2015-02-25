import project.models as models
from random import randint
from faker import Faker
from factory.alchemy import SQLAlchemyModelFactory
fake = Faker()
from app import db


class PersonFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.person.Person
        sqlalchemy_session = db.session

    name  = fake.name()
    email = fake.email()
    age   = randint(10, 99)
