#! /usr/bin/env python3

import sqlite3,base64

def getRows(self,db):
    mRowSql='''select rowid from topartists order by rowid desc limit 1;'''
    db['cursor'].execute(mRowSql)
    mRow=db['cursor'].fetchone()
    if mRow != None:
        mRow=mRow[0]
    else:
        exit("there are no rows!")
    return mRow

def getArtists(self,db,mRow):
    chunks=50
    modulo=mRow%chunks
    segs=int(mRow/chunks)
    counter=0
    print(mRow,segs,modulo,(segs*chunks)+modulo)
    while counter <= mRow:
        sql='''select nameb64 from topartists 
            group by artist order by listeners 
            desc limit {} offset {}'''.format(chunks,counter)
        db['cursor'].execute(sql)
        results=db['cursor'].fetchall()
        if results != None:
            for result in results:
                print(base64.b64decode(result[0].encode()).decode())
        counter+=chunks

