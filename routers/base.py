from flask import Blueprint, request, json, abort

from core.error import error_not_authenticate


class BaseRoute(object):
    route = Blueprint('base', __name__)

    def __init__(self):
        self.token = None

    def is_authenticate(self):
        def decorator(f):
            try:
                self.token = request.cookies['token']
            except KeyError:
                abort(401)
                return json.jsonify(error_not_authenticate)
            return f

        return decorator
