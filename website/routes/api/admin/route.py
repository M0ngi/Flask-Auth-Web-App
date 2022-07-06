from flask import Blueprint
from website.routes.api.route import api


admin = Blueprint("admin", __name__)
api.register_blueprint(admin, url_prefix="/admin/")