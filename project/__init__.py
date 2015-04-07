from flask import Flask, make_response
import os
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('project.config.BaseConfiguration')


# Catch all route for Reactjs
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    response = make_response(render_template("index.html", page='index'))
    return response

# Define the database object which is imported
# by modules and views
db = SQLAlchemy(app)

from project.extras.global_request_mods import *

# Connect all the routes from the views
try:
    view_names = []
    for file in [doc for doc in os.listdir("project/views") if doc.endswith(".py") and doc != "__init__.py"]:
        view_names.append("project.views." + file.split(".")[0])  # remove the .py from the file name

    # Loop through all contollers and register their blueprint
    for view_name in view_names:
        # This dynamically imports all modules in the tests_to_run list. This allows me to import a module using
        # a variable. This is fairly advanced and hard to follow for the beginner.
        view = __import__(view_name, fromlist=[view_name])
        if hasattr(view, "routes"):
            app.register_blueprint(view.routes)
except(OSError):
    pass

# Creates all tables not created for each view that was imported above
# db.create_all()
