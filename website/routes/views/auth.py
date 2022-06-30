import requests
from .route import web
from flask import flash, render_template, request, current_app, url_for, redirect
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


@web.route('logout', methods=['GET'])
def logout():
    try:
        resp = requests.post(current_app.config["API_PROXY"]+url_for('api.auth.logout'))
    except Exception:
        flash("An unknown error occured.", category="error")
        return render_template('error.html')
    
    if resp.status_code != 200:
        try:
            resp_data = json.loads(resp.content.decode())
        except Exception:
            resp_data = {}
        
        if 'error' not in resp_data:
            resp_data['error'] = 'An unknown error occured.'
        
        flash(resp_data['error'], category="error")
        return render_template('error.html')
    
    return redirect(url_for('web.login'))


@web.route('signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName') 
    login = request.form.get('login')
    password = request.form.get('password')

    if not firstName:
        flash("First name is required!", category="error")
        return render_template(
            'signup.html'
        )

    if not lastName:
        flash("Last name is required!", category="error")
        return render_template(
            'signup.html', 
            data={
                "firstname": firstName,
                "lastname": "",
                "login": "",
            }
        )
    
    if not login:
        flash("Email is required!", category="error")
        return render_template(
            'signup.html', 
            data={
                "firstname": firstName,
                "lastname": lastName,
                "login": "",
            }
        )

    if not password:
        flash("Password is required!", category="error")
        return render_template(
            'signup.html', 
            data={
                "firstname": firstName,
                "lastname": lastName,
                "login": login,
            }
        )

    try:
        resp = requests.post(current_app.config["API_PROXY"]+url_for('api.auth.login'))
    except Exception:
        flash("An unknown error occured.", category="error")
        return render_template('signup.html')
    
    if resp.status_code == 200:
        flash("Account created successfully", category="success")
        return render_template('signup.html')
    
    try:
        resp_data = json.loads(resp.content.decode())
    except Exception:
        resp_data = {}
    
    if 'error' not in resp_data:
        resp_data['error'] = 'An unknown error occured.'
    
    flash(resp_data['error'], category="error")
    return render_template('signup.html')
