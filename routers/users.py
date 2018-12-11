from flask import Blueprint, request
from flask_json import as_json
from flask_login import current_user, login_required, login_user

from models.users import User
from utils.error import error_code, error_params, error_user_does_exist, error_user_does_not_exist, error_user_password
from utils.generator import gen_random_string, gen_uid
from utils.libs import hash_password, safe_data
from utils.success import success_response_dict
from utils.validtor import is_code, is_password, is_phone

users = Blueprint('users', __name__)


@users.route('/')
def index():
    return 'hello user'


@users.route('/login', methods=['POST'])
@as_json
def login():
    try:
        phone = request.form['phone']
        password = request.form['password']
    except KeyError:
        return error_params

    if not is_phone(phone): return error_params
    if not is_password(password): return error_params

    pwd = hash_password(password)

    user = User.objects(phone=phone).first()

    if not user: return error_user_does_not_exist
    if user.password != pwd: return error_user_password

    login_user(user)
    return_data = success_response_dict()
    safe_data(user._data)
    return_data['data'] = user.to_dict()
    return return_data


@users.route('/register', methods=['POST'])
@as_json
def register():
    try:
        phone = request.form['phone']
        password = request.form['password']
        code = request.form['code']
    except KeyError:
        return error_params

    if not is_phone(phone): return error_params
    if not is_password(password): return error_params
    if not is_code(code): return error_code

    if User.objects(phone=phone).first(): return error_user_does_exist

    user = User(id=gen_uid(),
                nickname='手机用户' + phone,
                phone=phone,
                password=hash_password(password),
                device_id=gen_random_string(40)).save()
    login_user(user)
    return_data = success_response_dict()
    safe_data(user._data)
    return_data['data'] = user.to_dict()
    return return_data


@users.route('/info', methods=['POST', 'GET'])
@login_required
@as_json
def info():
    if request.method == 'GET':
        user = User.objects(id=current_user.id).first()
        return_data = success_response_dict()
        safe_data(user)
        return_data['data'] = user.to_dict()
        return return_data
    user = User.objects(id=current_user.id).first()
    return_data = success_response_dict()
    safe_data(user._data)
    return_data['data'] = user.to_dict()
    return return_data
