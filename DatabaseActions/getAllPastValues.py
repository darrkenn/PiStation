import sqlite3


class Reading:
    def __init__(self, temperature, humidity,pressure,rain, date, time):
        self.temperature = temperature
        self.humidity = humidity
        self.date = date
        self.time = time
        self.pressure = pressure
        self.rain = rain
    def __str__(self):
        return "Temperature: {}, Humidity: {},Air Pressure {}, Time {}, Date: {}, Time: {}".format(self.temperature, self.humidity,self.pressure,self.rain, self.date, self.time)
    def to_dict(self):
        return {"temperature": self.temperature, "humidity": self.humidity, "pressure":self.pressure, "rain":self.rain, "date": self.date, "time": self.time}



def getReadings():
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    weatherPastReadings = []
    try:
        cursor.execute("SELECT Temperature, Humidity,Air Pressure, Raining, Date, Time FROM weather ORDER BY ID DESC")
        output = cursor.fetchall()
        for row in output:
            temperature = row[0]
            humidity = row[1]
            airPressure = row[2]
            rain = row[3]
            date = row[4]
            time = row[5]
            if temperature is None:
                temperature = "No Value:("
            if humidity is None:
                humidity = "No Value:("
            if date is None:
                date = "No Value:("
            if time is None:
                time = "No Value:("
            if airPressure is None:
                airPressure = "No Value:("
            if rain is None:
                rain = "No Value:("

            weatherPastReadings.append(Reading(temperature, humidity, airPressure, rain, date, time))
    except Exception as e:
        print(e)
        conn.close()
    conn.close()
    return weatherPastReadings
