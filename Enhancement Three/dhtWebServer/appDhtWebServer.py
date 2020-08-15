#!/usr/bin/python3

from flask import Flask, render_template, request	# Import Flash module
app = Flask(__name__)

import sqlite3 as lite					# Import SQLite module

# function: retrieve data from db
def getData():
    c=lite.connect('../sensorsData.db')			# Create db connection
    cur=c.cursor()					# Initialize cursor

    for row in cur.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
        time = str(row[0])
        temp = row[1]
        hum = row[2]

    c.close()
    return time, temp, hum

# main route
@app.route("/")
def index():
        time, temp, hum = getData()
        templateData = {
                'time': time,
                'temp': temp,
                'hum': hum
                }
        return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)

