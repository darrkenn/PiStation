from flask import Flask, render_template

#Files
from Database_Actions.databaseCheck import *
from Database_Actions.getWeatherValues import getValues

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
        humidity=values[1]
    )

if __name__ == '__main__':
    app.run(debug=True)
