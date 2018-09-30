import os,sqlite3,base64

class sooper:
    limit=20
    directory='/home/carl'
    class void:
        master=None

    def assembler(self):
        self.void.sorter=self.sorting()
        self.void.coloring=self.colors()
        self.void.msgs=self.msgs()

        self.void.sorter.master=self.void
        self.void.sorter.run(self.directory,self.limit)

    class colors:
        red="\033[1;31;40m"
        yellow="\033[1;33;40m"
        green="\033[1;32;40m"
        stop="\033[0;m"

    class msgs:
        results="top '{}' files in '{}'; sizes are in bytes"
        sepChar='='
        def bar(self,string):
            return self.sepChar*len(string)

    class sorting:
        master=None
        db={}
        dbname='sizes.db'

        def createDb(self):
            if os.path.exists(self.dbname):
                os.remove(self.dbname)
            self.db['db']=sqlite3.connect(self.dbname)
            self.db['cursor']=self.db['db'].cursor()
        
        def mkTable(self):
            sql='''create table if not exists fs (file text,size real,rowid INTEGER PRIMARY KEY AUTOINCREMENT);'''
            self.db['cursor'].execute(sql)
            self.db['db'].commit()

        def insertRow(self,fname,size):
            sql='''insert into fs (file,size) values ("{}",{});'''.format(fname,size)
            self.db['cursor'].execute(sql)

        def scan(self,directory):
            self.directory=directory
            if type(directory) != type(bytes()):
                directory=directory.encode()
            counter=0
            for root,dir,fnames in os.walk(directory,topdown=True):
                for fname in fnames:
                    path=os.path.join(root,fname)
                    if os.path.exists(path):
                        lsize=os.stat(path).st_size 
                        self.insertRow(base64.b64encode(path).decode(),lsize)
                        if ( counter % 10000 ) == 0:
                            self.db['db'].commit()
                        counter+=1
                        msg="{}working{} : ".format(self.master.coloring.red,self.master.coloring.stop)
                        MSG=''.join(
                                [msg,
                                self.master.coloring.yellow,
                                str(counter),
                                self.master.coloring.stop,
                                len(msg+self.master.coloring.yellow+str(counter)+
                                self.master.coloring.stop)*"\b"]
                        )
                        print(MSG,end='')
            self.db['db'].commit()

        def getVals(self,limit):
            sql='''select file,size from fs order by size desc limit {};'''.format(limit)
            self.db['cursor'].execute(sql)
            results=self.db['cursor'].fetchall()
            if results != None:
                msg=''.join(
                        [self.master.coloring.green,
                        self.master.msgs.results.format(limit,self.directory),
                        self.master.coloring.stop]
                )
                print(msg)
                print(
                        self.master.coloring.yellow+
                        self.master.msgs.bar(msg)+
                        self.master.coloring.stop
                )
                for fname,size in results:
                    try:
                        print(
                            self.master.coloring.green+
                            base64.b64decode(fname.encode()).decode()+
                            self.master.coloring.stop,
                            self.master.coloring.red+
                            str(int(size))+
                            self.master.coloring.stop
                        )
                    except:
                        print(
                                base64.b64decode(fname.encode()),
                                self.master.coloring.red+
                                str(int(size))+
                                self.master.coloring.stop
                        )
                

        def closeDb(self):
            self.db['db'].commit()
            self.db['db'].close()

        def cleanup(self):
            os.remove(self.dbname)

        def run(self,directory,limit):
            self.createDb()
            self.mkTable()
            self.scan(directory)
            self.getVals(limit)
            self.closeDb()
            self.cleanup()

if __name__ == '__main__':
    a=sooper()
    a.directory='/'
    a.limit=10
    a.assembler()
