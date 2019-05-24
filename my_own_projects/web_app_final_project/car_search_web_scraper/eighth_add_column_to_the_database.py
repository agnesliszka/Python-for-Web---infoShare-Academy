# Standard library imports
import sqlite3

# Make a connection to the SQLite DB
dbCon = sqlite3.connect("offers.db")

# Obtain a Cursor object to execute SQL statements
cur = dbCon.cursor()

# Add a new column to student table
addColumn = "ALTER TABLE offers ADD COLUMN abnormalities VARCHAR DEFAULT '' "
cur.execute(addColumn)

# Close the database connection
dbCon.close()

