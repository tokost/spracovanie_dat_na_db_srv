import sqlite3      # pridane

# Establish a connection to the database
db = sqlite3.connect('testdb.sqlite3')  # pridane
# Create a cursor object
cursor = db.cursor()                    # pridane


# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > ?"
try:
   # Execute the SQL command
   cursor.execute(sql, (20,))
   # Commit your changes in the database
   db.commit()
   print("Deletion successful")      # pridane
   
except sqlite3.Error as e:      # zmenene
# except:
   # Rollback the transaction in case there is any error
   print("SQLite error:", e)
   db.rollback()

finally:                        # pridane
# Close the cursor and database connection
    if 'cursor' in locals():
        cursor.close()
    
    if 'db' in locals():
        db.close()