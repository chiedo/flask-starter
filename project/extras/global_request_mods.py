"""
**************************
Request Mods
**************************

Used for modifying requests before and after the requests are processed
"""
from project import app
from flask import request, render_template


@app.before_request
def before_request():
    """Happens before the requests is processed"""
    # You can do anything you want with the request here such as restricting access,
    # etc.
    print request


@app.after_request
def after_request(response):
    """Happens after the requests is processed but before it is returned"""
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
