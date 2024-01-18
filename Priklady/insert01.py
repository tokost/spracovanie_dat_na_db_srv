import sqlite3
conn=sqlite3.connect('testdb.sqlite3')
cur=conn.cursor()
qry="""INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES (?, ?, ?, ?, ?)"""
try:
   cur.execute(qry, ('Makrand', 'Mohan', 21, 'M', 5000))
   conn.commit()
   print ('Record inserted successfully')
except Exception as e:
   conn.rollback()
   print ('error in INSERT operation')
conn.close()