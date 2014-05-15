from flask import Blueprint, request
from app.models.person import Person
import json
routes = Blueprint('person', __name__)
# note-to-self: names of the definitions matter. Make sure
# they make sense


@routes.route('/person', methods=['GET', 'POST'])
def people():
    if request.method == 'GET':
        # outputs json needs to be in try catch eventually
        data = Person.query.all()
        return person_json(data)
    elif request.method == 'POST':
        return 'post'


@routes.route('/person/<id>', methods=['GET', 'DELETE', 'PUT'])
def person(id):
    if request.method == 'GET':
        data = Person.query.filter(Person.id == id).first()
        return person_json(data)
    elif request.method == 'PUT':
        return "put"
    elif request.method == 'DELETE':
        return "delete"


# Definitions
def person_json(data):
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
