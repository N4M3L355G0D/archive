#! /usr/bin/env python3

import sqlite3,os,base64,sys,time

class settings:
    master=None
    dbName='settings.db'

    def mkDb(self):
        db={}
        db['db']=sqlite3.connect(self.dbName)
        db['cursor']=db['db'].cursor()
        return db

    def mkTables(self,db):
        SQL=[]
        sql='''
        create table 
        if not exists
        apiKeys (
        apikey text,
        date text,
        rowid
        INTEGER
        PRIMARY KEY 
        AUTOINCREMENT 
        );
        '''
        SQL.append(sql)
        sql='''
        create table
        if not exists
        defaultSetting (
        setting text,
        val text,
        rowid
        INTEGER
        PRIMARY KEY
        AUTOINCREMENT
        );
        '''
        SQL.append(sql)
        for sql in SQL:
            db['cursor'].execute(sql)
        db['db'].commit()
    
    def insertNewKey(self,db,apikey):
        date=time.ctime()
        sql='''
        insert into apiKeys
        (apikey,date) values
        ('{}','{}');
        '''.format(apikey,date)
        db['cursor'].execute(sql)
        db['db'].commit()

    def getNewestKey(self,db):
        sql='''
        select apikey from apiKeys
        order by rowid desc limit 1;
        '''
        db['cursor'].execute(sql)
        result=db['cursor'].fetchone()
        db['db'].commit()
        if result != None:
            result=result[0]
        else:
            print("error! No apikey!")
        return result

    def getDefaultSetting(self,db,setting):
        sql='''
        select val from defaultSetting
        where setting = '{}' order by rowid
        desc limit 1;
        '''.format(setting)
        db['cursor'].execute(sql)
        result=db['cursor'].fetchone()
        if result != None:
            result=result[0]
        else:
            print("error! no setting '{}'!".format(setting))
        db['db'].commit()
        return result

    def getKeyFromDefaults(self,db):
        defaultRowid=self.getDefaultSetting(db,'apikey')
        if defaultRowid != None:
            sql='''
            select apikey from apiKeys
            where rowid = '{}' limit 1;
            '''.format(defaultRowid)
            db['cursor'].execute(sql)
            result=db['cursor'].fetchone()
            if result != None:
                result=result[0]
                return result
            else:
                print("""error! there is not  
                a default api key set!
                """)
        else:
            print('''there is not default
            api key set''')
        db['db'].commit()

    def insertNewDefault(self,db,setting,val):
        sql='''
        insert into defaultSetting(setting,val)
        values ("{}","{}")'''.format(setting,val)
        db['cursor'].execute(sql)
        db['db'].commit()

    def closeDb(self,db):
        db['db'].commit()
        db['db'].close()

'''
if __name__ == '__main__':
    #test settings functions
    setting=settings()
    db=setting.mkDb()
    setting.mkTables(db)
    setting.insertNewKey(db,"key 2")
    setting.insertNewDefault(db,'apikey','1')
    newestKey=setting.getNewestKey(db)
    print(newestKey,'getNewestKey()')
    keyFromDef=setting.getKeyFromDefaults(db)
    print(keyFromDef,'getKeyFromDef()')
    setting.closeDb(db)
'''
