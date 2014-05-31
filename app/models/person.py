"""The model for a person"""
from app import db
from app.models.base import Base


class Person(Base):
    __tablename__ = 'people'
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.SmallInteger, nullable=True)
    age = db.Column(db.String(128), nullable=False)

    def __init__(self, name, email, age):
        self.name  = name
        self.email = email
        self.age   = age

    def __repr__(self):
        return '<Name - %r>' % (self.name)
