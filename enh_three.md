### Enhancement Three: Databases

The automatic logging of data to the database is now in place in the DHT_logger.py script from Enhancement One: Software Design/Engineering.
To determine if the sensor data being fed automatically to the DHT_data table in my sensorsData.db SQLite database is good, I’ve written a small python script that includes multiple tests in the form of SQL queries to return some of the information being stored. These tests serve an important purpose to determine the current state of functionality of this feature and to test for any potential bugs that may exist.

Queries are one of the most important aspects when working with Structured Query Language as they allow you to extract specific data from a database, formatting it to your liking.
I’ve included 5 queries as tests to confirm different aspects of the data being stored.

The first query is a simple select all statement which will return all of the data from the database without filtering anything.
```sql
# Select all of the data in the databse
print ("\nAll entries:\n")
for row in curs.execute("SELECT * FROM DHT_data"):
    print (row)
```
The next two utilize specific temperature and humidity values – this allows me to confirm that I am getting multiple (different) readings by storing different values and that those values are able to be structured and filtered to return properly, this is crucial when integrating with the front end GUI.
```sql
# Select data where humidity value = 29   
print ("\nEntries for a humidity value of (29):\n")
for row in curs.execute("SELECT * FROM DHT_data WHERE hum='29'"):
    print (row)

# Select data where temperature value > 30    
print ("\nEntries for temperature above 30*C:\n")
for row in curs.execute("SELECT * FROM DHT_data WHERE temp>30.0"):
    print (row)
```
The next query confirms the functionality of using a variable ‘maxTemp’ as input to a query return specific temperature entries above whatever the input variable is.
This will allow for further development of interaction on the front end where a user can input a specific temperature or humidity value and query all dates and times when that value was read.
```sql
# Select data where temperature > maxTemp variable
print ("\nEntries for temperature is above x:\n")
for row in curs.execute("SELECT * FROM DHT_data WHERE temp>(?)", (maxTemp,)):
    print (row)
```
The last query is an important test that illustrates reading the most recent data entered to the table, this will serve as the basis of information for what the front end is presenting when a user is trying to find out what the current temperature or humidity levels are.
```sql
# Select last data value that was logged to the database
print ("\nLast logged temperature and humidity:\n")
for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
    print (row)
```
One of the crucial factors to take into consideration from a security perspective are SQL injection attacks. As this database will ultimately be the backend to a frontend GUI accepting user input, a major consideration needing to be evaluated is where and how I will scrub user input to prevent any potential bad actors from successfully attacking my database. It could be argued that as a standalone sensor merely reading temperature and humidity data – the data and device itself is not worth putting the effort into protecting, as the information isn’t considered valuable. However, I feel that it is simply good practice to be aware of and implement techniques to mitigate any potential threats and vulnerabilities, especially when something like scrubbing user input can be as simple as a few additional lines of code.

[Enhancement Three Files](https://github.com/erikroc-snhu/erikroc-snhu.github.io/tree/master/Enhancement%20Three)

[Back To Main](index.md)
