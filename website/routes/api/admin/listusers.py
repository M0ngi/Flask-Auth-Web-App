from website.const.init_roles import ADMIN_ROLE_ID
from website.utils.http_response import valid_response
from website.utils.role import role_required
from website.utils.jwt import api_token_required
from .route import admin

@admin.route("users")
@api_token_required
@role_required(ADMIN_ROLE_ID, api=True)
def listusers(user):
    return valid_response(result="WIP", code=200)