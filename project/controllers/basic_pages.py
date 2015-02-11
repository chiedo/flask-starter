from flask import Blueprint, render_template, abort, request, make_response
from jinja2 import TemplateNotFound
routes = Blueprint('static_pages', __name__)
import project.controllers.page_utils as page_utils
route_prefix = ""


# This will house all of the basic pages for the site
@routes.route(route_prefix + '/')
def index():
    try:
        global_page_args = page_utils.global_args(request)
        response = make_response(render_template("index.html", page='index', **global_page_args))
        return page_utils.global_response_handler(request, response)
    except TemplateNotFound:
        abort(404)


@routes.route(route_prefix + '/example-page/')
def example_page():
    try:
        return render_template("example_page.html", page='example_page')
    except TemplateNotFound:
        abort(404)
