# Import flask and template operators
from flask import Flask
import os

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('project.config.BaseConfiguration')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Connect all the routes from the controllers
try:
    controller_names = []
    for file in [doc for doc in os.listdir("project/controllers") if doc.endswith(".py") and doc != "__init__.py"]:
        controller_names.append("project.controllers." + file.split(".")[0])  # remove the .py from the file name

    # Loop through all contollers and register their blueprint
    for controller_name in controller_names:
        # This dynamically imports all modules in the tests_to_run list. This allows me to import a module using
        # a variable. This is fairly advanced and hard to follow for the beginner.
        controller = __import__(controller_name, fromlist=[controller_name])
        if hasattr(controller, "routes"):
            app.register_blueprint(controller.routes)
except(OSError):
    exit()

# Creates all tables not created for each controller that was imported above
db.create_all()
