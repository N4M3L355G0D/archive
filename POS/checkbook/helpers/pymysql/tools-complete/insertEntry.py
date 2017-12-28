#! /usr/bin/python3

import pymysql, time

def insertEntry(hostname,user,password,database,sql):
 #open datebase connection
 db = pymysql.connect(hostname,user,password,database)
 cursor = db.cursor()

 try:
  cursor.execute(sql)
  db.commit()
 except:
  #roll back in case of error
  db.rollback()
 db.close()


table="TRACKING"
phoneNumber="8045921431"
orderNumber="67215"
user="carl"
pin="12345678912345"
date=str(time.ctime())
plan="39.95"
SQL = " INSERT INTO "+table+"(PHONE_NUMBER, ORDER_NUMBER, USER, PLAN, PIN, DATE) VALUES ("+"'"+phoneNumber+"'"+",'"+orderNumber+"','"+user+"','"+plan+"','"+pin+"','"+date+"')"

print(SQL)

insertEntry("productlookup.net","store","avalon","cellular",SQL)
