#! /usr/bin/python3

import pymysql

def readEntry(hostname,user,password,database,sql):
 db = pymysql.connect(str(hostname),str(user),str(password),str(database))
 
 cursor = db.cursor()
 
 VALUE=str(100)
 
 #sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '"+VALUE+"'"
  
 try:
  cursor.execute(sql)
  results=cursor.fetchall()
  for f,l,a,s,i in results:
   print(f,l,a,s,i)
 except:
  print("error: cannot fetch data")
 
 db.close()

SQL = "SELECT * FROM EMPLOYEE WHERE FIRST_NAME = 'carl'"
readEntry("productlookup.net","store","avalon","testdb",SQL)
