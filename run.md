gunicorn -b 0.0.0.0:8000 --worker-class eventlet -w 1 app:app

ln -s /root/flask_project/conf/flask_project.conf /etc/supervisor/conf.d/flask_project.conf