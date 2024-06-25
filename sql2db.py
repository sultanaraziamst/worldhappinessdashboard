import sqlite3

# Path to your SQL file
sql_file_path = '2019.sql'
# Path to your SQLite database file (this will be created or overwritten)
db_file_path = 'world_happiness.db'

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Read the SQL file
with open(sql_file_path, 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script against the SQLite database
cursor.executescript(sql_script)

# Commit changes and close the connection
conn.commit()
conn.close()

print("SQL script executed and database created/updated successfully.")