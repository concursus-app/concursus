from flask import Blueprint
from ..utils import admin_only
from ..utils.database_handler import make_connection

from ..utils.database_handler import make_tables as mt
from ..utils.database_handler import drop_tables as dt
from ..utils.database_handler import fetch_all_users as fau

app = Blueprint('admin', __name__)

TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `users` ("
    "`user_id` MEDIUMINT(8) UNSIGNED NOT NULL AUTO_INCREMENT,"
    "`email` VARCHAR(255) NOT NULL,"
    "`username` VARCHAR(50) NOT NULL,"
    "`password` BINARY(64) NOT NULL,"
    "`salt` CHAR(29) NOT NULL,"
    "`created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    "`bio` TEXT,"
    "PRIMARY KEY (`user_id`)"
    ") ENGINE=InnoDB"
)

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

@app.route('/drop-tables')
@admin_only
def drop_tables():
    """ Drops all tables """
    return dt(TABLES)

@app.route('/all-users')
@admin_only
def fetch_all_users():
    return fau()

