from website.const.init_roles import ADMIN_ROLE_ID
from website.services.roles import findAll, roleToJSON
from website.utils.http_response import valid_response
from website.utils.role import role_required
from website.utils.jwt import api_token_required
from .route import admin

@admin.route("roles")
@api_token_required
@role_required(ADMIN_ROLE_ID, api=True)
def listroles(user):
    roles = findAll()
    roles = [roleToJSON(role) for role in roles]
    return valid_response(result=roles, code=200)