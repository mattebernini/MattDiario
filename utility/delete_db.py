import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('app/diary.db')
cursor = conn.cursor()

# Execute a DELETE query to remove all rows from the "pagina" table
cursor.execute('DELETE FROM pagina')

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()

print("All rows in the 'pagina' table have been deleted.")
