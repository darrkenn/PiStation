import sqlite3


class Reading:
    def __init__(self, temperature, humidity, date, time):
        self.temperature = temperature
        self.humidity = humidity
        self.date = date
        self.time = time
    def __str__(self):
        return "Temperature: {}, Humidity: {}, Date: {}, Time: {}".format(self.temperature, self.humidity, self.date, self.time)
    def to_dict(self):
        return {"temperature": self.temperature, "humidity": self.humidity, "date": self.date, "time": self.time}



def getReadings():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    weatherPastReadings = []
    try:
        cursor.execute("SELECT Temperature, Humidity, Date, Time FROM weather ORDER BY ID DESC")
        output = cursor.fetchall()
        for row in output:
            temperature = row[0]
            humidity = row[1]
            date = row[2]
            time = row[3]
            if temperature is None:
                temperature = "No Value:("
            if humidity is None:
                humidity = "No Value:("
            if date is None:
                date = "No Value:("
            if time is None:
                time = "No Value:("
            weatherPastReadings.append(Reading(temperature, humidity, date, time))
    except Exception as e:
        print(e)
        conn.close()
    conn.close()
    return weatherPastReadings
