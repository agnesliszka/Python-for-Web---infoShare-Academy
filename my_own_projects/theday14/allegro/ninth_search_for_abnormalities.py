# Standard library imports
import os
import sqlite3

# Project imports
from second_db_engine import Session

session = Session()




# Function to run a database query
def run_query(query, db):
    with sqlite3.connect(db) as conn:
        cursor = conn.execute(query)
        result = cursor.fetchall()
        return result

# Define a query map
QUERY_MAP = {
    'blanc_data': 'SELECT ID FROM offers WHERE (price=0 AND brand=0 AND model=0 AND course=0 and capacity=0 and power=0);',
    'low_price': 'SELECT ID FROM offers WHERE price < 10000;',
    'small_course': 'SELECT ID FROM offers WHERE course < 10000;'
}

# Define a database path
dirname = os.path.dirname(__file__)
db_name = 'offers.db'
path_to_db = os.path.join(dirname, db_name)

# Get offers with abnormalities
blank_data = run_query(QUERY_MAP['blanc_data'], path_to_db)
low_price = run_query(QUERY_MAP['low_price'], path_to_db)
small_course = run_query(QUERY_MAP['small_course'], path_to_db)

def update_task(conn, task):
        sql = ''' UPDATE offers
                  SET abnormalities = ?
                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, task)

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def update_omments():
    # database = "offers.db"
    # # create a database connection
    # conn = create_connection(database)
    with conn:
        for element in low_price:
            update_task(conn, element)
        for item in blank_data:
            update_task(conn, item)
        for data in small_course:
            update_task(conn, data)

if __name__ == '__main__':
    update_omments()


# http://www.sqlitetutorial.net/sqlite-python/update/

