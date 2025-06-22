import sqlite3


def getCurrentWeatherValues():
    conn = sqlite3.connect('/home/darragh/PiStation/weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT Temperature,Humidity,Date FROM Weather ORDER BY id DESC LIMIT 1 ')
        output = cursor.fetchone()

        if output is None:
            conn.close()
            return None, None
        else:
            temperature = output[0]
            humidity = output[1]
            conn.close()
            return temperature, humidity
    except Exception as e:
        print(e)
        conn.close()
        return None, None
