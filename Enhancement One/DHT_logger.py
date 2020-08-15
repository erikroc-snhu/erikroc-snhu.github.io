#!/usr/bin/python3
#
#  DHT_logger.py
#  Capture realtime data from a DHT11 sensor and save it to SQLite db.
#
#  Erik Roccuzzo 7/14/2020
#

# Import Libraries/Modules
import time
import sqlite3
import Adafruit_DHT

# Declare Variables
dbname='sensorsData.db' # SQLite Database
sampleFreq = 60         # Time in seconds

# Function: Get data from DHT11 Sensor
def getDHTdata():	
	
    # Instantiate Sensor + Read values
	DHT11Sensor = Adafruit_DHT.DHT11
	DHTpin = 4 # Signal pin
	hum, temp = Adafruit_DHT.read_retry(DHT11Sensor, DHTpin)
	
	if hum is not None and temp is not None:
		hum = round(hum)
		temp = round(temp, 1)
	return temp, hum

# Function: Log the data collected to db
def logData (temp, hum):
	
	conn=sqlite3.connect(dbname)    # Create DB connection
	curs=conn.cursor()              # Create cursor to work in DB
	
    # Use SQL Statements with cursor to 'execute' statement on the database
    # Here we are 'Insert'ing data into a table called DHT_data the values of 'temp' and 'hum'
    #  collected from the getDHTdata() function, along with a current datetime timestamp.
	curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
	conn.commit()
	conn.close()

# Function: Main
def main():
    # Keep collecting data and sending it to the database as long as we run
	while True:
		temp, hum = getDHTdata()
		logData (temp, hum)
		time.sleep(sampleFreq)

# ------------ Execute program 
main()