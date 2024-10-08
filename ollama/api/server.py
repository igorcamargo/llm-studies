#!/usr/bin/env python
import os
import importlib
from decouple import config
from flask import Flask, request, make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app     = Flask(__name__)
auth    = HTTPBasicAuth()
users   = {config('API_USER'): generate_password_hash(config('API_PASS'))}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@auth.error_handler
def auth_error(status):
    return __make_json_response({}, status)

@app.route('/health', methods=['GET'])
@auth.login_required
def health():
    try:
        return __make_json_response({'hello': 'world'})
    except Exception as e:
        print('[ERROR] - ', e)
        
        if len(e.args) == 2:
            message, code = e.args
            return __make_json_response({'error': message}, code)
        
        return __make_json_response({'error': str(e)}, 500)

@app.route('/<state>', methods=['GET'])
@auth.login_required
def state(state: str):
    try:
        if not request.is_json:
            raise Exception('Invalid payload!', 400)
        
        if not state:
            raise Exception('State route is required!', 400)

        module = importlib.import_module(f"states.{state}")
        execute = getattr(module, 'execute')

        return __make_json_response(execute(state, request.get_json(silent=True)))
    except Exception as e:
        print('[ERROR] - ', e)
        
        if len(e.args) == 2:
            message, code = e.args
            return __make_json_response({'error': message}, code)
        
        return __make_json_response({'error': str(e)}, 500)

def __make_json_response(content: dict, code: int = 200):
    response = make_response(content)
    response.headers['Content-Type'] = 'application/json'
    response.status = code
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
