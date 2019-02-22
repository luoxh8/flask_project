from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/index')
def index():
    return render_template('admin/index.html')
