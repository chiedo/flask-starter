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
>* Install Elastic Beanstalk command line tools. If using a mac, you can use homebrew and use the following:
```
brew install aws-elasticbeanstalk
```
>* Before you can push to Elastic Beanstalk for the first time, you will need to navigate to your git repo on your local machine then run the following
```
eb init
```
>*AFTER YOU DO THIS, MAKE SURE .elasticbeanstalk/ and .ebextensions/ ARE NOT in .gitignore.
>* It is recommended that after you run 'eb init', you update the path to your AWS credential file as found in /.elasticbeanstalk/config to /usr/local/AWS/.elasticbeanstalk/ENVIRONMENTNAME_credentials being sure to move the original file to the new path. You will likely have to create that path. This will prevent collisions when you have multiple projects using Elastic Beanstalk on one machine.
>* Elastic beanstalk deployment is currently untested. In theory, it should work.

