flask-vagrant-starter
=========
A framework for a new flask project utilizing vagrant for setting up the development environment and gulp as the task runner.

READ THIS FIRST (DO NOT IGNORE): https://gist.github.com/chiedojohn/c3e37041b829f28c0c78
----------

Local Development Environment
----------
- Once inside your vagrant virtual machine, navigate to /vagrant in your vm to get to your flask app the run:
```
sudo pip install -r requirements.txt
```
-To run tests and tasks for static assets, open up a new tab with the vagrant VM and run the following:
```
gulp
```
-To run the application, enter the following from within your vagrant VM at /vagrant:
```
python run.py
```
