#! /usr/bin/python3

import pymysql, time

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

phoneNumber="test"
orderNumber="test"
user="test"
pin="1234567891test"
date=str(time.ctime())
plan="test"
##not complete yet, this is just for example code
SQL = " INSERT INTO "+table+"(PHONE_NUMBER, ORDER_NUMBER, USER, PLAN, PIN, DATE, BILL_DATE, ACTIVATION) VALUES ("+"'"+phoneNumber+"'"+",'"+orderNumber+"','"+user+"','"+plan+"','"+pin+"','"+date+"')"

print(SQL)

insertEntry(hostname,uzer,password,database,SQL)
