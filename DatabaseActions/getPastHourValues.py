import sqlite3

def getPastHourTimes():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('Select Time FROM Weather ORDER BY id DESC LIMIT 7')
        output = cursor.fetchall()
        if output is None:
            conn.close()
            return None
        else:
            conn.close()
            output = [row[0] for row in output]
            output = list(reversed(output))
            return output
    except Exception as e:
        conn.close()
        return None




def getPastHourTemps():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('Select Temperature FROM Weather ORDER BY id DESC LIMIT 7')
        output = cursor.fetchall()
        if output is None:
            conn.close()
            return None
        else:
            conn.close()
            output = [row[0] for row in output]
            output = list(reversed(output))
            return output
    except Exception as e:
        conn.close()
        return None

def getPastHourHumidity():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('Select Humidity FROM Weather ORDER BY id DESC LIMIT 7')
        output = cursor.fetchall()
        if output is None:
            conn.close()
            return None
        else:
            conn.close()
            output = [row[0] for row in output]
            output = list(reversed(output))
            return output
    except Exception as e:
        conn.close()
        return None


def getPastHourPressure():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('Select Air Pressure FROM Weather ORDER BY id DESC LIMIT 7')
        output = cursor.fetchall()
        if output is None:
            conn.close()
            return None
        else:
            conn.close()
            output = [row[0] for row in output]
            output = list(reversed(output))
            return output
    except Exception as e:
        conn.close()
        return None

def getPastHourRain():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    try:
        cursor.execute('Select Raining FROM Weather ORDER BY id DESC LIMIT 7')
        preOutput = cursor.fetchall()
        if preOutput is None:
            conn.close()
            return None
        else:
            conn.close()
            output = []
            preOutput = [row[0] for row in preOutput]
            print(preOutput)
            for reading in preOutput:
                if reading == "Not raining":
                    output.append(0)
                if reading == "It's raining":
                    output.append(1)
        output = list(reversed(output))
        return output
    except Exception as e:
        conn.close()
        return None