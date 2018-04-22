#! /usr/bin/env python3
#NoGuiLinux
#grab top artists from last fm from a country
import urllib.request as urlRequest
import sqlite3,os,sys,json,string,time

class container:
    skipRemoveOld=None
    class data:
        master=None
        apikey=''
        country=''
        badchar=string.punctuation

        def getData(self,page,apikey,country):
            url='http://ws.audioscrobbler.com/2.0/?method={}&api_key={}&country={}&format=json&page={}'.format('geo.gettopartists',apikey,country,page)
            data=urlRequest.urlopen(url)
            data=json.loads(data.read().decode())
            return data

        def getTotalPages(self):
            data=self.getData(1,self.apikey,self.country)
            pageAttr=data['topartists']['@attr']
            totalPages=pageAttr['totalPages']
            return totalPages

        def cleanupArtist(self,artist):
            for char in self.badchar:
                if char in artist:
                    artist=artist.replace(char,'0x'+str(ord(char)))
            return artist
        
        def extractData(self,totalPages,db,apikey,country):
            colors=self.master.colors
            counter=1
            for i in range(1,int(totalPages)+1):
                data=self.getData(i,apikey,country)
                artist=data['topartists']['artist']
                if len(artist) > 0:
                    for art in artist:
                        artName=self.cleanupArtist(art['name'])
                        sql='''insert into topartists ( artist,country,listeners) values ("{}","{}",{}) 
                        '''.format(artName,country,art['listeners'])
                        msg='''totalPages: {}{}{} page: {}{}{} artistNumber: {}{}{} artist: "{}{}{}" country: "{}{}{}" listeners: "{}{}{}"'''.format(
                                colors.red,totalPages,colors.stop,
                                colors.green,i,colors.stop,
                                colors.yellow,counter,colors.stop,
                                colors.blue,artName,colors.stop,
                                colors.lightBlue,country,colors.stop,
                                colors.cyan,art['listeners'],colors.stop
                            )
                        print(msg)
                        db['cursor'].execute(sql)
                        counter+=1
                else:
                    print("{}No more results{}".format(colors.red,colors.stop))
                    break
                db['db'].commit()

    class dbManager:
        master=None
        dbName=''
        skipRemoveOld=False
        def newDb(self,dbName):
            if self.skipRemoveOld == False:
                if os.path.exists(dbName) and os.path.isfile(dbName):
                    os.remove(dbName)

        def mkDb(self,dbName):
            db={}
            db['db']=sqlite3.connect(dbName)
            db['cursor']=db['db'].cursor()
            return db

        def mkTable(self,db):
            sqlMkTbl='''create table if not exists topartists ( artist text, country text, listeners real, rowid INTEGER PRIMARY KEY AUTOINCREMENT);'''
            db['cursor'].execute(sqlMkTbl)
            db['db'].commit()

        def cleanupDb(self,db):
            db['db'].commit()
            db['db'].close()

    class colors:
        master=None
        green='\033[1;32;40m'
        red='\033[1;31;40m'
        yellow='\033[1;33;40m'
        stop='\033[0;m'
        lightBlue='\033[1;36;40m'
        cyan='\033[1;35;40m'
        blue='\033[1;34;40m'

    class void:
        master=None

    class tasks:
        master=None
        def run(self):
            dbName=self.master.db.dbName
            self.master.db.newDb(dbName)
            db=self.master.db.mkDb(dbName)
            self.master.db.mkTable(db)
            totalPages=self.master.data.getTotalPages()
            self.master.data.extractData(totalPages,db,self.master.data.apikey,self.master.data.country)
            self.master.db.cleanupDb(db)

    def assembler(self):
        wa=self.void()
        wa.master=wa

        wa.data=self.data()
        wa.data.master=wa
        wa.data.country=self.country
        wa.data.apikey=self.apikey

        wa.db=self.dbManager()
        wa.db.master=wa
        wa.db.dbName='topartists.db'
        wa.db.skipRemoveOld=self.skipRemoveOld

        wa.colors=self.colors()

        wa.run=self.tasks()
        wa.run.master=wa
        wa.run.run()

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        c=container()
        c.apikey=sys.argv[1]
        c.country=sys.argv[2]
        if len(sys.argv) >= 4:
            if sys.argv[3] == 'y':
                c.skipRemoveOld=True
            elif sys.argv[3] == 'n':
                c.skipRemoveOld=False
            else:
                c.skipRemoveOld=True
        c.assembler()
    else:
        exit("missing apikey/country... do you have one for LastFM {} [apikey] [country]".format(sys.argv[0]))
