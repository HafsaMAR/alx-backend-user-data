#!/usr/bin/env python3
'''view session'''


# api/v1/views/session_auth.py

from flask import Blueprint, jsonify, request

# Create a Blueprint for session authentication views
session_auth_bp = Blueprint(
    'session_auth', __name__,
    url_prefix='/api/v1/auth_session')


# Route for the POST /auth_session/login endpoint
@session_auth_bp.route('/login', methods=['POST'])
def login():
    # Get username and password from request data
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Example login logic
    if username == 'example_user' and password == 'example_password':
        # For demonstration purposes, return a success message
        return jsonify({'message': 'Login successful'}), 200
    else:
        # Return an error message if login fails
        return jsonify({'message': 'Invalid username or password'}), 401
