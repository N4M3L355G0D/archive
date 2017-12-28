#! /usr/bin/python3

import pymysql, argparse, os,sys

import os

nl="\n"
hostname=""
uzer=""
database=""
password=""
table=""


#allow script to be run standalone, for debugging changes
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


def readEntry(hostname,user,password,database,sql):
 try:
  db = pymysql.connect(str(hostname),str(user),str(password),str(database))
  
  cursor = db.cursor()
  
  VALUE=str(100)
  
  #sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '"+VALUE+"'"
  alist=list()
  blist=list()
 
  try:
   cursor.execute(sql)
   results=cursor.fetchall()
   try:
    for a,b,c,d,e,f,g,h in results:
     print(a,b,c,d,e,f,g,h,sep=" | ")
     alist=[a,b,c,d,e,f,g,h]
     return True
   except:
     return False
  except:
   print("error: cannot fetch data")
 
  db.close()
 except:
  os.system("python ./fail.py -t NoServer -m 'No Server to connect to! Exit Now!'")
  print(sys.exc_info())
  return False
#check values
'''
phoneNumber="8043841324"
orderNumber="63447409"
user="carl"
plan="39.95"
pin="16725897422259"
bill_date="1-20-2017"
activation="0"

phoneNumber=""
orderNumber=""
user=""
plan=""
pin=""
bill_date=""
activation=""


SQL = "SELECT * FROM "+str(table)+" WHERE ( PHONE_NUMBER = '"+str(phoneNumber)+"' and ORDER_NUMBER ='"+orderNumber+"' and "+"USER = '"+str(user)+"' and "+"PLAN = '"+str(plan)+"' and PIN = '"+str(pin)+"' and BILL_DATE = '"+str(bill_date)+"' and ACTIVATION = '"+str(activation)+"');"
#assist with troubleshooting
print(SQL)

readEntry(hostname,uzer,password,database,SQL)'''
