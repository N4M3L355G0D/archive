#! /usr/bin/python3

import pymysql, time

def createTable(hostname,user,password,datebase,sql,table=""):
 #open database connection
 db = pymysql.connect(str(hostname),str(user),str(password),str(datebase))
 # prepare a cursor object using cursor() method
 cursor=db.cursor()
 # drop table if it already exists using exute method
 cursor.execute("DROP TABLE IF EXISTS "+table)
 cursor.execute(sql)
 db.close()

#table="TRACKING"
#SQL="CREATE TABLE "+table+" ( PHONE_NUMBER CHAR(20) NOT NULL, ORDER_NUMBER CHAR(20), PLAN CHAR(10),USER CHAR(20), PIN CHAR(20), DATE TEXT )"""

#createTable("productlookup.net","store","avalon","cellular",SQL,table=table)

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


