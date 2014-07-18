from flask import render_template
from walraven import app


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import Contollers
import webapp.controllers.static_pages as static_pages
import webapp.controllers.index as index
import webapp.controllers.person as person

# Register blueprints and their routes
app.register_blueprint(static_pages.routes)
app.register_blueprint(index.routes)
app.register_blueprint(person.routes, url_prefix='/person')
