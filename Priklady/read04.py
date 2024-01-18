import sqlite3 

# Connecting to sqlite 
# connection object 
connection_obj = sqlite3.connect('geek.db') 

# cursor object 
cursor_obj = connection_obj.cursor() 

# to select all column we will use 
statement = '''SELECT * FROM GEEK'''

cursor_obj.execute(statement) 

print("Only one data") 
output = cursor_obj.fetchone() 
print(output) 

connection_obj.commit() 

# Close the connection 
connection_obj.close() 
