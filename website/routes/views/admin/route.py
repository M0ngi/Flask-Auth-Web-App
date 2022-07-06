from flask import Blueprint
from website.routes.views.route import web


admin = Blueprint("admin", __name__)
web.register_blueprint(admin, url_prefix="/admin/")