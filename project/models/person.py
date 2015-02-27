"""
**************************
Person
**************************

A person.
"""
from project import db
from project.models.base import Base
from project.extras.serializer import Serializer


class Person(Base, Serializer):
    __tablename__ = 'people'
    __public__ = ['name', 'email', 'age']
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    age = db.Column(db.SmallInteger, nullable=True)

    def __init__(self, name, email, age):
        self.name  = name
        self.email = email
        self.age   = age

    def __repr__(self):
        return '<Name - %r>' % (self.name)

    def adult(self):
        if(self.age >= 18):
            return True
        else:
            return False

    def age_str(self):
        return str(self.age)
