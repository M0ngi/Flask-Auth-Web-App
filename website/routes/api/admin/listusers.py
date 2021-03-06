from website.const.init_roles import ADMIN_ROLE_ID
from website.services.users import findAll, userToJSON
from website.utils.http_response import valid_response
from website.utils.role import role_required
from website.utils.jwt import api_token_required
from .route import admin

@admin.route("users")
@api_token_required
@role_required(ADMIN_ROLE_ID, api=True)
def listusers(user):
    users = findAll()
    users = [userToJSON(user) for user in users]
    return valid_response(result=users, code=200)