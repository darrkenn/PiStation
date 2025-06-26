from flask import Flask, render_template

from DataFunctions.individualValues import getIndividualTemps, getIndividualHumidity, getIndividualDates, \
    getIndividualTimes
#Files
from DatabaseActions.databaseCheck import *
from DatabaseActions.getAllPastValues import getReadings
from DatabaseActions.getCurrentWeatherValues import getCurrentWeatherValues
from DatabaseActions.getPastDayValues import getPastDayTemps
from DatabaseActions.getPastHourValues import getPastHourTimes, getPastHourTemps, getPastHourHumidity, \
    getPastHourPressure, getPastHourRain

#Checks if sqlite database is present if not then it adds fills it.
createDb()


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html",)

@app.route('/homepage')
def homepage():
    currentWeather = getCurrentWeatherValues()

    pastHourTimes = getPastHourTimes()
    pastHourTemps = getPastHourTemps()
    pastHourHumidity = getPastHourHumidity()
    pastHourPressure = getPastHourPressure()
    pastHourRain = getPastHourRain()
    return render_template(
        "homepage.html",
        temp=currentWeather[0],
        humidity=currentWeather[1],
        time=currentWeather[2],

        pastHourTimes=pastHourTimes,

        pastHourTemps=pastHourTemps,
        pastHourHumidity=pastHourHumidity,
        pastHourPressure=pastHourPressure,
        pastHourRain=pastHourRain
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
