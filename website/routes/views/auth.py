from .route import web


@web.route('login')
def login():
    return "Login"


@web.route('logout')
def logout():
    return "Logout"


@web.route('signup')
def signup():
    return "Signup"