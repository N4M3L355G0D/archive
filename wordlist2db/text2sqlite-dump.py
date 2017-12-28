#! /usr/bin/python3

#need to add something that will detect ctrl-c and make this program perfrom a wal_checkpoint
import sqlite3, os, sys, binascii

counter=0

if len(sys.argv) >= 3:
    suppress=sys.argv[2]
else:
    suppress="no"
ID=0
source=open("result.sql","w")
source.write("PRAGMA foreign_keys=OFF;\n")
source.write("PRAGMA journal_mode = OFF;\n")
source.write("PRAGMA synchronous = NORMAL;\n")
source.write("BEGIN TRANSACTION;\n")
source.write("CREATE TABLE wordlist ( WORD text, ID real);\n")
with open(sys.argv[1],"rb") as file:
    for i in file:
        counter+=1
        ID=counter
        data=binascii.hexlify(i).decode()
        sql="INSERT INTO wordlist (WORD,ID) SELECT '"+data+"',"+str(ID)+" WHERE NOT EXISTS(SELECT WORD FROM wordlist where WORD='"+data+"');\n"
        source.write(sql)

source.write("COMMIT;\n")
source.close()

print("values were stored in a ascii hex format so that non- UTF-8 characteds could be stored as well. to use the\n generated DB, you should use something like python's binascii.unhexlify() on the queried string. This seems to be the easiest method of storing wordlists with non-UTF-8 characters that send python3 into spasms!")
print("processed entries from current infile:",counter)
print("total Row in DB:",ID)
