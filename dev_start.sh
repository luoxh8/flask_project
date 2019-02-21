#!/usr/bin/env bash

gunicorn -b 0.0.0.0:8000 --worker-class eventlet -w 1 app:app
