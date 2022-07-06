from functools import wraps
from flask import redirect, url_for
from website.utils.http_response import error_response


def role_required(role, api=False):
    def decorator(f):
        def notAuthorized():
            if api:
                return error_response(error="Unauthorized", code=401)
            return redirect(url_for('web.home'))
        
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = args[0]

            if user.role == role:
                return f(*args, **kwargs)
            return notAuthorized()
        
        return wrapper
    return decorator