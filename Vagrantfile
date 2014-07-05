VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT
yes | sudo apt-get install libpq-dev
yes | sudo apt-get install nodejs
yes | sudo apt-get install python-pip python-dev build-essential 
yes | sudo pip install --upgrade pip
yes | sudo apt-get install git
yes | sudo apt-get install vim-nox
yes | sudo apt-get install sqlite3 libsqlite3-dev
cd /vagrant
sudo pip install -r requirements.txt 
npm install

if [ ! -f /var/log/databasesetup ];
then
  yes | sudo apt-get install postgresql postgresql-contrib
  yes | sudo apt-get install postgresql-client
  sudo -u postgres psql -U postgres -d postgres -c "alter user postgres with password 'postgres';"
  postgres -D /usr/local/pgsql/data >/var/log/postgres.log 2>&1 &
  echo "listen_addresses = '*'" | sudo tee -a /etc/postgresql/9.3/main/postgresql.conf 
  echo "host    all    all    0.0.0.0/0    md5" | sudo tee -a /etc/postgresql/9.3/main/pg_hba.conf
  sudo service postgresql restart
  touch /var/log/databasesetup
fi
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 8000, host: 8001
  config.vm.network "forwarded_port", guest: 5432, host: 5433

  config.vm.provision "shell", inline: $script
  config.vm.synced_folder ".", "/vagrant", :mount_options => ['dmode=777,fmode=666']
end
