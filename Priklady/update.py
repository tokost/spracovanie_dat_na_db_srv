import sqlite3
conn=sqlite3.connect('testdb.sqlite3')
cur=conn.cursor()
qry="UPDATE EMPLOYEE SET INCOME = INCOME+1000 WHERE INCOME=?"

try:
   # Execute the SQL command
   cur.execute(qry, (1000,))
   # Fetch all the rows in a list of lists.
   conn.commit()
   print ("Records updated")
except Exception as e:
   print ("Error: unable to update data")
conn.close()