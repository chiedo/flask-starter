"""The model for a person"""
from project import db
from project.models.base import Base
import json


class Person(Base):
    __tablename__ = 'people'
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    age = db.Column(db.SmallInteger, nullable=True)

    def __init__(self, name, email, age):
        self.name  = name
        self.email = email
        self.age   = age

    def __repr__(self):
        return '<Name - %r>' % (self.name)

    @staticmethod
    def json(data):
        """Converts a result from sql alchemy into json"""
        output = list()
        if(type(data) is not list):
            data = [data]
        for i in data:
            output.append({
                'name': i.name,
                'email': i.email,
                'age': i.age
            })
        return json.dumps(output)
