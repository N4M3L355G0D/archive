#! /usr/bin/env python3

import sqlite3,base64,os,time
from multiprocessing import Process as process, Queue as queue

def splitfile(file):
    ifile=open(file,'rb')
    count=0
    for i in ifile:
        count+=1
    chunks=4
    chunk_size=(count-(count%chunks))/chunks
    
    chunk1=[0,chunk_size-1]
    chunk2=[chunk_size,(chunk_size*2)-1]
    chunk3=[(chunk_size*2),(chunk_size*3)-1]
    chunk4=[(chunk_size*3),(chunk_size*4)+(count%chunks)-1]

    ifile.close()
    ifile=open(file,"rb")
    newfile=os.path.basename(file)
    filep1=open(newfile+".part1","wb")
    filep2=open(newfile+".part2","wb")
    filep3=open(newfile+".part3","wb")
    filep4=open(newfile+".part4","wb")

    count=0
    for i in ifile:
        if chunk1[0] <= count <= chunk1[1]:
            #print(i.rstrip(b"\n"),count,'chunk1')
            filep1.write(i)
        elif chunk2[0] <= count <= chunk2[1]:
            filep2.write(i)
            #print(i.rstrip(b"\n"),count,'chunk2')
        elif chunk3[0] <= count <= chunk3[1]:
            filep3.write(i)
            #print(i.rstrip(b"\n"),count,'chunk3')
        elif chunk4[0] <= count <= chunk4[1]:
            filep4.write(i)
            #print(i.rstrip(b"\n"),count,'chunk4')
        else:
            print(i.rstrip(b"\n"),count,"out side chunk")
        count+=1

#splitfile('mount/wpa-psk-wordlist-3-final-13gb/Custom-WPA')
def mainworker(dbfile,file,chunk,pathfile,pathdb):
    dbfile=os.path.join(pathdb,dbfile+str(chunk)+".db")
    dicFile=os.path.join(pathfile,file+str(chunk))
    db=sqlite3.connect(dbfile)
    cursor=db.cursor()
    
    sql="drop table if exists words;"
    cursor.execute(sql)
    
    sql="create table if not exists words(word text,id INTEGER PRIMARY KEY AUTOINCREMENT)"
    cursor.execute(sql)
    
    with open(dicFile,'rb') as data:
        counter=0
        for i in data:
            i=i.rstrip(b"\n")
            i=i.rstrip(b"\r")
            counter+=1
            sql=b'insert into words(word) values("'+base64.b64encode(i)+b'");'
            sql=sql.decode()
            string='"chunk:{}"#"cmd:{}"#"line_number:{}"#"word:{}"'.format(chunk,sql,counter,i)
            if (counter % 50000) == 0:
                print(string)
                print("performing intermediate commit: {}".format(dbfile))
                db.commit()
            cursor.execute(sql)
    print("committing changes to '{}'".format(dbfile))
    db.commit()

proc=[]

if __name__ == '__main__':
    for i in range(1,5):
        proc.append(process(target=mainworker,args=('custom-wpa.part','Custom-WPA.part',i,"wordlists","db")).start())

#mainworker(dbfile="custom-wpa.part",file='Custom-WPA.part',chunk=1)
