import sqlite3
def getValues():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Temperature,Humidity FROM Weather ORDER BY id DESC LIMIT 1')
    output = list(sum(cursor.fetchall(), ()))
    conn.close()
    return output
