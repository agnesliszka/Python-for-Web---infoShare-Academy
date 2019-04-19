# Standard library imports
import os
import sqlite3

# Project imports
from second_db_engine import Session

session = Session()

conn = sqlite3.connect('offers.db')

# Function to run a database query
def run_query(query):
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
blank_data = run_query(QUERY_MAP['blanc_data'])
low_price = run_query(QUERY_MAP['low_price'])
small_course = run_query(QUERY_MAP['small_course'])

print(blank_data)
print(low_price)
print(small_course)

# def update_task(conn, task):
#         sql = ''' UPDATE offers
#                   SET abnormalities = ?
#                   WHERE id = ?'''
#         cur = conn.cursor()
#         cur.execute(sql, task)
#
# def update_omments():
#     # database = "offers.db"
#     # # create a database connection
#     # conn = create_connection(database)
#     with conn:
#         for element in low_price:
#             update_task(conn, element)
#         for item in blank_data:
#             update_task(conn, item)
#         for data in small_course:
#             update_task(conn, data)
#
# if __name__ == '__main__':
#     update_omments()
#

# http://www.sqlitetutorial.net/sqlite-python/update/

