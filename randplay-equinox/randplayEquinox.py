#! /usr/bin/env python3

import os,sqlite3,random,base64,time,hashlib
import subprocess as sp

class Hyperion:
    dir=None
    cmd=None
    dbname=None
    class void:
        master=None
        listExists=True

    def assembler(self):
        self.wa=self.void()
        self.wa.dir=self.dir
        self.wa.cmd=self.cmd
        self.wa.dbname=self.dbname
        while self.wa.listExists == True:
            self.wa.listExists=False
            self.wa.colors=self.colors()

            self.wa.dbManager=self.dbManager()
            self.wa.dbManager.master=self.wa
            self.wa.dbManager.dbname=self.dbname
            print('initializing',end='')
            self.wa.dbManager.dbCreate()
            print('.',end='')
            self.wa.dbManager.mkTableNameRand()
            print('.',end='')
            self.wa.dbManager.mkTable()
            print('.')
            if self.wa.listExists == False: 
                print('scanning')
                self.wa.scan=self.scan()
                self.wa.scan.master=self.wa
                self.wa.scan.scan()
                print('generating random list')
                self.wa.results=self.results()
                self.wa.results.master=self.wa
                self.wa.results.run()
            self.wa.warn=self.warn()
            self.wa.warn.master=self.wa
            self.wa.warn.logic()
        self.wa.getEntries=self.getEntries()
        self.wa.getEntries.master=self.wa
        self.wa.getEntries.readEntry()
        self.wa.dbManager.closeDb()

    class warn:
        master=None
        def logic(self):
            results=self.master.dbManager.getTableCount()
            rows=self.master.dbManager.getMaxRows()
            if rows != None:
                rows=rows[0]
            else:
                exit(str(rows))

            if results != None:
                results=results[0]
            else:
                exit(str(rows))
            if results >= rows**rows:
                print("you have maxed out the number of combinations you can have in the current db, re-initializing db!")
                os.remove(self.master.dbManager.dbname)
                self.master.listExists=True

    class colors:
        red='\033[1;31;40m'
        green='\033[1;31;40m'
        yellow='\033[1;31;40m'
        stop='\033[0;m'
    
    class dbManager:
        master=None
        dbname=None
        def hashed(self,idata):
            sha=hashlib.sha512()
            sha.update(idata)
            return sha.hexdigest()

        def randomTableName(self):
            date=time.ctime().encode()
            randomBytes=os.urandom(32)
            total=date+randomBytes
            return 'l'+self.hashed(base64.b64encode(total))

        def dbCreate(self):
            db={}
            db['db']=sqlite3.connect(self.dbname)
            db['cursor']=db['db'].cursor()
            self.db=db
        
        def mkTableNameRand(self):
            self.tbName=self.randomTableName()
        def mkTableNameHash(self,idata):
            self.tbName='SHA512_'+self.hashed(idata)

        def mkTable(self):
            try:
                sql='''
                create table {}(fname text,rowid INTEGER PRIMARY KEY AUTOINCREMENT);
                '''.format(self.tbName)
                self.db['cursor'].execute(sql)
                self.db['db'].commit()
            except:
                self.master.ListExists=True
            
        def insertEntry(self,entry):
            sql='''
            insert into {} (fname) values ("{}");
            '''.format(self.tbName,base64.b64encode(entry).decode())
            self.db['cursor'].execute(sql)

        def getMaxRows(self):
            sql='''
            select count(rowid) as count from {};
            '''.format(self.tbName)
            self.db['cursor'].execute(sql)
            result=self.db['cursor'].fetchone()
            return result

        def getEntry(self,num):
            sql='''
            select fname from {} where rowid={};
            '''.format(self.tbName,num)
            self.db['cursor'].execute(sql)
            result=self.db['cursor'].fetchone()
            return result
        
        def deleteTable(self):
            sql='''drop table {};'''.format(self.tbName)
            self.db['cursor'].execute(sql)
            self.db['db'].commit()

        def getTableCount(self):
            sql='''select count(name) as count from sqlite_sequence ;'''
            self.db['cursor'].execute(sql)
            result=self.db['cursor'].fetchone()
            return result

        def closeDb(self):
            self.db['db'].commit()
            self.db['db'].close()

    class results:
        master=None
        rlist=[]
        playList=[]
        stgMsg='stage {}'
        def run(self):
            print(self.stgMsg.format(0))
            self.generateRandomList()
            print(self.stgMsg.format(1))
            self.mkRandomList()
            print(self.stgMsg.format(2))
            self.master.dbManager.deleteTable()
            print(self.stgMsg.format(3))
            self.mkNewEntry()
            print(self.stgMsg.format(4))

        def generateRandomList(self):
            rows=self.master.dbManager.getMaxRows()
            if rows != None:
                while True:
                    rnum=random.randint(1,rows[0])
                    if rnum not in self.rlist:
                        self.rlist.append(rnum)
                    if len(self.rlist) >= rows[0]:
                        break
        def mkRandomList(self):
            for num in self.rlist:
                entry=self.master.dbManager.getEntry(num)
                if entry != None:
                    self.playList.append(base64.b64decode(entry[0].encode()).decode())
            print(len(self.playList))

        def mkNewEntry(self):
            musicString=''.join(self.playList).encode()
            self.master.dbManager.mkTableNameHash(musicString)
            self.master.dbManager.mkTable()
            for entry in self.playList:
                self.master.dbManager.insertEntry(entry.encode())

    class getEntries:
        master=None
        def readEntry(self):
            rows=self.master.dbManager.getMaxRows()
            if rows != None:
                rows=rows[0]
                for num in range(1,rows+1):
                    entry=self.master.dbManager.getEntry(num)
                    if entry != None:
                        entry=base64.b64decode(entry[0].encode())
                        self.runCmd(entry)
                        print(entry)
            else:
                print(rows)

        def runCmd(self,entry):
            cmd=self.master.cmd
            #do a custom cmd for each entry
            exe=sp.Popen(cmd+b'"'+entry+b'"',shell=True,stdout=sp.PIPE)
            stdout,stderr=exe.communicate()
            print(stdout)


    class scan:
        master=None
        def scan(self):
            for root,dir,fnames in os.walk(self.master.dir,topdown=True):
                for fname in fnames:
                    path=os.path.join(root,fname)
                    if os.path.isfile(path):
                        self.master.dbManager.insertEntry(path)


if __name__ == "__main__":
    h=Hyperion()
    h.dir='/home/carl/Downloads/torrents'.encode()
    h.cmd=b"vlc --play-and-exit "
    h.dbname="list.db"
    h.assembler()
