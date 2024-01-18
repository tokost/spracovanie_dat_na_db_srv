# sql.py

import sqlite3

# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object
c = conn.cursor()

# create a table named 'users' with columns for id, name, and email
c.execute('''CREATE TABLE users
	(id INTEGER PRIMARY KEY, name TEXT, email TEXT)
''')

# insert five rows of data into the 'users' table
c.execute('''
INSERT INTO users (name, email) VALUES
	('John Doe', 'johndoe@example.com'),
	('Jane Smith', 'janesmith@example.com'),
	('Bob Johnson', 'bobjohnson@example.com'),
	('Emily Davis', 'emilydavis@example.com'),
	('Mike Lee', 'mikelee@example.com');
''')

# commit changes to the database
conn.commit()

# close the database connection
conn.close()