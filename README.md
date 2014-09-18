flask-vagrant-starter
=========
A framework for a new flask project utilizing vagrant for setting up the development environment and gulp as the task runner.

Local Development Environment
----------
> Requirements: Vagrant and Virtual Box

> It will be assumed that you are familiar with vagrant.

> ####Local Mysql port: 5433

> ####Local http port: 3001

> ####Mysql username: root

> ####Mysql password: root

> ####Existing database: flask_app_default


- Once inside your vagrant virtual machine, navigate to /vagrant in your vm to get to your flask app the run:
```
sudo pip install -r requirements.txt
```
-To run tests and tasks for static assets, open up a new tab with the vagrant VM and run the following:
```
gulp
```
-To run the application, enter the following from within your vagrant VM:
```
python run.py
```

###Notes:
>* If you have an issue with mysql not connecting, you may need to restart mysql by running 'sudo service mysql restart'
>* Be sure to delete the .git folder after cloning this repo if you intend to use it for a completely unrelated project.

###Notes for elastic beanstalk users:
>* You should do all of your elastic beanstalk interaction via the vagrant VM. You should only need to run 'eb init' if you are the first person who hooks up the repository to Elastic Beanstalk. After you do this, make sure .elasticbeanstalk/ and .ebextensions/ ARE NOT in .gitignore.
>* Everyone who intends to push changes to Elastic Beanstalk will need to set up their AWS credential file at '/home/vagrant/.elasticbeanstalk/aws_credential_file'.
