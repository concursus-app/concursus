import mysql.connector
import logging
import time
import dotenv
import os
import bcrypt
import hashlib

from mysql.connector.abstracts import MySQLConnectionAbstract 
from mysql.connector.pooling import PooledMySQLConnection

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] (%(name)s) - %(message)s")

file_handler = logging.FileHandler("output/.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

dotenv.load_dotenv()

config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT')
}

def make_connection(attempts: int = 3, delay: int = 2) -> PooledMySQLConnection | MySQLConnectionAbstract | None:
    """
    Creates a connection to the database as specified by the `config` dict.
    """
    attempt = 1
    while attempt < attempts + 1:
        try:
            cnx = mysql.connector.connect(**config)
            logger.info("Successfully fetched connection: %s", str(cnx))

            return cnx
        except (mysql.connector.Error, IOError) as err:
            if (attempts is attempt):
                logger.error("Failed to fetch connection, exiting without a connection (Error: %s)", err)
                return None
            
            logger.warning(
                "Connection failed. Retrying (%d/%d) (Error: %s)",
                err,
                attempt,
                attempts
            )

            time.sleep(delay ** attempt)
            attempt += 1

    return None

def make_tables(tables: dict[str, str]):
    """
    Makes the tables provided in the tables dict.

    Args:
        tables: A dict of table name to table creation command

    Returns:
        A response dict
    """

    cnx = make_connection()
    if not cnx:
        return {
            'status': 503,
            'details': 'Could not make connection to database'
        }
    
    created_tables = 0
    failed_tables = []
    with cnx.cursor(buffered=True) as cursor:
        for table_name, command in tables.items():
            logger.info("Creating table %s", table_name)
            try:
                cursor.execute(command)
                created_tables += 1
            except mysql.connector.Error as err:
                logger.error("Error in creating table: %s", err)
                failed_tables.append(table_name)

        cnx.commit()
        logger.info("Table creation commands committed to database.")

    cnx.close()

    return {
        'status': 200,
        'details': {
            'created_tables': created_tables,
            'total_tables': len(tables),
            'failed_tables': failed_tables
        }
    }

def check_user_exists(username: str | None = None, email: str | None = None) -> bool | dict:
    if not (username or email):  # Neither username nor email was specified:
        logging.error("`check_user_exists` called without username and email parameters.")
        return False

    cnx = make_connection()
    if not cnx:
        return {
            'status': 503,
            'details': 'Could not make connection to database'
        }

    with cnx.cursor(buffered=True) as cursor:
        if username:
            cursor.execute(
                "SELECT username FROM users "
                "WHERE username = %s",
                (username,)
            )
            if cursor.fetchone():
                return True
        
        if email:
            cursor.execute(
                "SELECT email FROM users "
                "WHERE email = %s",
                (email,)
            )
            
            return cursor.fetchone() is not None

    # If this runs, something is fucked up.
    return False

def drop_tables(tables):
    cnx = make_connection()  
    if not cnx:
        return {
            'status': 503,
            'details': 'Could not make connection to database'
        }

    with cnx.cursor() as cursor:
        for table in tables:
            cursor.execute(f"DROP TABLE {table}")

        cnx.commit()

    cnx.close()

    return {
        'status': 200
    }


def register_user(email, username, password):
    cnx = make_connection()
    if not cnx:
        return {
            'status': 503,
            'details': 'Could not make connection to database'
        }

    with cnx.cursor() as cursor:
        salt = bcrypt.gensalt()  # 29 bytes long
        hashed_password = hashlib.scrypt(
            bytes(password, encoding='utf-8'),
            salt=salt,
            n=2 ** 14,
            r=8,
            p=1
        )  # 64 long binary

        cursor.execute(
            "INSERT INTO users "
            "(email, username, password, salt, bio) "
            "VALUES (%s, %s, %s, %s, '')",
            (email, username, hashed_password, salt)
        )

    cnx.commit()
    cnx.close()

    return {
        'status': 200
    }

def fetch_all_users():
    cnx = make_connection()
    if not cnx:
        return {
            'status': 503,
            'details': 'Could not make connection to database'
        }


    with cnx.cursor() as cursor:
        cursor.execute("SELECT username, email FROM users")
        res = cursor.fetchall()

    cnx.close()

    return {
        'status': 200,
        'details': res
    }


