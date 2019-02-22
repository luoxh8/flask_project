import hashlib
import json
from urllib.parse import unquote

from flask import (abort, Flask, request)
from flask_mongoengine import MongoEngineSessionInterface

from core.config import (base_dir, white_list, BaseConfig)
from core.extra import db, json, login_manager
from core.generator import gen_ip


def reg_db(app):
    db.init_app(app)
    db.app = app


def reg_bp(app):
    from routers.users import users
    from routers.homes import homes
    from routers.others import others
    from routers.admin import admin

    app.register_blueprint(users)
    app.register_blueprint(homes)
    app.register_blueprint(others)
    app.register_blueprint(admin)


def reg_session(app):
    app.session_interface = MongoEngineSessionInterface(db)


def reg_auth(app):
    login_manager.init_app(app)
    login_manager.login_view = "users.login"


def reg_redis(app):
    pass


def reg_check_sn(app):
    @app.before_request
    def verify():
        if gen_ip() in ['127.0.0.1']:
            return

        try:
            version = request.args['v']
            old_key = request.args['sn']
            platform = request.args['platform'].lower()
            m_id = int(request.args['m_id'])
            time = request.args.get('t')
        except KeyError:
            abort(400)
            return

        if platform == 'ios':
            if m_id != -1:
                platform = 'ios_other'

        if request.path in white_list \
                or '/recharge/' in request.path \
                or '/notify/' in request.path:
            return

        # if (platform == 'android' and version < '1.0.5') \
        #         or (platform == 'ios' and version < '1.0.3'):
        #     return

        if platform not in ['android', 'ios', 'ios_other'] \
                or not app.config['API_SECRET_KEYS'].get(platform, {}).has_key(version):
            abort(400)
            return

        api_key = app.config['API_SECRET_KEYS'].get(platform).get(version)
        args = list()
        get_args = request.args
        post_args = request.form

        for key in get_args:
            if key.lower() != 'sn':
                for v in get_args.getlist(key):
                    arg_str = '%s=%s' % (key, v)
                    args.append(arg_str)
        for key in post_args:
            if key.lower() != 'sn':
                for v in post_args.getlist(key):
                    arg_str = '%s=%s' % (key, v)
                    args.append(arg_str)

        sorted_args = sorted(args)
        sorted_args.append(api_key)

        params = ''.join(sorted_args)
        md5 = hashlib.md5()
        md5.update(unquote(params.encode('UTF-8')))
        md5_str = md5.hexdigest()
        new_key = md5_str[:7]

        if old_key.lower() != new_key.lower():
            tmp_s = json.dumps({
                'get_params': request.args.to_dict(),
                'post_params': request.form.to_dict(),
                'sorted_params': params,
                'sorted_params_encoded': unquote(params.encode('UTF-8')),
                'server_sn': new_key.lower(),
                'client_sn': old_key.lower(),
                'server_md5': md5_str,
            })
            print('\r\n Error Verify >>>', tmp_s)
            # return tmp_s
            abort(400)
            return


def enable_logging(app):
    pass


def reg_json(app):
    json.init_app(app)


def create_app(config_class=None):
    app = Flask(__name__, template_folder=base_dir + '/templates')
    app.config.from_object(config_class if config_class else BaseConfig)

    reg_db(app)

    if not app.debug:
        enable_logging(app)

    reg_bp(app)
    reg_auth(app)
    reg_redis(app)
    reg_session(app)
    reg_json(app)
    # reg_check_sn(app)
    return app
