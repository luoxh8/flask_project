from flask import Blueprint, render_template

from routers.base import BaseRoute


class AdminRoute(BaseRoute):


    @admin.route('/index')
    def index(self):
        return render_template('admin/index.html')


admin_route = AdminRoute()
