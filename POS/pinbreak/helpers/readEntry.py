#! /usr/bin/python3

import pymysql, argparse, os

import os, dump2html

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


def readEntry(hostname,user,password,database,sql,export):
 db = pymysql.connect(str(hostname),str(user),str(password),str(database))
 
 cursor = db.cursor()
 
 VALUE=str(100)
 
 #sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '"+VALUE+"'"
  
 try:
  cursor.execute(sql)
  results=cursor.fetchall()
  
  if export == True:
   dump2html.dump1()
  for f,l,a,s,i,h,j,k in results:
   if export == True:
    dump2html.dumper(f,l,a,s,i,h,j,str(k))
   print(f,l,a,s,i,h,j,k,sep=" | ")
 except:
  print("error: cannot fetch data")
 
 db.close()


parser=argparse.ArgumentParser()
parser.add_argument("-t","--table",help="table to search")
parser.add_argument("-f","--field",help="field to search")
parser.add_argument("-v","--value",help="value to search field")
parser.add_argument("-e","--export",action="store_true")
options=parser.parse_args()

value="*"
field="BILL_DATE"

if options.table:
    table=str(options.table)
if options.field:
    field=str(options.field)
if options.value:
    value=str(options.value)
SQL = "SELECT * FROM "+str(table)+" WHERE "+str(field)+" = '"+str(value)+"'"
readEntry(hostname,uzer,password,database,SQL,options.export)
