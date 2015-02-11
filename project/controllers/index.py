from flask import Blueprint, render_template, abort, request, make_response
from jinja2 import TemplateNotFound
import project.controllers.page_utils as page_utils
routes = Blueprint('index', __name__)


@routes.route('/')
def index():
    try:
        global_page_args = page_utils.global_args(request)
        response = make_response(render_template("index.html", page='index', **global_page_args))
        return page_utils.global_response_handler(request, response)
    except TemplateNotFound:
        abort(404)
