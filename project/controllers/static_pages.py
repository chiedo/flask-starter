from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
routes = Blueprint('static_pages', __name__)


# This will house all of the static pages for the site
@routes.route('/example-page/')
def example_page():
    try:
        return render_template("example_page.html", page='example_page')
    except TemplateNotFound:
        abort(404)
