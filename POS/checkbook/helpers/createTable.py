#! /usr/bin/python3

import pymysql,dbtools

import os

nl="\n"
hostname=""
uzer=""
database=""
password=""
table=""

CFG="./checkbook.cfg"
if os.path.exists(CFG) and os.path.isfile(CFG):
 with open(CFG,"r") as cfg:
  for i in cfg:
   if len(i.split("=")) > 1:
    varName=i.split("=")[0]
    varVal=i.split("=")[1]
    if varName == "hostname":
     hostname=varVal.rstrip(nl)
    if varName == "uzer":
     uzer=varVal.rstrip(nl)
    if varName == "database":
     database=varVal.rstrip(nl)
    if varName == "password":
     password=varVal.rstrip(nl)
    if varName == "table":
     table=varVal.rstrip(nl)
else:
    print("configuration file does not exist! quitting!")
    exit()

dbtools.check(hostname,uzer,password,database)

def createTable(hostname,user,password,datebase,sql,table=""):
 #open database connection
 db = pymysql.connect(str(hostname),str(user),str(password),str(datebase))
 # prepare a cursor object using cursor() method
 cursor=db.cursor()
 # drop table if it already exists using exute method
 cursor.execute("DROP TABLE IF EXISTS "+table)
 cursor.execute(sql)
 db.close()


SQL="CREATE TABLE "+table+" ( SUBTOTAL CHAR(10) NOT NULL, TAX CHAR(10), TOTALSALE CHAR(16),STORE CHAR(64), USER CHAR(32), ENTRYDATE char(100) ,DATE char(32),NOTES TEXT)"
print(SQL)
createTable(hostname,uzer,password,database,SQL,table=table)
