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
5. Navigate to the application directory and start the python server
```
cd /vagrant
python manage.py runserver 0.0.0.0:8000
```
6. To run tests and tasks, create another tab, start vagrant ssh and run:
```
gulp
```
