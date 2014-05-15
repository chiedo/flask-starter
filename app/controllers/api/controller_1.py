from flask import Blueprint
from app.models.controller_1 import Controller1
import json
routes = Blueprint('controller_1', __name__)


@routes.route('/')
def all():
    """return all data as a json"""
    # needs to be in try catch eventually
    output = list()
    data = Controller1.query.all()
    for i in data:
        output.append({
            'name': i.name,
            'email': i.email,
            'age': i.age
        })
    return json.dumps(output)
