from flask import Blueprint, request
from ..utils.database_handler import check_user_exists, register_user as ru
import logging
import datetime
import jwt
import dotenv
import os

app = Blueprint('auth', __name__)
logger = logging.getLogger(__name__)

dotenv.load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

def _encode_auth_token(username: str):
    """ Encodes the given username into a JSON web token """
    try:
        payload = {
            'exp': datetime.datetime.now() + datetime.timedelta(days=7),
            'iat': datetime.datetime.now(),
            'sub': username
        }

        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as err:
        return err


@app.route('/register', methods=['POST']) 
def register_user():
    data = request.get_json()
    
    match data:
        case {
            'email': email,
            'username': username,
            'password': _  # We don't care about the password because the data dict is being passed as a whole to the database_handler.register_user function
        }:
            if check_user_exists(email=email):
                return {
                    'status': 409,
                    'details': 'The specified email is already in use.'
                }
            
            if check_user_exists(username=username):
                return {
                    'status': 409,
                    'details': 'The specified username is already in use.'
                }

            auth_token = _encode_auth_token(username)
            res = ru(**data)

            if res['status'] == 200:
                return {
                    'status': 200,
                    'auth_token': auth_token
                }
        case _:
            logging.error(f"Malformed registration request: {data}")
            return {
                'status': 422,
                'details': 'Registration request was malformed.'
            }

