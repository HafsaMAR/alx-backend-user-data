#!/usr/bin/env python3
'''flask app module'''


from flask import Flask, jsonify, request
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
