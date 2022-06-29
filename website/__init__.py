from flask import Flask
import os

from website.routes import views


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getrandom(25)
    app.config['API_PROXY'] = "http://0.0.0.0:5000/"

    from .routes.views import web
    from .routes.api import api

    app.register_blueprint(web, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api/')
    
    return app