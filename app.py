from flask import Flask, render_template

from DataFunctions.individualValues import getIndividualTemps, getIndividualHumidity, getIndividualDates, \
    getIndividualTimes
#Files
from DatabaseActions.databaseCheck import *
from DatabaseActions.getAllPastValues import getReadings
from DatabaseActions.getCurrentWeatherValues import getCurrentWeatherValues
from DatabaseActions.getPastHourValues import getPastHourTemps, getPastHourTimes

db_location = '/home/darragh/PiStation/weather.db'
#Checks if sqlite database is present if not then it adds fills it.
createDb()


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html",)

@app.route('/homepage')
def homepage():
    currentWeather = getCurrentWeatherValues()
    pastHourTemps = getPastHourTemps()
    pastHourTimes = getPastHourTimes()
    return render_template(
        "homepage.html",
        temp=currentWeather[0],
        humidity=currentWeather[1],
        time=currentWeather[2],

        pastHourTimes=pastHourTimes,
        pastHourTemps=pastHourTemps,

    )

@app.route('/homepage/pastReadings')
def pastReadings():
    Readings = getReadings()
    filteredTemp = getIndividualTemps(Readings)
    filteredHumidity = getIndividualHumidity(Readings)
    filteredDates = getIndividualDates(Readings)
    filteredTimes = getIndividualTimes(Readings)
    return render_template(
    "pastReadings.html",
        pastReadings=Readings,

        filteredTemp=filteredTemp,
        filteredHumidity=filteredHumidity,
        filteredDates=filteredDates,
        filteredTimes=filteredTimes,
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6789,debug=True)
