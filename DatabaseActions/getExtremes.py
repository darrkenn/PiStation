import datetime
import sqlite3

def getDayExtreme():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    try:
        cursor.execute('SELECT Temperature,Humidity,Air Pressure FROM Weather WHERE Date LIKE ?', (date,))
        preOutput = cursor.fetchall()
        if preOutput is None:
            conn.close()
            return None
        else:
            temps = [temp[0] for temp in preOutput]
            humidities = [humidity[1] for humidity in preOutput]
            pressures = [pressure[2] for pressure in preOutput]

            maxTemp = max(temps)
            maxHumidity = max(humidities)
            maxPressure = max(pressures)
            return maxTemp, maxHumidity, maxPressure, date
    except Exception as e:
        conn.close()
        print(e)

def getHourExtreme():
        conn = sqlite3.connect('/var/lib/PiStation/weather.db')
        cursor = conn.cursor()
        date = datetime.datetime.now().strftime('%d-%m-%Y')
        try:
            cursor.execute('SELECT Temperature,Humidity,Air Pressure FROM Weather ORDER BY id DESC LIMIT 7')
            preOutput = cursor.fetchall()
            if preOutput is None:
                conn.close()
                return None
            else:
                temps = [temp[0] for temp in preOutput]
                humidities = [humidity[1] for humidity in preOutput]
                pressures = [pressure[2] for pressure in preOutput]

                maxTemp = max(temps)
                maxHumidity = max(humidities)
                maxPressure = max(pressures)
                return maxTemp, maxHumidity, maxPressure, date
        except Exception as e:
            conn.close()
            print(e)