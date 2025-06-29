import sqlite3


def getCurrentWeatherValues():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT Temperature,Humidity,Air Pressure,Raining, Time FROM Weather ORDER BY id DESC LIMIT 1 ')
        output = cursor.fetchone()

        if output is None:
            conn.close()
            return None, None, None
        else:
            temperature = output[0]
            humidity = output[1]
            pressure = output[2]
            raining = output[3]
            time = output[4]
            conn.close()
            return temperature, humidity,pressure,raining, time
    except Exception as e:
        print(e)
        conn.close()
        return None, None, None, None, None
