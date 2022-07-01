from website.utils.jwt import token_required
from .route import web
from flask import render_template

@web.route('/')
@token_required()
def home(user):
    return render_template("home.html")
