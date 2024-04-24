#!/usr/bin/env python3
'''flask app module'''


from flask import Flask, jsonify, request, abort
from auth import Auth

Auth = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    '''welcome method'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def user_register() -> str:
    '''End_point to register new users
    '''
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    '''check credentials to login / abort otherwise
    '''
    email = request.form.get('email')
    password = request.form.get('password')

    if Auth.valid_login(email, password):
        session_id = Auth.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
