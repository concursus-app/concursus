import dotenv
import os
from flask import request
from functools import wraps

dotenv.load_dotenv()

ADMIN_PASS = os.getenv("ADMIN_PASS")

def admin_only(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if request.args.get('password') == ADMIN_PASS:
            return func(*args, **kwargs)

        return {
            'status': 401,
            'details': "The given password was incorrect."
        }

    return inner

