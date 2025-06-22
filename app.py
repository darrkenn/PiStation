from flask import Flask, render_template
#Files
from DatabaseActions.databaseCheck import *
from DatabaseActions.getAllPastValues import getReadings
from DatabaseActions.getCurrentWeatherValues import getCurrentWeatherValues

db_location = '/home/darragh/PiStation/weather.db'
#Checks if sqlite database is present if not then it adds fills it.
createDb()


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html",)

@app.route('/homepage')
def homepage():
    currentTemp = getCurrentWeatherValues()
    return render_template(
        "homepage.html",
        temp=currentTemp[0],
        humidity=currentTemp[1],
    )

@app.route('/homepage/pastReadings')
def pastReadings():
    Readings = getReadings()
    return render_template(
    "pastReadings.html",
    pastReadings=Readings,
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6789,debug=True)
