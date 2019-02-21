import hashlib

import requests
from flask import (current_app, request)


def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()


def get_define(group, name, config=None):
    if not config:
        config = current_app.config

    defines = config['DEFINES']
    return defines[group][name]


def channel_collect(p):
    """
        渠道数据收集
    """
    url = current_app.config['CHANNEL_URL'] + '/channel/collect'
    params = request.args.to_dict()
    params.update(p)
    try:
        requests.get(url, params, timeout=0.5)
    except:
        import traceback
        current_app.logger.info(traceback.format_exc())
        current_app.logger.info(str(params))


def allowed_file(filename):
    """
        统一某个文件
    :param filename:
    :return:
    """
    ALLOWED_EXTENSIONS = {'png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', 'gif', 'GIF'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def get_kick_key(user_id):
    return 'kick:%s' % user_id


def kick_out(user_id, exclude=''):
    """
        踢出某个用户
    :param user_id:
    :param exclude:
    :return:
    """
    current_app.redis.set(get_kick_key(user_id), exclude, ex=36000)


def safe_data(data):
    """
        None判空，保护客户端
    :param data: 源data
    :return: 修改后的data
    """
    for k in data:
        if data[k] is None:
            data[k] = ''


def safe_data_list(data):
    """
       安全的将null数据转化为空字符串
    :param data:
    :return:
    """
    list = []
    for d in data:
        safe_data(d)
        list.append(d.to_dict())
    return list
