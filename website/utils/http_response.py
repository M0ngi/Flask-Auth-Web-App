from flask import jsonify, make_response, Blueprint, request


def error_response(error, code : int):
    return make_response(jsonify(error=error), code)


def valid_response(result, code : int = 200):
    return make_response(jsonify(result=result), code)