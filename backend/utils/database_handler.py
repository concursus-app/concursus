import mysql.connector
import logging
import time
import dotenv
import os

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

