import datetime
import os
import sqlite3
from time import sleep
import requests

from databaseCheck import createDb

headers = {'Accept': 'application/json'}

def retrieveWeather():
    try:
        print('Retrieving Weather Data')
        response = requests.get('http://192.168.1.248/', timeout=10, headers=headers)
        if response.status_code == 200:
            try:
                json_data = response.json()
                return json_data
            except ValueError as e:
                print(e)
                return None
        else:
            print(response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None



def getWeatherData():
    while True:
        try:
            weather = retrieveWeather()
            if weather is not None:
                print("Response is valid")
                temperature = weather['temperature']
                humidity = weather['humidity']
                airPressure = weather['airPressure']
                rain = weather['rain']
                dateTime = datetime.datetime.now()
                date = dateTime.strftime('%d-%m-%Y')
                time = dateTime.strftime('%H:%M')
                fixed_time = time[:-1] + "0"

                if temperature is not None and humidity is not None:
                    database_add(temperature, humidity, airPressure, rain, date, fixed_time)
                    print("successfully added")
                    sleep(600)
            else:
                print('Weather data is bad')

        except RuntimeError as e:
            print(e)


def database_add(temperature, humidity,airPressure,rain, date, time):
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Weather VALUES(NULL,?,?,?,?,?,?)', (temperature, humidity, airPressure, rain, date, time))
    conn.commit()
    conn.close()

if not os.path.exists('/var/lib/PiStation/weather.db'):
    createDb()

print("Started!!")
getWeatherData()