from .route import web
from flask import render_template

@web.route('/')
def home():
    return render_template("home.html")
