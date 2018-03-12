#! /usr/bin/env python3
#NoGuiLinux
import sqlite3,base64,os,gzip

class dataC:
    dataB64=''
    dbName='data.db'
    final={}
    boldGreen='\033[1;32;40m'
    boldRedBlink='\033[1;5;31;40m'
    reset='\033[0;m'
    boldYellow='\033[1;33;40m'
    def writeData(self):
        data=open(self.dbName,'wb')
        data.write(base64.b64decode(gzip.decompress(base64.b64decode(self.dataB64))))
        data.close()
    def connect(self):
        db=sqlite3.connect(self.dbName)
        cursor=db.cursor()
        return {'db':db,'cursor':cursor}
    def getInfo(self):
        DB=self.connect()
        db=DB['db']
        cursor=DB['cursor']
        self.final['homeAddress']=self.getDetail('home',cursor,db,1)[0]
        if self.final['homeAddress'] != None:
            self.final['homeAddress']=self.final['homeAddress'][0]
        self.final['cell']=self.getDetail('cell',cursor,db,1)[0]
        if self.final['cell'] != None:
            self.final['cell']=self.final['cell'][0]
        self.final['city']=self.getDetail('city',cursor,db,1)[0]
        if self.final['city'] != None:
            self.final['city']=self.final['city'][0]
        self.final['occupation']=self.getDetail('occupation',cursor,db,1)[0]
        if self.final['occupation'] != None:
            self.final['occupation']=self.final['occupation'][0]
        db.close()

    def getDetail(self,field,cursor,db,ID):
        sql='select {} from info where id={}'.format(field,ID)
        cursor.execute(sql)
        return cursor.fetchall()
    def printTable(self):
        longest=0
        finalPrint=[]
        for i in self.final.keys():
            printString='{0}{1}{2} : {3}{4}{5}'.format(self.boldGreen,i,self.reset,self.boldRedBlink,self.final[i],self.reset)
            if len(printString) > longest:
                longest=len(printString)
            finalPrint.append(printString)
        sepBar=self.boldYellow+'='*(longest-(len(self.boldGreen)+len(self.boldRedBlink)+(len(self.reset)*2)))+self.reset
        print(sepBar)
        for i in finalPrint:
            print(i)
        print(sepBar)

a=dataC()
a.dataB64=b'''
H4sIAMHPpVoAA+3aTY+bMBAG4Dt/pnwkVXu0AROyC4ohNoZbgK1JYrqRkk1Ifn0hq12pUi+V+iX1
HckzyJhnhLiNEA5LNiozcVSdm97pWp/cCCWE8JBwn2gyxT0n5PsI39NbWOOi5OfCJ/6sORL7fh3c
YhLM+CrRr9gvC2DAgAEDBgwYMGDAgAEDBgwYMGDAgP09jHKiS/VwPdJCZV3ZD6bx2HGaSyovNY2S
pu7TH+5ZxE7zTDCR5VRwsUzGemuK4dBG8kvjyqEt5Evpiue6Z6cqH26VCg9POlywQUhSMtVGbFtH
8lD31dnaFPO+viwDsZdUhkLLkPnrsd73r91z7TomXmTmacGPpSuPtU/tSnX2Y5Qe2sVej01nrT+c
Szd1rCZi9qb4/PL2wKbgOhdzkYmWiS3lYm9SLpdVHJ5YkVMqZbYa70/N02w898DvU1EafPxErCn9
xg8ADBgwYMCAAQMGDBgwYMCAAQMGDBgwYP80RleEl85yLTwS6CHZxTp3jV26nal7eY3D7LpRlUlv
wntcay+52l6yCwcrc4dzW0zj5cw024uW+1Anu+SS7pgqi+FUqqUdh/ND5XZjdbq6Z18rFaf3nvyD
R8i0/txrAgMGDBgwYMCAAQMGDBgwYMCAAQMGDNj/htFLGDBuXv/k/Qb7vGmo2EAAAA==
'''
a.writeData()
a.getInfo()
a.printTable()
