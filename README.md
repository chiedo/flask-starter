flask-vagrant-starter
=========
A framework for a new flask project utilizing vagrant for setting up the development environment and gulp as the task runner.

READ THIS FIRST (DO NOT IGNORE): https://gist.github.com/chiedojohn/c3e37041b829f28c0c78
----------

Installing Needed Packages (navigate to  /vagrant)
----------
- For some reason Vagrant doesn't properly install lxml and needed packages, so run
```
sudo apt-get install libxml2-dev libxslt1-dev libxslt-dev python-dev
```
- To get the necessary node packages installed, run
```
sudo npm install gulp -g
npm install
```
- Install the needed pip packages.
```
sudo pip install -r requirements.txt
```

Local Development Environment
----------
- To the automatic reloaded for runing tests, compiling static assets, and more open up a new tab with the vagrant VM and run the following:
```
gulp
```
- To handle migrations, we are using Flask-Migrate.

Running Your Application
----------
- To run the application, enter the following from within your vagrant VM at /vagrant:
```
python app.py runserver -h 0.0.0.0
```

Testing
----------
- To run tests alone, or specifiy a specific test, we are using nosetests. See the nosetests documentation for more options.
```
nosetests --rednose --force-color --nocapture
```

Some Helpful External Docs
-----------
- Flask - http://flask.pocoo.org/
- Flask-Migrate - https://flask-migrate.readthedocs.org/en/latest/
