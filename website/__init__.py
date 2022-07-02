from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy 


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hard code for debug" # os.getrandom(25)
    app.config['API_PROXY'] = "http://0.0.0.0:5000/"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .routes.views import web
    from .routes.api import api

    app.register_blueprint(web, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api/')

    from .models import Log, User, Role

    createDb(app)
    return app


def createDb(app):
    if not os.path.exists('website/'+DB_NAME):
        db.create_all(app=app)

        from website.const.init_roles import DEFAULT_ROLES
        from .models import Role

        for role in DEFAULT_ROLES:
            r = Role(title=role['title'])
            db.session.add(r)
        
        db.session.commit()


db = SQLAlchemy()
DB_NAME = "database.db"