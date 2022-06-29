from .route import web


@web.route('/')
def home():
    return "<h1>Hi</h1>"
