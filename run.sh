#!/bin/sh
locale-gen en_US.UTF-8
export LANG=en_US.UTF-8

cd /home/myblog
source env3/bin/activate
killall -9 gunicorn
gunicorn -w3 -k gevent app:app