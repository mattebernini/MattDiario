from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from datetime import datetime
import sqlite3

class Pagina:
    def __init__(self, title='', date=None, content='', category=''):
        self.title = title
        self.date = date
        self.content = content
        self.category = category

class ScriviScreen(Screen):
    def __init__(self, **kwargs):
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        super(ScriviScreen, self).__init__(**kwargs)
        self.pagina = Pagina(date=current_datetime)  # Create a Pagina instance with the default date

    def save_pagina(self):
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect('diary.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pagina (title, datetime, content, category)
            VALUES (?, ?, ?, ?)
        ''', (self.pagina.title, current_datetime, self.pagina.content, self.pagina.category))
        conn.commit()
        conn.close()
        # Clear the TextInput fields
        self.ids.title.text = ""  # Clear the title field
        self.ids.content.text = ""  # Clear the content field
        self.ids.category.text = ""  # Clear the category field
        
class LeggiScreen(Screen):
    def __init__(self, **kwargs):
        conn = sqlite3.connect('diary.db')
        cursor = conn.cursor()

        # Retrieve the most recent diary entry from the "pagina" table
        cursor.execute('SELECT * FROM pagina ORDER BY datetime DESC LIMIT 1')
        most_recent_entry = cursor.fetchone()
        conn.close()
        id, title, datetime, content, category = most_recent_entry
        super(LeggiScreen, self).__init__(**kwargs)
        self.pagina = Pagina(title, datetime, content, category)

class MattDiarioApp(App):
    def build(self):
        self.title = 'MattDiario'
        return Builder.load_file('matt_diario.kv')

if __name__ == '__main__':
    MattDiarioApp().run()
