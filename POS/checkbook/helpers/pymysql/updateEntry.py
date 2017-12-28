#! /usr/bin/python3

import pymysql

def updateEntry(hostname,user,password,database,sql):
 db = pymysql.connect(hostname,user,password,database)
 cursor = db.cursor()

 try:
  cursor.execute(sql)
  db.commit()
 except:
  db.rollback()
 db.close()

fname="kate"
SQL = "UPDATE EMPLOYEE SET LAST_NAME = 'himer' WHERE FIRST_NAME = '"+str(fname)+"'"
updateEntry("productlookup.net","store","avalon","testdb",SQL)
