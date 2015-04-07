"""
**************************
Basic Pages
**************************

Basic pages with pretty much no dynamic content
"""
from flask import Blueprint, render_template
routes = Blueprint('static_pages', __name__)
route_prefix = ""


# This will house all of the basic pages for the site
@routes.route(route_prefix + '/example-page/')
def example_page():
    return render_template("example_page.html", page='example_page')
