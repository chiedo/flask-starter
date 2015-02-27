"""
**************************
Person Controller
**************************

The controller for the person related urls
"""
from flask import request, redirect
from flask.ext.restful import Resource, Api
from project.models.person import Person
from project.extras.serializer import make_json
from project import db, app
# note-to-self: names of the definitions matter. Make sure
# they make sense
api = Api(app)


class PeopleList(Resource):
    def get(self):
        return make_json(Person.query.all())

    def post(self):
        data = request.get_json()
        name = data["name"]
        email = data["email"]
        age = data["age"]

        person = Person(name, email, age)
        db.session.add(person)
        db.session.commit()
        return make_json(person)


class OnePerson(Resource):
    def get(self, person_id):
        person = Person.query.filter_by(id=person_id).first()
        return make_json(person)

    def put(self, person_id):
        person = Person.query.filter_by(id=person_id).first()
        data = request.get_json()
        person.name = data['name']
        person.email = data['email']
        person.age = data['age']
        db.session.commit()
        return make_json(person), 201

    def delete(self, person_id):
        person = Person.query.filter_by(id=person_id).first()
        db.session.delete(person)
        db.session.commit()
        return '', 204

api.add_resource(PeopleList, '/people/')
api.add_resource(OnePerson, '/people/<int:person_id>/')
