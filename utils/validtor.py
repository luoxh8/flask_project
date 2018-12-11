import re

from models.others import Banner
from models.users import User


def is_phone(phone):
    return re.match('^1[345789]\d{9}$', phone)


def is_nick(nick):
    return re.match('^[a-zA-Z0-9_\\u4e00-\\u9fa5]+$', nick)


def is_password(password):
    return re.match('^[a-zA-Z0-9_-]{6,30}$', password)


def is_code(code):
    return code == '66666'


def is_uid(id):
    if User.objects(pk=id):
        return True
    return False


def is_bid(id):
    if Banner.objects(pk=id):
        return True
    return False
