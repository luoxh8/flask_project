from flask_script import (Command, Manager)

from core import create_app
from core.config import BaseConfig

app = create_app(BaseConfig)

manager = Manager(app)


class MyServer(Command):
    def __call__(self, *args, **kwargs):
        app.run('0.0.0.0', 8080, threaded=True, use_reloader=True)


manager.add_command('run', MyServer())

if __name__ == '__main__':
    manager.run()
