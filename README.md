1. Be sure to remove the .git directory after you have downloaded this repository.
2. Download Vagrant
3. Download Virtualbox
4. To set up your Vagrant development environment, execute the following in the terminal:
```
vagrant up
```
5. To connect to your development environment, execute
```
vagrant ssh
```
6. Navigate to the application directory and start the python server. You will be able to see this server on your local machine at port 5001 in the browser.
```
cd /vagrant
python run.py
```
7. To run tests and tasks, create another tab, start vagrant ssh and run:
```
gulp
```
8. You can access the mysql server at port 5433 with the username root and the password root. 
9. You can stop vagrant by running 'vagrant halt' or completely destroy the vagrant machine by running 'vagrant destroy'.
