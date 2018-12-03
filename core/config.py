from os.path import abspath, dirname

white_list = [
    '/accounts/avatar',
    '/accounts/_avatar',
    '/accounts/not_logined',
    '/accounts/logout',
    '/accounts/pic_captcha',
    '/user/login',
    '/other/landing_page',
    '/other/upload_img',
    '/other/tmp_proxy',
    '/other/get_test_comic_images',
]

base_dir = abspath(dirname(__file__))
print(base_dir)


class BaseConfig:
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    SECRET_KEY = 'CmNDp9oi9uj2OeW2P0E1w932lk'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']
    MONGODB_DB = 'flask_project'
    FLASK_ADMIN_SWATCH = 'cerulean'

    JSON_ADD_STATUS = False
    JSON_DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'


class DebugConfig(BaseConfig):
    pass
