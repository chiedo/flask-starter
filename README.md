1. Download Vagrant
2. Download Virtualbox
3. To set up your Vagrant development environment, execute the following in the terminal:
```
vagrant up
```
4. To connect to your development environment, execute
```
vagrant ssh
```
5. Navigate to the application directory and start the python server. You will be able to see this server on your local machine at port 5001 in the browser.
```
cd /vagrant
python run.py
```
6. To run tests and tasks, create another tab, start vagrant ssh and run:
```
gulp
```
7. You can access the mysql server at port 3307 with the username root and the password root. 
8. You can stop vagrant by running 'vagrant halt' or completely destroy the vagrant machine by running 'vagrant destroy'.
