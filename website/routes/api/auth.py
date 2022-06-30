from crypt import methods
from .route import api
from flask import jsonify, make_response, Blueprint


auth = Blueprint('auth', __name__, url_prefix='auth/')

@auth.route('login', methods=['POST'])
def login():
    return make_response(jsonify(error="Work in progress"), 206)


@auth.route('/signup', methods=['POST'])
def signup():
    return make_response(jsonify(error="Work in progress"), 206)


@auth.route('logout', methods=['POST'])
def logout():
    return make_response(jsonify(error="Work in progress"), 206)


api.register_blueprint(auth)
