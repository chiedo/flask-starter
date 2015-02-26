flask-vagrant-starter
=========
A framework for a new flask project utilizing vagrant for setting up the development environment and gulp as the task runner.

READ THIS FIRST (DO NOT IGNORE): https://gist.github.com/chiedojohn/c3e37041b829f28c0c78
----------

Local Development Environment
----------
- To get the necessary node packages installed, run
```
sudo npm install gulp -g
npm install
```
- Once inside your vagrant virtual machine, navigate to /vagrant in your vm to get to your flask app the run:
```
sudo pip install -r requirements.txt
```
- To run tests and tasks for static assets, open up a new tab with the vagrant VM and run the following:
```
gulp
```
- To run tests alone, run
```
nosetests --rednose --force-color --nocapture
```
- To run the application, enter the following from within your vagrant VM at /vagrant:
```
python app.py runserver -h 0.0.0.0
```
- To handle migrations, we are using Flask-Migrate. Obviously, since you will be starting a new project, you will want to remove all migrations created for this demo before starting your project and initalizing your migrations. See the docs: https://flask-migrate.readthedocs.org/en/latest/
