import json
from flask import current_app
from requests import post, get, Response


def apiGet(route : str, data : dict = {}, params : dict = {}) -> tuple[Response, dict]:
    resp = get(
        current_app.config["API_PROXY"] + route,
        headers={'Content-type': 'application/json', 'Accept': 'text/plain'},
        data=json.dumps(data),
        params=params
    )
    return resp, respJSON(resp)


def apiPost(route : str, params : dict = {}) -> tuple[Response, dict]:
    resp = post(
        current_app.config["API_PROXY"] + route, 
        data=json.dumps(params),
        headers={'Content-type': 'application/json', 'Accept': 'text/plain'}
    )
    return resp, respJSON(resp)


def respJSON(resp : Response) -> dict:
    try:
        resp_data = json.loads(resp.content.decode())
    except Exception:
        resp_data = {}
    return resp_data