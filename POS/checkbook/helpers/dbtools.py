#! /usr/bin/python3

import pymysql

def serverDetect(host,user,passwd):
 msg="could not get data\n[REASON]\n"
 try:
  db=pymysql.connect(str(host),str(user),str(passwd))
  cursor = db.cursor()
  sql="select version()"
  cursor.execute(sql)
  a=cursor.fetchone()
  print(a)
  success=True
 except pymysql.InterfaceError as error:
     print(msg,error)
     success=False
 except pymysql.DataError as error:
     print(msg,error)
     success=False
 except pymysql.DatabaseError as error:
     print(msg,error)
     success=False
 except pymysql.OperationalError as error:
     print(msg,error)
     success=False
 except pymysql.IntegrityError as error:
     print(msg,error)
     success=False
 except pymysql.InternalError as error:
     print(msg,error)
     success=False
 except pymysql.ProgrammingError as error:
     print(msg,error)
     success=False
 except pymysql.NotSupportedError as error:
     print(msg,error)
     success=False
 return success


def createDB(host,user,passwd,DB):
 db = pymysql.connect(str(host),str(user),str(passwd))
 cursor = db.cursor()
 sql = "create database "+str(DB)
 cursor.execute(sql)
 db.close()


def deleteDB(host,user,passwd,DB):
 db = pymysql.connect(str(host),str(user),str(passwd))
 cursor = db.cursor()
 sql = 'drop database '+str(DB)
 a=cursor.execute(sql)
 db.close()
 return a

def checkDB(host,user,passwd,DB):
 db = pymysql.connect(str(host),str(user),str(passwd))
 cursor=db.cursor()
 dbName="'"+str(DB)+"' "
 sql="show schemas like "+dbName
 a=cursor.execute(sql)
 db.close()
 return a

def check(host,user,passwd,DB):
 result=serverDetect(str(host),str(user),str(passwd))
 if result == True:
  verify=checkDB(str(host),str(user),str(passwd),str(DB))
  if verify == 0:
   createDB(str(host),str(user),str(passwd),str(DB))
   success=True
  else:
   print("DB Create FAIL - server db value was", verify)
   success=False
  return success
 else:
  print("there was an error")
#check("127.0.0.1","store","avalon","jek")
#serverDetect("128.0.0.1","store","avalon")
