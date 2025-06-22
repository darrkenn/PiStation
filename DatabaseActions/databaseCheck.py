import sqlite3
def createDb():
    conn = sqlite3.connect('/home/darragh/PiStation/weather.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,Temperature INTEGER,Humidity INTEGER, Date DATE, Time TIME)')
    conn.commit()
    conn.close()
