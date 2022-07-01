from website import db
from website.models.user import User
from werkzeug.security import generate_password_hash


def createUser(email : str, password : str, firstname : str, lastname : str) -> User:
    new_acc = User(
        firstName=firstname,
        lastName=lastname,
        email=email,
        password=generate_password_hash(password, 'sha256')
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
