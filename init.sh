pip install virtualenv
virtualenv -p python3 env3
source env3/bin/activate
pip install -r requirements.txt
mkdir instance
cp config.example.py instance/config.py
