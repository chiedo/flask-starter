from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
routes = Blueprint('index', __name__)


@routes.route('/')
def show():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        abort(404)
