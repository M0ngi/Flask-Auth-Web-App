from website.const.init_roles import USER_ROLE_ID
from website.models.role import Role

def findAll() -> list[Role]:
    try:
        return Role.query.all()
    except:
        return []


def roleToJSON(role : Role) -> dict:
    return {
        "id": role.id,
        "title": role.title
    }