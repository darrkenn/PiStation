import datetime
import os
import sqlite3
from time import sleep
import board
import adafruit_dht
from databaseCheck import createDb
#DHT22
dhtDevice = adafruit_dht.DHT22(board.D4)

def getTempAndHumidity():
    while True:
        try:
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity
            #Better formatting for time as it was too complex.
            date = datetime.datetime.now().strftime('%d-%m-%Y')
            time = datetime.datetime.now().strftime('%H:%M')
            if humidity is not None and temperature is not None and date is not None and time is not None:
                print("Temperature:", temperature, "Humidity:", humidity)
                database_add(int(temperature), int(humidity), date, time)
                print("successfully added")
                sleep(600)
        except RuntimeError as e:
            print(e)


def database_add(temperature, humidity, date, time):
    conn = sqlite3.connect('/var/lib/PiStation/weather.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Weather VALUES(NULL,?,?,?, ?)', (temperature, humidity, date, time))
    conn.commit()
    conn.close()


createDb()
getTempAndHumidity()
