from .route import web
from flask import render_template


@web.route('login')
def login():
    return render_template('login.html')


@web.route('logout')
def logout():
    return render_template('logout.html')


@web.route('signup')
def signup():
    return render_template('signup.html')