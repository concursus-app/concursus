import time
from flask import Flask, request

from .routes.auth import app as auth_app
from .routes.admin import app as admin_app 

app = Flask(__name__)
app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(admin_app, url_prefix='/admin')

print(app.url_map)


@app.route('/time')
def get_time():
    """Test function"""
    return {'time': int(time.time())}

