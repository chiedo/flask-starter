"""
**************************
Basic Pages
**************************

Basic pages with pretty much no dynamic content
"""
from flask import Blueprint, render_template, abort, make_response
from jinja2 import TemplateNotFound
routes = Blueprint('static_pages', __name__)
from project.extras.request_mods import *
route_prefix = ""


# This will house all of the basic pages for the site
@routes.route(route_prefix + '/')
def index():
    try:
        response = make_response(render_template("index.html", page='index'))
        return response
    except TemplateNotFound:
        abort(404)


@routes.route(route_prefix + '/example-page/')
def example_page():
    try:
        return render_template("example_page.html", page='example_page')
    except TemplateNotFound:
        abort(404)
