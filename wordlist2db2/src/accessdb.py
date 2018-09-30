#! /usr/bin/env python3
import sqlite3,os
from multiprocessing import Process as process
import base64
dbpath="db"

db=[]
db.append(os.path.join(dbpath,"custom-wpa.part1.db"))
db.append(os.path.join(dbpath,"custom-wpa.part2.db"))
db.append(os.path.join(dbpath,"custom-wpa.part3.db"))
db.append(os.path.join(dbpath,"custom-wpa.part4.db"))

term=base64.b64encode(input('word to check: ').encode()).decode()

def main(dbfile,term):
    sql="select word from words where word='"+term+"';"
    db=sqlite3.connect(dbfile)
    cursor=db.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    if result != None:
        for i in result:
            for x in i:
                print('Entry Found in "{}": '.format(dbfile),base64.b64decode(x))
res=[]
for i in db:
    res.append(process(target=main,args=(i,term)).start())
