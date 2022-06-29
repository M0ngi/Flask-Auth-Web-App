import requests
from .route import web
from flask import flash, render_template, request, current_app, url_for
import json


@web.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    if not login or not password:
        flash("Email & password are required to login!", category="error")
        return render_template('login.html')

    try:
        resp = requests.post(current_app.config["API_PROXY"]+url_for('api.auth.login'))
    except Exception:
        flash("An unknown error occured.", category="error")
        return render_template('login.html')
    
    if resp.status_code == 200:
        pass
    
    try:
        resp_data = json.loads(resp.content.decode())
    except Exception:
        resp_data = {}
    
    if 'error' not in resp_data:
        resp_data['error'] = 'An unknown error occured.'
    
    flash(resp_data['error'], category="error")
    return render_template('login.html')


@web.route('logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')


@web.route('signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')