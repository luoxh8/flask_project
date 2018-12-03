import random
import string

from flask import request

from utils.validtor import is_bid, is_uid


def gen_ip():
    return request.headers.get('X-Real-Ip') or request.remote_addr


def gen_random_string(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def gen_uid():
    zero_to_nine = string.digits
    one_to_nine = zero_to_nine[1:]

    def _uid():
        first = gen_random_string(1, one_to_nine)
        others = gen_random_string(6, zero_to_nine)
        return first + others

    while True:
        uid = _uid()
        if not is_uid(uid):
            return uid


def gen_bid():
    zero_to_nine = string.digits
    one_to_nine = zero_to_nine[1:]

    def _uid():
        first = gen_random_string(1, one_to_nine)
        others = gen_random_string(6, zero_to_nine)
        return first + others

    while True:
        id = _uid()
        if not is_bid(id):
            return id
