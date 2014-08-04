from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import webapp.controllers.page_utils as page_utils
routes = Blueprint('index', __name__)


@routes.route('/')
def index():
    try:
        page_utils.global_tasks(request)
        global_page_args = page_utils.global_args(request)
        return render_template("index.html", page='index', **global_page_args)
    except TemplateNotFound:
        abort(404)
