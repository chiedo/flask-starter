# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config.BaseConfiguration')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import Contollers
import webapp.controllers.index as index
import webapp.controllers.person as person

# Creates all tables not created
db.create_all()


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# To build the database import db from this app and all the models then
# run db.create_all() in the interactive python shell.

# Register blueprints
app.register_blueprint(index.routes)
app.register_blueprint(person.routes, url_prefix='/person')
