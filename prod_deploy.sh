#!/usr/bin/env bash

virtualenv env --python=python3
source env/bin/activate
pip install -r requirements.txt
ln -s /root/flask_project/conf/flask_project.conf /etc/supervisor/conf.d/flask_project.conf
