import sqlite3

conn=sqlite3.connect('testdb.sqlite3')
cur=conn.cursor()
qry="""INSERT INTO EMPLOYEE(FIRST_NAME,     # SQL pr=ikaz
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   cur.execute(qry)
   conn.commit()
   print ('Record inserted successfully')
except:
   conn.rollback()
print ('error in INSERT operation')
conn.close()