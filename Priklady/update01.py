# importing sqlite3 module 
import sqlite3 

# create connection by using object to 
# connect with gfg database 
connection = sqlite3.connect('gfg.db') 

# query to create a table named STUDENT 
connection.execute(''' CREATE TABLE STUDENTS 
		(SID INT PRIMARY KEY	 NOT NULL, 
		SNAME		 TEXT NOT NULL, 
		SAGE		 INT	 NOT NULL, 
		ADDRESS	 CHAR(50)); 
		''') 

# insert query to insert student details 
# in the above table 
connection.execute( 
	"INSERT INTO STUDENTS VALUES (1, 'mohan pavan', 22, 'ponnur' )") 

connection.execute( 
	"INSERT INTO STUDENTS VALUES (2, 'sudheer', 28, 'chebrolu' )") 

connection.execute( 
"INSERT INTO STUDENTS VALUES (3, 'mohan', 22, 'tenali' )") 

# creating cursor object to display all 
# the data in the table 
cursor = connection.execute("SELECT * from STUDENTS") 

# display data 
print('\nOriginal Table:') 
for row in cursor: 
	print(row) 

# update query to update sname to sravan 
# where id = 1 
connection.execute("UPDATE STUDENTS set SNAME = 'sravan' where SID = 1") 

# save the changes 
connection.commit() 

# creating cursor object to display all 
# the data in the table 
cursor = connection.execute("SELECT * from STUDENTS") 

# display data 
print('\nUpdated Table:') 
for row in cursor: 
	print(row) 
