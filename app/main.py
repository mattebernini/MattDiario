import sqlite3
from kivy.app import App
from kivy.lang import Builder
from datetime import datetime
import webbrowser
import requests
import os
from dotenv import load_dotenv

class MattDiario(App):
    def build(self):
        load_dotenv()
        self.title = "MattDiario"
        self.root = Builder.load_file("matt_diario.kv")
        # Initialize the date TextInput with the current date and time
        self.root.ids.date.text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return self.root

    def save_pagina(self):
        title = self.root.ids.title.text
        date = self.root.ids.date.text
        category = self.root.ids.category.text
        content = self.root.ids.content.text

        conn = sqlite3.connect("diary.db")
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pagina
            (id INTEGER PRIMARY KEY, title TEXT, date TEXT, category TEXT, content TEXT, sync BOOLEAN DEFAULT 0)
        ''')

        cursor.execute('INSERT INTO pagina (title, date, category, content) VALUES (?, ?, ?, ?)',
                       (title, date, category, content))

        conn.commit()
        conn.close()
        self.clear()
    
    def clear(self):
        # Clear the TextInput widgets after saving
        self.root.ids.title.text = ''
        self.root.ids.category.text = ''
        self.root.ids.content.text = ''

    def leggi(self):
        url = os.getenv("LEGGI_URL")
        url = "http://localhost:5000"
        webbrowser.open(url)

    def sincronizza(self):
        # Fetch rows with sync=False from the Kivy app's database
        conn = sqlite3.connect("diary.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pagina WHERE sync = 0")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            data = {
                "title": row[1],
                "date": row[2],
                "category": row[3],
                "content": row[4]
            }

            # Send data to the Flask server
            url = os.getenv("SEND_URL")
            url = "http://localhost:5000/api/send"
            response = requests.post(url, json=data)

            if response.status_code == 200:
                print(f"Page '{data['title']}' sent successfully")
                # Update the sync status in the Kivy app's database
                conn = sqlite3.connect("diary.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE pagina SET sync = 1 WHERE id = ?", (row[0],))
                conn.commit()
                conn.close()
            else:
                print(f"Failed to send page '{data['title']}'")

    

if __name__ == '__main__':
    MattDiario().run()
