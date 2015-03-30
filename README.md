flask-starter
=========
<img src="https://travis-ci.org/chiedojohn/flask-starter.svg?branch=master" />

A framework for a new flask project utilizing vagrant or docker 1.5.0 for setting up the development environment and gulp as the task runner. 

Platform specific notes
====================
Docker Notes
---------
First read: https://gist.github.com/chiedojohn/e7ece910ef4a7e3ce125

You will need to set up a file by the name of .env in the root of your project to store private environments that should not be committed to the git repository. It should have the following contents that you can customize if needed.
```
#FLASK
FLASK_ENV=development
FLASK_SECRET_KEY=NONE
FLASK_CSRF_SESSION_KEY=NONE

#MYSQL
MYSQL_DATABASE=app_development
MYSQL_USER=admin
MYSQL_PASS=admin
# This is using the docker link
MYSQL_HOSTNAME=db
MYSQL_PORT=3306
```

Vagrant Notes
---------
First read: https://gist.github.com/chiedojohn/c3e37041b829f28c0c78


Local Development Environment
=============
- To set up automatic compiling static assets, and more open up a new tab on your local machine and run the following:
```
gulp
```
- You may need to first set run npm install and run npm install -g gulp on your local machine.
- To handle migrations, we are using Flask-Migrate.

Running Your Application
==============
- To run the application, enter the following within your vm or container:
```
python app.py runserver -h 0.0.0.0
```

Testing
=============
- To run tests alone, or specifiy a specific test, we are using nosetests. See the nosetests documentation for more options.
```
nosetests --rednose --force-color --nocapture
```

Some Helpful External Docs
=============
- Flask - http://flask.pocoo.org/
- Flask-Migrate - https://flask-migrate.readthedocs.org/en/latest/
