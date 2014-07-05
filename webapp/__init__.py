# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('webapp.config.BaseConfiguration')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Creates all tables not created
db.create_all()
