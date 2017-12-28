#! /usr/bin/python3

import pymysql,argparse,os

import readconf
conf=readconf.confread()
address=conf[0]
user=conf[1]
password=conf[2]
database=conf[3]



db = pymysql.connect(address,user,password)
cursor=db.cursor()
cursor.execute("CREATE DATABASE "+database)
data=cursor.fetchone()

print(data)
db.close()
