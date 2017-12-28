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
  for f,l,a,s,i,h,j in results:
   print(f,l,a,s,i,h,j)
 except:
  print("error: cannot fetch data")
 
 db.close()

table="TRACKING"
date="1-4-2017"
SQL = "SELECT * FROM "+str(table)+" WHERE BILL_DATE = '"+str(date)+"'"
readEntry("productlookup.net","store","avalon","cellular",SQL)
