from os.path import abspath, dirname

# 白名单
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

# 手动在最后添加/，因为abspath不会末尾没有/
base_dir = abspath(dirname(__file__)) + '/..'
print(base_dir)


class BaseConfig:
    # 前端babel的语言
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    # 秘钥用来使用加密的session
    SECRET_KEY = 'CmNDp9oi9uj2OeW2P0E1w932lk'
    # 开发模式
    DEBUG = True
    # mysql的配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # debug下打印查询语句
    DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']
    # MongoDB的数据库
    MONGODB_DB = 'flask_project'

    FLASK_ADMIN_SWATCH = 'cerulean'

    # flask_json配置
    JSON_ADD_STATUS = False
    JSON_DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'

    MONGODB_SETTINGS = {
        'db': 'flask_project',
        'host': 'mongodb://localhost/flask_project',
        'connect': False,
    }


class DebugConfig(BaseConfig):
    pass
