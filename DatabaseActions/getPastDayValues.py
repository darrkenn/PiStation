import datetime
import sqlite3
def getPastDayTemps():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    pureDate = datetime.datetime.now()
    date = pureDate.strftime('%d-%m-%Y')
    try:
        cursor.execute('Select Temperature FROM Weather WHERE Date = ? ORDER BY id DESC', (date,))
        output = cursor.fetchall()
        print(output)
        if output is None:
            conn.close()
            return None
        else:
            conn.close()
            output = list(reversed(output))
            return output
    except Exception as e:
        print(e)
        conn.close()
        return None

getPastDayTemps()