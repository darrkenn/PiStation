import sqlite3
def createDb():
    conn = sqlite3.connect('../weather.db')
    conn.execute('CREATE TABLE IF NOT EXISTS Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,Temperature INTEGER,Humidity INTEGER)')
