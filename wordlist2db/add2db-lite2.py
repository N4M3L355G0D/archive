#! /usr/bin/python3

#need to add something that will detect ctrl-c and make this program perfrom a wal_checkpoint
import sqlite3, os, sys, binascii

#create db

conn=sqlite3.connect("wordlist.db")
c=conn.cursor()

sql='PRAGMA journal_mode = WAL'
c.execute(sql)
sql='PRAGMA synchronous = NORMAL'
c.execute(sql)

#check for table

sql="create table if not exists wordlist ( WORD text , ID real)"
c.execute(sql)
#create table

try:
    sql="SELECT ID FROM wordlist ORDER BY ID DESC LIMIT 1"
    c.execute(sql)
    ID=int(c.fetchone()[0])
except:
    ID=0

print("Last Column ID: "+str(ID))
counter=0

if len(sys.argv) >= 3:
    suppress=sys.argv[2]
else:
    suppress="no"

with open(sys.argv[1],"rb") as file:
    for i in file:
        counter+=1
        data=binascii.hexlify(i).decode()
        sql="INSERT INTO wordlist (WORD,ID) SELECT '"+data+"',"+str(ID)+" WHERE NOT EXISTS(SELECT WORD FROM wordlist where WORD='"+data+"');"
        #print(sql)
        c.execute(sql)
        if c.rowcount == 1:
            ID+=1
            print(ID)
            if ( counter % 50000 ) == 0 and counter != 0:
                sql="PRAGMA wal_checkpoint;"
                c.execute(sql)

        else:
            print(data+"[not added]")
        """    
        # this hould only execute when a successful insertion is done
        if ( counter % 50000 ) == 0 and counter != 0:
            sql="PRAGMA wal_checkpoint;"
            c.execute(sql)
        """
        '''
        sql='SELECT WORD FROM wordlist WHERE word="'+data+'"'
        c.execute(sql)
        result=c.fetchone()
        if result == None:
            sql="INSERT INTO wordlist VALUES (\""+data+"\","+str(ID)+")"
            ID+=1
            if suppress == "no":
                print(data+" [added] <= ",binascii.unhexlify(data))
            c.execute(sql)
            conn.commit()
        else:
            if suppress == "no":
                print(data+" [not added]")
        '''
conn.close()

print("values were stored in a ascii hex format so that non- UTF-8 characteds could be stored as well. to use the\n generated DB, you should use something like python's binascii.unhexlify() on the queried string. This seems to be the easiest method of storing wordlists with non-UTF-8 characters that send python3 into spasms!")
print("processed columns from current infile:",counter)
print("total columns in DB:",ID)
