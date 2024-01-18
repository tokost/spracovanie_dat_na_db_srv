import sqlite3 

# Connecting to sqlite 
# connection object 
connection_obj = sqlite3.connect('geek1.db') 

# cursor object 
cursor_obj = connection_obj.cursor() 

connection_obj.execute("""CREATE TABLE GEEK( 
Email varchar(255), 
Name varchar(50), 
Score int 
);""") 

connection_obj.execute( 
	"""INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk1@gmail.com","Geek1",25)""") 
connection_obj.execute( 
	"""INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk2@gmail.com","Geek2",15)""") 
connection_obj.execute( 
	"""INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk3@gmail.com","Geek3",36)""") 
connection_obj.execute( 
	"""INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk4@gmail.com","Geek4",27)""") 
connection_obj.execute( 
	"""INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk5@gmail.com","Geek5",40)""") 
connection_obj.execute( 
	"""INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk6@gmail.com","Geek6",36)""") 
connection_obj.execute( 
	"""INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk7@gmail.com","Geek7",27)""") 

connection_obj.commit() 

# Close the connection 
connection_obj.close() 
