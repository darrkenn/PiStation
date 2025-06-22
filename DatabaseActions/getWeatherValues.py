import sqlite3


def getValues():
    conn = sqlite3.connect('/home/darragh/PiStation/weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT Temperature,Humidity,Date FROM Weather ORDER BY id DESC LIMIT 1 ')
        output = cursor.fetchone()

        if output is None:
            conn.close()
            return None, None, None
        else:
            temperature = output[0]
            humidity = output[1]
            date = output[2]
            conn.close()
            return temperature, humidity, date
    except Exception as e:
        print(e)
        conn.close()
        return None, None
