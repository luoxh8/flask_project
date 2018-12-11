from flask import Blueprint
from flask_json import as_json

from models.others import Banner
from utils.error import error_data
from utils.generator import gen_bid
from utils.libs import safe_data_list
from utils.success import success_response_list, success_response_dict

others = Blueprint('others', __name__)


@others.route('/banners/create', methods=['POST'])
@as_json
def create():
    data = {
        'title'     : 'hello world',
        'platform'  : 'ios',
        'url'       : 'www.baidu.com',
        'banner_url': 'www.baidu.com',
    }
    banner = Banner(
        id=gen_bid(),
        title=data['title'],
        platform=data['platform'],
        url=data['url'],
        banner_url=data['banner_url'],
    ).save()
    return_data = success_response_dict()
    return_data['data'] = banner.to_dict()
    return return_data


@others.route('/banners/list')
@as_json
def list():
    banners = Banner.objects()
    if not banners: return error_data
    return_data = success_response_list()
    return_data['data'] = safe_data_list(banners)
    return return_data


@others.route('/config')
@as_json
def config():
    data = {
        'ios_test'    : False,
        'force_update': False,
        'check_update': {
            "appVersion" : 100,
            "changeLog"  : "更新内容",
            "downloadUrl": "https://www.baidu.com",
        },
    }
    return data
