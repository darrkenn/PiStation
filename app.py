from flask import Flask, render_template
#Files
from DatabaseActions.databaseCheck import *
from DatabaseActions.getWeatherValues import getValues

db_location = '/home/darragh/PiStation/weather.db'
#Checks if sqlite database is present if not then it adds fills it.
createDb()


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html",)

@app.route('/homepage')
def homepage():
    values = getValues()
    return render_template(
        "homepage.html",
        temp=values[0],
        humidity=values[1],
        date=values[2]
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
