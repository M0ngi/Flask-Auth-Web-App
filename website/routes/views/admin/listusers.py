from website.const.init_roles import ADMIN_ROLE_ID
from website.utils.role import role_required
from website.utils.jwt import token_required
from .route import admin

@admin.route("users")
@token_required()
@role_required(ADMIN_ROLE_ID)
def listusers(user):
    return "Hi"