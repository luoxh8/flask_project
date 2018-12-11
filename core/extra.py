from threading import Lock

from flask_json import FlaskJSON
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO

from models.users import User

# flask-login
login_manager = LoginManager()


class UserInfo(object):
    def __init__(self, admin_id):
        self.id = admin_id

    def __str__(self):
        return '{}'.format(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


@login_manager.user_loader
def load_user(id):
    return User.objects(id=id).first()


# socketio
async_mode = None
thread_lock = Lock()
io = SocketIO(async_mode=async_mode)

# MongoDB
db = MongoEngine()

# json
json = FlaskJSON()
