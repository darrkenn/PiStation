import datetime
import sqlite3
import sqlite3


def getPastDayTimes():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    try:
        cursor.execute("SELECT Time FROM Weather WHERE Date LIKE ?", (date,))
        output = cursor.fetchall()
        if output is None:
            conn.close()
            return None
        else:
            conn.close()
            output = [row[0] for row in output]
            for row in output:
                print(row)
            return output
    except Exception as e:
        conn.close()
        return None

def getPastDayTemps():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    try:
        cursor.execute('Select Temperature FROM Weather WHERE Date LIKE ?', (date,))
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

def getPastDayHumidity():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    try:
        cursor.execute('Select Humidity FROM Weather WHERE Date LIKE ?', (date,))
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


def getPastDayPressure():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    try:
        cursor.execute('Select Air Pressure FROM Weather WHERE Date LIKE ?', (date,))
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

def getPastDayRain():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    try:
        cursor.execute('Select Raining FROM Weather WHERE Date LIKE ?', (date,))
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
