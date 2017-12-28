#! /usr/bin/python3

import pymysql, argparse, os
import dump2html_repeats
import os

nl="\n"
hostname=""
uzer=""
database=""
password=""
table=""
nototals=True

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
 count=0
 totalSales=0
 db = pymysql.connect(str(hostname),str(user),str(password),str(database))
 
 cursor = db.cursor()
 
 VALUE=str(100)
 count=0
 unique=dict()
 try:
  cursor.execute(sql)
  results=cursor.fetchall()
  dump2html_repeats.dump1()
  for a,b,c in results:
   if a != "unknown":
    print(a,b,c,sep=" | ")
    dump2html_repeats.dumper(str(a),str(b),str(c))
    if str(b) not in unique.keys():
     unique[str(b)]=c
    else:
     unique.update({str(b):unique[str(b)]+c})
 except:
  print("error: cannot fetch data")
 print("=========================\n\tStatistics\n")
 for i in unique.keys():
  count=count+unique[i]
 print("Total renewals : ",count)
 dump2html_repeats.twofield("Total renewals",str(count))
 for i in unique.keys():
  planTotals="Plan "+i+" Useage: "+str(unique[i])
  dump2html_repeats.twofield("Plan "+i+" Useage",str(unique[i]))
  print(planTotals)
 if nototals == True:
  for i in unique.keys():
   totalSales=totalSales+(float(i)*float(unique[i]))
  print("Total Sales: ",totalSales)
  dump2html_repeats.twofield("Total Sales",str(totalSales))
 db.close()

parser=argparse.ArgumentParser()
parser.add_argument("-n","--nt",help="no total",action="store_true")
options=parser.parse_args()

if options.nt:
 nototals=False
else:
 nototals=True

SQL="select PHONE_NUMBER, PLAN , count(*) c from "+table+" group by PHONE_NUMBER having c > 1;"
readEntry(hostname,uzer,password,database,SQL)
