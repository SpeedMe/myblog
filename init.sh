pip install virtualenv
virtualenv -p python3 env3
source env3/bin/activate

apt-get install mysql-server
apt-get install libmysqlclient-dev
apt-get install gcc
apt-get install python3-dev

pip install -r requirements.txt
mkdir instance
cp config.example.py instance/config.py
