#!/usr/bin/python3
#
#
#  DHT11_test.py
#

import Adafruit_DHT                 # Module to initialize and access sensor
import time

DHT11Sensor = Adafruit_DHT.DHT11    # Create an instance of the DHT11 Sensor class
DHTpin = 4                          # Pin which is connected to the signal line
sampleFreq = 2                      # Number of seconds between samples

while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT11Sensor, DHTpin)
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)
        
    time.sleep(sampleFreq)