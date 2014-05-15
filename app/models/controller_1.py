"""The model for controller 1"""
from app import db
from app.models.base import Base


class Controller1(Base):
    __tablename__ = 'controller_1'
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.SmallInteger, nullable=True)
    age = db.Column(db.String(128), nullable=False)

    def __init__(self, name, email, age):
        self.name  = name
        self.email = email
        self.age   = age

    def __repr__(self):
        return '<Name - %r>' % (self.name)
