import sqlite3

conn = sqlite3.connect('diary.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagina (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        datetime TEXT,
        content TEXT,
        category TEXT
    )
''')
conn.commit()
conn.close()