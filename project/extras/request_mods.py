"""
**************************
Request Mods
**************************

Used for modifying requests before and after the requests are processed
"""
from project import app
from flask import request


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


def global_args(request):
    """Arguments that can be passed to all pages. Request is passed in the event that
    conditional variables need to be passed to the page"""
    kwargs = {'bar': 'foo', 'foo': 'bar'}
    return kwargs
