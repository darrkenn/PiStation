import datetime
import os
import sqlite3
from time import sleep
import requests

from databaseCheck import createDb


def retrieveWeather():
    while True:
        try:
            print('Retrieving Weather Data')
            response = requests.get('http://192.168.1.248', timeout=300)
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
            print('Retrieving Weather Data')
            response = retrieveWeather()
            if response is not None:
                print('Weather Data Retrieved')
                temperature = response['temperature']
                humidity = response['humidity']
                date = datetime.datetime.now().strftime('%d-%m-%Y')
                time = datetime.datetime.now().strftime('%H:%M')
                if temperature is not None and humidity is not None:
                    database_add(int(temperature), int(humidity), date, time)
                    print("successfully added")
                    sleep(600)
            else:
                print('Failed to retrieve Weather Data')

        except RuntimeError as e:
            print(e)


def database_add(temperature, humidity, date, time):
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Weather VALUES(NULL,?,?,?, ?)', (temperature, humidity, date, time))
    conn.commit()
    conn.close()

if not os.path.exists('/var/lib/PiStation/weather.db'):
    createDb()

getWeatherData()