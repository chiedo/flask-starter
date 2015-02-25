import factory
import factory.alchemy
import project.models as models
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from random import randint
from faker import Faker
fake = Faker()
from project.config import BaseConfiguration
engine = create_engine(BaseConfiguration.SQLALCHEMY_DATABASE_URI)

session = scoped_session(sessionmaker(bind=engine))


class PersonFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.person.Person
        sqlalchemy_session = session

    name  = fake.name()
    email = fake.email()
    age   = randint(10, 99)
