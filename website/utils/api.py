import json
from flask import current_app
from requests import post, get


def apiGet(route : str, params : dict = {}):
    return get(
        current_app.config["API_PROXY"] + route, 
        data=params
    )


def apiPost(route : str, params : dict = {}):
    return post(
        current_app.config["API_PROXY"] + route, 
        data=json.dumps(params),
        headers={'Content-type': 'application/json', 'Accept': 'text/plain'}
    )