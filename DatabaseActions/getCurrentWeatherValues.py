import sqlite3


def getCurrentWeatherValues():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT Temperature,Humidity,Time FROM Weather ORDER BY id DESC LIMIT 1 ')
        output = cursor.fetchone()

        if output is None:
            conn.close()
            return None, None, None
        else:
            temperature = output[0]
            humidity = output[1]
            time = output[2]
            conn.close()
            return temperature, humidity, time
    except Exception as e:
        print(e)
        conn.close()
        return None, None, None
