# socketio
from threading import Lock

from flask_json import FlaskJSON
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO

async_mode = None
thread_lock = Lock()
io = SocketIO(async_mode=async_mode)
db = MongoEngine()
json = FlaskJSON()
