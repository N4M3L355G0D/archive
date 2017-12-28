#! /usr/bin/python3

import pymysql,dbtools

import os

nl="\n"
hostname=""
uzer=""
database=""
password=""
table=""

CFG="./pinbreak.cfg"
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


SQL="CREATE TABLE "+table+" ( PHONE_NUMBER CHAR(20) NOT NULL, ORDER_NUMBER CHAR(20), PLAN CHAR(10),USER CHAR(20), PIN CHAR(20), DATE TEXT ,BILL_DATE char(32),ACTIVATION char(10))"
print(SQL)
createTable(hostname,uzer,password,database,SQL,table=table)
