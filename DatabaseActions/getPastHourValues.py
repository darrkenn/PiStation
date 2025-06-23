import sqlite3

def getPastHourTemps():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('Select Temperature FROM Weather ORDER BY id DESC LIMIT 6')
        output = cursor.fetchall()
        if output is None:
            conn.close()
            return None
        else:
            conn.close()
            output = [row[0] for row in output]
            return output
    except Exception as e:
        conn.close()
        return None

def getPastHourTimes():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('Select Time FROM Weather ORDER BY id DESC LIMIT 6')
        output = cursor.fetchall()
        if output is None:
            conn.close()
            return None
        else:
            conn.close()
            output = [row[0] for row in output]
            return output
    except Exception as e:
        conn.close()
        return None