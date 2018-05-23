#! /usr/bin/env python3

import os,sys,sqlite3
import argparse
#find xml import code
desDir=sys.argv[1]

#create cmdline class
##get desiredDir to scan -d
##take sql select statement -q
##convert output to xml -x
##convert output to csv (default) -c
##get file mimetype -m
##more options comming soon

class container:
    external=None
    class gather:
        def int2Str(self,size,string):
            return '{}{}'.format(str(size),string)

        def bytes2Eng(self,size):
            if size < 1024:
                return self.int2Str(size,'B')
            elif (1024**1) < size < (1024**2):
                size=int(size/(1024**1))
                return self.int2Str(size,'K')
            elif (1024**2) < size < (1024**3):
                size=int(size/(1024**2))
                return self.int2Size(size,'M')
            elif (1024**3) < size < (1024**4):
                size=int(size/(1024**3))
                return self.int2Size(size,'G')
            elif (1024**4) < size < (1024**5):
                size=int(size/(1024**4))
                return self.int2Size(size,'T')
            elif (1024**5) < size < (1024**6):
                size=int(size/(1024**5))
                return self.int2Size(size,'P')
            elif (1024**6) < size < (1024**7):
                size=int(size/(size**6))
                return self.int2Size(size,'E')
            else:
                return size

        def scanFS(self):
            counter=0
            sys.stdout.flush()
            for root,dir,fnames in os.walk(desDir,topdown=True):
                for fname in fnames:
                    path=os.path.abspath(os.path.realpath(os.path.join(root,fname)))
                    if os.path.exists(path) and os.path.isfile(path):
                        size=os.stat(path).st_size
                        self.master.db.insertEntry(path,size)
                    counter+=1
                    sys.stdout.write(str('\b'*len(str(counter)))+str(counter))
                    if ( counter % 1000 ) == 0:
                        self.master.db.db['db'].commit()
            self.master.db.db['db'].commit()
            print('')

    class dbManager:
        master=None
        dbname='records.db'
        db={}
        tbName='fsScanData'
        def init(self):
            self.dbCon()
            self.mkTable()

        def dbCon(self):
            if os.path.exists(self.dbname):
                os.remove(self.dbname)
            self.db['db']=sqlite3.connect(self.dbname)
            self.db['cursor']=self.db['db'].cursor()

        def insertEntry(self,fname,size):
            sql='''
            insert into {}(fname,byteSize)
            values("{}",{});
            '''.format(self.tbName,fname,size)
            self.db['cursor'].execute(sql)

        def mkTable(self):
            sql='''
            create table if not exists {}(
            fname text,
            byteSize real,
            rowid INTEGER PRIMARY KEY AUTOINCREMENT);
            '''.format(self.tbName)
            self.db['cursor'].execute(sql)
            self.db['db'].commit()
        def cleanup(self):
            self.db['db'].close()
            os.remove(self.dbname)
        
        def queryEntry(self,sqlMod=None):
            if sqlMod != None:
                mod=sqlMod
            else:
                mod=''
            sql='''select * from {}{};'''.format(self.tbName,mod)
            try:
                self.db['cursor'].execute(sql)
                results=self.db['cursor'].fetchall()
                return results
            except OSError as err:
                print(err)
                exit(1)
        def displayQuery(self,results):
            print('fname,sizeInEng,sizeInBytes,rowNum')
            for fname,size,fnum in results:
                print('{0},{1},{2},{3}'.format(fname,self.master.gather.bytes2Eng(int(size)),int(size),fnum))

    class void:
        master=None
    class run:
        master=None
        def run(self):
            self.master.db.init()
            self.master.gather.scanFS()
            results=self.master.db.queryEntry()
            self.master.db.displayQuery(results)
            self.master.db.cleanup()

    def assemble(self):
        self.wa=self.void()
        self.wa.master=None
        
        self.wa.db=self.dbManager()
        self.wa.db.master=self.wa

        self.wa.gather=self.gather()
        self.wa.gather.master=self.wa

        self.wa.run=self.run()
        self.wa.run.master=self.wa

        self.wa.run.run()

if __name__ == '__main__':
    app=container()
    app.assemble()
