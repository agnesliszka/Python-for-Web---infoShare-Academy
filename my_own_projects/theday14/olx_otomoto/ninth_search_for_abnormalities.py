# Standard library imports
import sqlite3

blank_data_ids_updated = []
low_price_ids_updated = []
small_course_ids_updated = []

# Make a connection to the SQLite DB
conn = sqlite3.connect("offers.db")

# Obtain a Cursor object to execute SQL statements
cur = conn.cursor()

# Function to run a database query
def run_query(query):
    cursor = conn.execute(query)
    result = cursor.fetchall()
    return result

# Define a query map
QUERY_MAP = {
    'blank_data': 'SELECT ID FROM offers WHERE (price IS null AND brand IS null AND model IS null AND course IS null AND capacity IS null AND power IS null);',
    'low_price': 'SELECT ID FROM offers WHERE price < 1000;',
    'small_course': 'SELECT ID FROM offers WHERE course < 1000;'
}

# Get offers with abnormalities
blank_data_ids = run_query(QUERY_MAP['blank_data'])
low_price_ids = run_query(QUERY_MAP['low_price'])
small_course_ids = run_query(QUERY_MAP['small_course'])

for element in blank_data_ids:
    element = str(element).replace(",)","")
    element = str(element).replace("(", "")
    element = int(element)
    blank_data_ids_updated.append(element)

for element in low_price_ids:
    element = str(element).replace(",)","")
    element = str(element).replace("(", "")
    element = int(element)
    low_price_ids_updated.append(element)

for element in small_course_ids:
    element = str(element).replace(",)","")
    element = str(element).replace("(", "")
    element = int(element)
    small_course_ids_updated.append(element)

blank_data_text = 'blank data'
low_price_text = 'low price'
small_course_text = 'small course'

# Update comments in appropriate cell of abnormalities column in offers.db when a certain condition is met
for item in blank_data_ids_updated:
    # print(item)
    cur.execute('''UPDATE offers SET abnormalities = ? WHERE id = ?''', (blank_data_text, item))
    conn.commit()

for item in low_price_ids_updated:
    cur.execute('''UPDATE offers SET abnormalities = ? WHERE id = ?''', (low_price_text, item))
    conn.commit()

for item in small_course_ids_updated:
    cur.execute('''UPDATE offers SET abnormalities = ? WHERE id = ?''', (small_course_text, item))
    conn.commit()

# https://stackoverflow.com/questions/22872814/how-do-i-update-values-in-an-sql-database-sqlite-python
# https://stackoverflow.com/questions/2847999/why-the-need-to-commit-explicitly-when-doing-an-update