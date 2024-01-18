import sqlite3
conn=sqlite3.connect('testdb.sqlite3')
cur=conn.cursor()
qry="SELECT * FROM EMPLOYEE"

try:
   # Execute the SQL command
   cur.execute(qry)
   # Fetch all the rows in a list of lists.
   results = cur.fetchall()
   for row in results:
      fname = row[1]
      lname = row[2]
      age = row[3]
      sex = row[4]
      income = row[5]
      # Now print fetched result
      print ("fname={},lname={},age={},sex={},income={}".format(fname, lname, age, sex, income ))
except Exception as e:
   print (e)
   print ("Error: unable to fecth data")

conn.close()