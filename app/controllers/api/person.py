from flask import Blueprint, request
from app.models.person import Person
routes = Blueprint('person', __name__)
# note-to-self: names of the definitions matter. Make sure
# they make sense


@routes.route('/person/', methods=['GET', 'POST'])
def people():
    if request.method == 'GET':
        # outputs json needs to be in try catch eventually
        data = Person.query.all()
        return Person.json(data)
    elif request.method == 'POST':
        return 'post'


@routes.route('/person/<id>/', methods=['GET', 'DELETE', 'PUT'])
def person(id):
    if request.method == 'GET':
        # or could use .all()
        data = Person.query.filter(Person.id == id).first()
        return Person.json(data)
    elif request.method == 'PUT':
        return "put"
    elif request.method == 'DELETE':
        return "delete"
