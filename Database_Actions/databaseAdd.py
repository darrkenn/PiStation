import sqlite3
from random import randint
from time import sleep
def database_add():
    humidity = randint(30, 50)
    temperature = randint(10, 30)
    conn = sqlite3.connect('../weather.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Weather VALUES(NULL,?,?)', (temperature, humidity))
    conn.commit()
    conn.close()

while True:
    try:
        database_add()
    except Exception as e:
        print(e)
        pass
    sleep(600)
