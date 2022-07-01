from website.services.users import createUser, findOneByEmail
from website.utils.http_response import error_response, valid_response
from website.utils.jwt import createToken
from .route import api
from flask import Blueprint, request
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, url_prefix='auth/')


@auth.route('login', methods=['POST'])
def login():
    data = request.json
    if 'login' not in data or 'password' not in data:
        return error_response(error="Fields are missing", code=400)
    
    if len(data['login']) == 0 or len(data['password']) == 0:
        return error_response(error="Fields are missing", code=400)
    
    user = findOneByEmail(data['login'])
    if check_password_hash(user.password, data['password']):
        token = createToken(user)

        return valid_response(result={"token": token}, code=200)
    return error_response(error="Invalid email/password.", code=401)


@auth.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if 'firstname' not in data or 'lastname' not in data or 'login' not in data or 'password' not in data:
        return error_response(error="Fields are missing", code=400)
    
    if len(data['firstname']) == 0 or len(data['lastname']) == 0 or len(data['login']) == 0 or len(data['password']) == 0:
        return error_response(error="Fields are missing", code=400)
    
    createUser(email=data['login'], password=data['password'], firstname=data['firstname'], lastname=data['lastname'])
    return valid_response(result="Account created successfully!", code=200)


@auth.route('logout', methods=['POST'])
def logout():
    return error_response(error="Work in progress", code=423)


api.register_blueprint(auth)
