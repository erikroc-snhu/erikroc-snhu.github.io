## Enhancement One

The first piece of this project was a way to collect real time data from a DHT11 sensor attached to a Raspberry Pi ARM-architecture running a Debian based Linux operating systems called RaspbianOS.

The DHT11 sensor is a very basic and slow temperature and humidity sensor that is a good way to learn basic data logging utilizing a combination of hardware and software.

The sensor is made up of a capacitive humidity sensor and a thermistor with a basic chip inside that does some analog to digital conversion to give a digital signal with the temperature and humidity.

After downloading the appropriate sensor library, the initial script used with this hardware consisted of creating an instance of the DHT11 class that would be used to read and write values over the pin which is connected to the signal line of the Raspberry Pi controller.

Once instantiated, I used a simple try/except in Python to print the temperature and humidity values that were being collected by the sensor, converted by the ADC converter within the chip, and passed along the signal line to the Pi.

The enhancements for this part of the project needed to include a way to automate this process and integrate the information being collected into a database for later recollection and processing which required a couple of functions.

First, I encapsulated what was the while True try/except loop into it’s own function called getDHTdata().
This function is responsible for the initial instantiation of the DHT11 class and collection of the actual humidity and temperature values which are stored in ‘hum’ and ‘temp’ variables respectively.
```markdown
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
  ```

The next function is the logData() function, which accepts 2 parameters as inputs (temp, hum).
This function is responsible for creating the initial database connection, the cursor that is required to execute work on that database, as well as the actual SQL statements that will be inserting the data into the table being used for this database.
```markdown
def logData (temp, hum):
	
	conn=sqlite3.connect(dbname)    # Create DB connection
	curs=conn.cursor()              # Create cursor to work in DB
	
    # Use SQL Statements with cursor to 'execute' statement on the database
    # Here we are 'Insert'ing data into a table called DHT_data the values of 'temp' and 'hum'
    #  collected from the getDHTdata() function, along with a current datetime timestamp.
	curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
	conn.commit()
	conn.close()
  ```

The main function employs the whileTrue loop, and goes on to call the getDHTdata() function – which populates the ‘temp’ and ‘hum’ variables.
These variables are then passed to logData() as parameters, where they are insert into the database table along with a timestamp for the current date and time.
```markdown
# Function: Main
def main():
    # Keep collecting data and sending it to the database as long as we run
	while True:
		temp, hum = getDHTdata()
		logData (temp, hum)
		time.sleep(sampleFreq)
```

The enhancements have been successful and I am able to let this script run as a background task to automatically collect data and insert it into a SQLite database table for later processing.

Link to Enhancement One repo files:
[Link](url) and ![Image](src)
```
