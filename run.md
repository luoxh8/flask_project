gunicorn -b 0.0.0.0:8000 --worker-class eventlet -w 1 app:app

ln -s /root/zh_flask/conf/zh_flask.conf /etc/supervisor/conf.d/zh_flask.conf