import sqlite3 

# Connecting to sqlite 
# connection object 
connection_obj = sqlite3.connect('geek1.db') 

# cursor object 
cursor_obj = connection_obj.cursor() 

# to select all column we will use 
statement = '''SELECT * FROM GEEK'''

cursor_obj.execute(statement) 

print("Limited data") 
output = cursor_obj.fetchmany(5) 
for row in output: 
    print(row) 

connection_obj.commit() 

# Close the connection 
connection_obj.close() 
