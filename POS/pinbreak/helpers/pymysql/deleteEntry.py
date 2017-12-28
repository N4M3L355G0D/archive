#! /usr/bin/python3

import pymysql

def deleteEntry(hostname,user,password,database,sql):
 db = pymysql.connect(hostname,user,password,database)
 cursor=db.cursor()
 try:
  cursor.execute(sql)
  db.commit()
 except:
  db.rollback()
 db.close()

user=""
table="TRACKING"
SQL = "DELETE FROM "str(TABLE)" WHERE USER = '"+str(user)+"'"
deleteEntry("productlookup.net","store","avalon","testdb",SQL)
