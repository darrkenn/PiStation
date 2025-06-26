import sqlite3
def createDb():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,Temperature INTEGER,Humidity INTEGER,Air Pressure INTEGER, Raining TEXT, Date DATE, Time TIME)')
    conn.commit()
    conn.close()
    print('Database Created')