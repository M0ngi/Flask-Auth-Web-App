from functools import wraps
from flask import flash, request, current_app, redirect, url_for
import jwt
import datetime
from website.models.user import User
from website.services.users import findOne
from website.utils.http_response import error_response


def token_required(required=True):
    def token_verifier(f):
        def notAuthorized():
            if required:
                flash('You must be logged in!')
                return redirect(url_for('web.login'))
            return redirect(url_for('web.home'))
        
        @wraps(f)
        def decorator(*args, **kwargs):
            token = None
            if 'auth' in request.cookies:
                token = request.cookies.get('auth')
            
            valid, current_user = isTokenValid(token)
            if valid != required:
                return notAuthorized()

            return f(current_user, *args, **kwargs)
        return decorator
    return token_verifier


def api_token_required(f):
    def notAuthorized():
        return error_response(error="Invalid access token", code=401)
    
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'auth' in request.json:
            token = request.json['auth']

        valid, current_user = isTokenValid(token)
        if not valid:
            return notAuthorized()

        return f(current_user, *args, **kwargs)
    return decorator


def createToken(user : User):
    token = jwt.encode(
        {
            'user_id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
        },
        current_app.config['SECRET_KEY'],
        "HS256"
    )
    return token


def isTokenValid(token : str) -> tuple[bool, User or None]:
    if not token:
        return False, None
    
    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        current_user = findOne(data['user_id'])

        if not current_user:
            raise Exception
    except Exception as e:
        print(e)
        return False, None

    return True, current_user
