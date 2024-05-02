from flask import Flask, request, jsonify, Blueprint, session
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
import logging

auth_bp = Blueprint('auth', __name__)

# Configure logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

# User Registration Endpoint
@auth_bp.route('/register', methods=['POST'])
def register(mysql):
    try:
        # Extract user data from request
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        full_name = data.get('full_name')
        phone = data.get('phone')

        # Validate required fields
        if not username or not email or not password or not full_name:
            return jsonify({'error': 'Missing required fields'}), 400

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create MySQL cursor
        cursor = mysql.get_db().cursor()

        # Check if the username or email already exists
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        user = cursor.fetchone()
        if user:
            return jsonify({'error': 'Username or email already exists'}), 400

        # Insert user data into the database
        cursor.execute("INSERT INTO users (username, email, password, full_name, phone) VALUES (%s, %s, %s, %s, %s)",
                       (username, email, hashed_password, full_name, phone))
        mysql.get_db().commit()
        cursor.close()

        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        # Log the error
        logging.error(f"Error during user registration: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred, please try again later'}), 500

# User Login Endpoint
@auth_bp.route('/login', methods=['POST'])
def login(mysql):
    try:
        # Extract login credentials from request
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate required fields
        if not username or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create MySQL cursor
        cursor = mysql.get_db().cursor()

        # Fetch user data from the database
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if not user:
            return jsonify({'error': 'Invalid username or password'}), 401

        # Check if the password is correct
        if check_password_hash(user[3], password):
            # User authenticated successfully
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401

    except Exception as e:
        # Log the error
        logging.error(f"Error during user login: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred, please try again later'}), 500

# User Logout Endpoint
@auth_bp.route('/logout', methods=['POST'])
def logout():
    try:
        # Clear session data
        session.clear()

        return jsonify({'message': 'Logout successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500