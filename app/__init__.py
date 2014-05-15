# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
webapp = Flask(__name__)

# Configurations
webapp.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(webapp)

# Import Contollers
import app.controllers.index as index
import app.controllers.api.controller_1 as api_controller_1

# Uncomment the following to create the database. Can delete when done
# db.create_all()


# Sample HTTP error handling
@webapp.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# To build the database import db from this app and all the models then
# run db.create_all() in the interactive python shell.

# Register blueprints
webapp.register_blueprint(index.routes, url_prefix='')
webapp.register_blueprint(api_controller_1.routes,
                          url_prefix='/api/controller_1/')
