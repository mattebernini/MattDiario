import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('diary.db')
cursor = conn.cursor()

# Execute a SELECT query to retrieve data from the "pagina" table
cursor.execute('SELECT * FROM pagina')

# Fetch all the rows as a list of tuples
rows = cursor.fetchall()

# Close the database connection
conn.close()

# Display the retrieved data
for row in rows:
    id, title, datetime, content, category, sync = row
    print(f"ID: {id}")
    print(f"Title: {title}")
    print(f"Datetime: {datetime}")
    print(f"Content: {content}")
    print(f"Category: {category}")
    print(f"sync: {sync}")
    print("-" * 30)
