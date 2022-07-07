from website import db
from website.const.init_roles import ADMIN_ROLE_ID, USER_ROLE_ID
from website.models.user import User
from werkzeug.security import generate_password_hash


def createUser(email : str, password : str, firstname : str, lastname : str) -> User:
    new_acc = User(
        firstName=firstname,
        lastName=lastname,
        email=email,
        password=generate_password_hash(password, 'sha256'),
        role=USER_ROLE_ID
    )
    db.session.add(new_acc)
    db.session.commit()
    return new_acc


def findOneByEmail(email : str) -> User or None:
    try:
        return User.query.filter_by(email=email).first() 
    except:
        return None


def findOne(id : int) -> User or None:
    try:
        return User.query.filter_by(id=id).first() 
    except:
        return None


def findAll() -> list[User]:
    try:
        return User.query.all()
    except:
        return []


def userToJSON(user : User) -> dict:
    return {
        "id": user.id,
        "email": user.email,
        "password": user.password,
        "firstname": user.firstName,
        "lastname": user.lastName,
        "role": user.role
    }