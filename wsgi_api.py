import traceback
from configparser import ConfigParser

from manage import (manager,
                    MyServer)

try:
    config_parser = ConfigParser()
    config_parser.read("conf/flask_project.ini")
    sever_type = config_parser.get("xx_server", "type")
    if sever_type == "dev":
        print("run with DebugConfig")
        manager.add_command('run', MyServer())
    else:
        manager.add_command('run', MyServer())
except Exception as e:
    print(traceback.format_exc())

if __name__ == '__main__':
    manager.run()

'''
uwsgi --http :8080 --wsgi-file manage.py run
'''
