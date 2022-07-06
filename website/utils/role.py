from functools import wraps
from flask import redirect, url_for


def role_required(role):
    def decorator(f):
        def notAuthorized():
            return redirect(url_for('web.home'))
        
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = args[0]

            if user.role == role:
                return f(*args, **kwargs)
            return notAuthorized()
        
        return wrapper
    return decorator