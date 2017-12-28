#! /usr/bin/python3

import pymysql,argparse

import readconf
conf=readconf.confread()
address=conf[0]
user=conf[1]
password=conf[2]
database=conf[3]

db = pymysql.connect(address,user,password,database)
cursor = db.cursor()

#drop existing table

cursor.execute('DROP TABLE IF EXISTS WORDLIST')

# create table

sql = "CREATE TABLE WORDLIST ( word CHAR(64), ID INT )"
cursor.execute(sql)
db.close()
