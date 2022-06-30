from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy 
from website.routes import views


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getrandom(25)
    app.config['API_PROXY'] = "http://0.0.0.0:5000/"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .routes.views import web
    from .routes.api import api

    app.register_blueprint(web, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api/')

    from .models import Log, User

    createDb(app)
    return app


def createDb(app):
    if not os.path.exists('website/'+DB_NAME):
        db.create_all(app=app)


db = SQLAlchemy()
DB_NAME = "database.db"