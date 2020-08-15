#!/usr/bin/python3
#
#  DHT_SQLtests.py
#  Queries to test reading values from the sensorsData database
#   These scripted tests are crucial in confirming that we are
#   getting good data to analyze further.
#
#  Erik Roccuzzo 7/30/2020
#
import sqlite3

conn=sqlite3.connect('sensorsData.db')              # Create database connection
curs=conn.cursor()                                  # Create database cursor
maxTemp = 28.2                                      # Arbitrary temp value for testing

# Select all of the data in the databse
print ("\nAll entries:\n")
for row in curs.execute("SELECT * FROM DHT_data"):
    print (row)
    
# Select data where humidity value = 29   
print ("\nEntries for a humidity value of (29):\n")
for row in curs.execute("SELECT * FROM DHT_data WHERE hum='29'"):
    print (row)

# Select data where temperature value > 30    
print ("\nEntries for temperature above 30*C:\n")
for row in curs.execute("SELECT * FROM DHT_data WHERE temp>30.0"):
    print (row)
    
# Select data where temperature > maxTemp variable
print ("\nEntries for temperature is above x:\n")
for row in curs.execute("SELECT * FROM DHT_data WHERE temp>(?)", (maxTemp,)):
    print (row)
    
# Select last data value that was logged to the database
print ("\nLast logged temperature and humidity:\n")
for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
    print (row)