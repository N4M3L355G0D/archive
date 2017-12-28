#! /usr/bin/env python2
from scapy.all import *
import os

def textConfig(reason=''):
 Dst=''
 conf_txt="conf.txt"
 print 'attempting to use {} due to {}'.format(conf_txt,reason)
 if os.path.exists(conf_txt):
     with open(conf_txt,"r") as conf:
         for i in conf:
             opt=i.split("=")[0]
             arg=i.split("=")[1]
             if opt == "DST":
                 Dst=arg.rstrip("\n")
 return Dst

try:
 import sqlite3
 conf_db="conf.db"
 if os.path.exists(conf_db):
  print 'using {} configuration'.format(conf_db)
  db=sqlite3.connect(conf_db)
  cursor=db.cursor()
  sql="select count(version) as count from conf;"
  cursor.execute(sql) 
  version=cursor.fetchall()[0][0]
  sql="select DST from conf where version="+str(version)+";"
  cursor.execute(sql)
  Dst=cursor.fetchall()[0][0]

  if Dst == None:
      print "that conf does not exist"
      exit
  if Dst == "":
      print "that conf does not seem right"
      exit
 else:
     Dst=textConfig('[conf db does not exist: {}]'.format(conf_db))

except:
 Dst=textConfig("[import of sqlite3 failed]")

payload=' '*(1024*63)
pingr=IP(dst=Dst)/ICMP()/payload

srloop(pingr)
