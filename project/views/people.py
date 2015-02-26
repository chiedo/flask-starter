"""
**************************
Person Controller
**************************

The controller for the person related urls
"""
from flask import Blueprint, request, redirect
from project.models.person import Person
from project import db
routes = Blueprint('person', __name__)
route_prefix = "/people"
# note-to-self: names of the definitions matter. Make sure
# they make sense


@routes.route(route_prefix + '/', methods=['GET', 'POST'])
def people():
    if request.method == 'GET':
        # outputs json needs to be in try catch eventually
        data = Person.query.all()
        return Person.json(data)
    elif request.method == 'POST':
        data = request.get_json()
        name = data["person"]["name"]
        email = data["person"]["email"]
        age = data["person"]["age"]

        person = Person(name, email, age)
        db.session.add(person)
        db.session.commit()
        return redirect("/people/")


@routes.route(route_prefix + '/<id>/', methods=['GET', 'DELETE', 'PUT'])
def person(id):
    if request.method == 'GET':
        # or could use .all()
        data = Person.query.filter(Person.id == id).first()
        return Person.json(data)
    elif request.method == 'PUT':
        return "put"
    elif request.method == 'DELETE':
        return "delete"
