import time
from flask import Flask, request
from .utils.database_handler import make_connection
from .utils.database_handler import make_tables as mt
from .utils import admin_only

app = Flask(__name__)

TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `users` ("
    "`user_id` MEDIUMINT(8) UNSIGNED NOT NULL AUTO_INCREMENT,"
    "`email` VARCHAR(255) NOT NULL,"
    "`username` VARCHAR(50) NOT NULL,"
    "`password` CHAR(32) NOT NULL,"
    "`salt` CHAR(32) NOT NULL,"
    "`created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    "`bio` TEXT,"
    "PRIMARY KEY (`user_id`)"
    ") ENGINE=InnoDB"
)

@app.route('/time')
def get_time():
    """Test function"""
    return {'time': int(time.time())}

@app.route('/ensure-conn')
@admin_only
def get_conn():
    """ Ensures that connections can be made. """
    cnx = make_connection()
    return {
        'status': 200,
        'success': cnx is not None
    }


@app.route('/make-tables')
@admin_only
def make_tables():
    """ Makes the required tables """
    return mt(TABLES)

