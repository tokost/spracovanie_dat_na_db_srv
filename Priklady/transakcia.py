# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > ?"
try:
   # Execute the SQL command
   cursor.execute(sql, (20,))
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()