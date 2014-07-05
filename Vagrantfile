VAGRANTFILE_API_VERSION = "2"

# These are the scripts that will be run by the terminal upon creation of a new machine.
# The answer 'yes' is piped into the commands that require 'Y' as user input
$script = <<SCRIPT
yes | sudo apt-get install libpq-dev
yes | sudo apt-get install nodejs npm
yes | sudo apt-get install python-pip python-dev build-essential 
yes | sudo pip install --upgrade pip
yes | sudo apt-get install git
yes | sudo apt-get install vim-nox
yes | sudo apt-get install sqlite3 libsqlite3-dev
cd /vagrant
sudo pip install -r requirements.txt 
npm install

# This sets up postgresql
if [ ! -f /var/log/databasesetup ];
then
  # installs postgresql
  yes | sudo apt-get install postgresql postgresql-contrib
  yes | sudo apt-get install postgresql-client
  # sets 'postgres' as the password for the postgres user.
  sudo -u postgres psql -U postgres -d postgres -c "alter user postgres with password 'postgres';"
  # sets postgres to start automatically on the restarting of the machine
  postgres -D /usr/local/pgsql/data >/var/log/postgres.log 2>&1 &
  # make postgres accept connections from the host machine using the forwarded ports
  echo "listen_addresses = '*'" | sudo tee -a /etc/postgresql/9.3/main/postgresql.conf 
  echo "host    all    all    0.0.0.0/0    md5" | sudo tee -a /etc/postgresql/9.3/main/pg_hba.conf
  # restart postgres
  sudo service postgresql restart
  touch /var/log/databasesetup
fi
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  # forward the python runserver port
  config.vm.network "forwarded_port", guest: 5000, host: 5001
  # forward postgresql
  config.vm.network "forwarded_port", guest: 5432, host: 5433

  # run the script from above
  config.vm.provision "shell", inline: $script
  config.vm.synced_folder ".", "/vagrant", :mount_options => ['dmode=777,fmode=666']
end
