import datetime
import os
import sqlite3
from time import sleep
import requests

from databaseCheck import createDb

headers = {'Accept': 'application/json'}
def retrieveWeather():
    while True:
        try:
            print('Retrieving Weather Data')
            response = requests.get('http://192.168.1.248/', timeout=5, headers=headers)
            print('Weather Data Retrieved')
            if response.status_code == 200:
                return response.json()
            else:

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
                date = datetime.datetime.now().strftime('%d-%m-%Y')
                time = datetime.datetime.now().strftime('%H:%M')
                if temperature is not None and humidity is not None:
                    database_add(temperature, humidity, airPressure, rain, date, time)
                    print("successfully added")
                    sleep(600)
            else:
                print('Weather data is bad')

        except RuntimeError as e:
            print(e)


def database_add(temperature, humidity,airPressure,rain, date, time):
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Weather VALUES(NULL,?,?,?, ?)', (temperature, humidity, airPressure, rain, date, time))
    conn.commit()
    conn.close()

if not os.path.exists('/var/lib/PiStation/weather.db'):
    createDb()

print("Started!!")
getWeatherData()