#! /usr/bin/python3
#NoGuiLinux
#get artist info
import urllib.request as urlRequest
import json,sqlite3,string
import urllib.parse

class containerLib:
    class data:
        master=None
        def getData(self,artist,apikey):
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

    class dbManager:
        master=None
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
            a,b,c,d,e,f,g,h,i=sqlfields
            sql='''
            select rowid from info_{} where 
            name = "{}" and 
            streamable = {} and 
            ontour = {} and 
            listeners = {} and 
            played = {} and 
            similar = "{}" and 
            tags = "{}" and 
            publish_date = "{}";'''.format(a,b,c,d,e,f,g,h,i)
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
            
