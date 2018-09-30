#! /usr/bin/python3
#NoGuiLinux
#get artist info
import urllib.request as urlRequest
import json,sqlite3,string
import urllib.parse,base64
import time,random

class containerLib:
    class data:
        master=None
        def getData(self,artist,apikey):
            #time.sleep(random.random()+random.randint(0,5))
            artist=urllib.parse.quote(artist)
            url='http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={}&api_key={}&format=json'.format(artist,apikey)
            print(url)
            data=urlRequest.urlopen(url)
            data=json.loads(data.read().decode())
            return data

        def artistFields(self,data):
            fields={}
            try:
                data=data['artist']
                fields['name']=self.master.data.cleanupArtist(data['name'])
                fields['nameb64']=base64.b64encode(data['name'].encode()).decode()
                fields['streamable']=int(data['streamable'])
                fields['ontour']=int(data['ontour'])
                fields['listeners']=int(data['stats']['listeners'])
                fields['played']=int(data['stats']['playcount'])
                fields['similar']=','.join([self.master.data.cleanupArtist(i['name']) for i in data['similar']['artist']])
                fields['tags']=','.join([i['name'] for i in data['tags']['tag']])
                fields['publish_date']=data['bio']['published']
                return fields
            except:
                print(data)
                return None

        def getArtists(self,db,apikey):
            mRow=self.master.artinfo.db.getRows(db)
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
                        data=self.getData(base64.b64decode(result[0].encode()).decode(),apikey)
                        artist=self.master.data.cleanupArtist(base64.b64decode(result[0].encode()).decode())
                        fields=self.artistFields(data)
                        if fields != None:
                            self.master.artinfo.db.mkTable(db,artist,fields)
                            self.master.artinfo.db.insertEntry(db,artist,fields)
                counter+=chunks





    class dbManager:
        master=None
        def getRows(self,db):
            mRowSql='''select rowid from topartists order by rowid desc limit 1;'''
            db['cursor'].execute(mRowSql)
            mRow=db['cursor'].fetchone()
            if mRow != None:
                mRow=mRow[0]
            else:
                exit("there are no rows!")
            return mRow

        def mkFieldsStringT(self,fields):
            fieldL=[]
            for field in fields.keys():
                if type(fields[field]) == int:
                    fieldL.append(field+" real")
                else:
                    fieldL.append(field+" text")
            return ','.join(fieldL)
       
        def mkFieldsStringI(self,fields):
            fieldL=[]
            for field in fields.keys():
                fieldL.append(field)
            return "("+','.join(fieldL)+")"

        def mkFieldDataStringI(self,fields):
            fieldL=[]
            for field in fields.keys():
                if type(fields[field]) == int:
                    fieldL.append(str(fields[field]))
                else:
                    fieldL.append('"'+str(fields[field])+'"')
            return 'values ('+','.join(fieldL)+");"

        def insertEntry(self,db,artist,fields):
            artist=self.removeSpace(artist)
            results=self.checkTable(db,artist,fields)
            if results == False:
                sql="insert into info_{}{} {}".format(artist,self.mkFieldsStringI(fields),self.mkFieldDataStringI(fields))
                db['cursor'].execute(sql)
                db['db'].commit()
            else:
                print("artist already exists in db: '{}'".format(artist))

        def checkTable(self,db,artist,fields):
            artist=self.removeSpace(artist)
            sqlfields=[artist]
            sqlfields.extend([fields[i] for i in fields.keys()])
            a,nameb64,b,c,d,e,f,g,h,i=sqlfields
            sql='''
            select rowid from info_{} where 
            name = "{}" and 
            nameb64 = "{}" and
            streamable = {} and 
            ontour = {} and 
            listeners = {} and 
            played = {} and 
            similar = "{}" and 
            tags = "{}" and 
            publish_date = "{}";'''.format(a,nameb64,b,c,d,e,f,g,h,i)
            db['cursor'].execute(sql)
            result=db['cursor'].fetchone()
            db['db'].commit()
            if result != None:
                return True
            else:
                return False
        
        def removeSpace(self,tbName):
            for i in string.whitespace:
                tbName=tbName.replace(i,"_")
            return tbName
        
        def mkTable(self,db,artist,fields):
            artist=self.removeSpace(artist)
            fieldsStr=self.mkFieldsStringT(fields)
            sql='''
            create table if not exists info_{}({},
            rowid INTEGER PRIMARY KEY AUTOINCREMENT);
            '''.format(artist,fieldsStr)
            db['cursor'].execute(sql)
            db['db'].commit()
            
