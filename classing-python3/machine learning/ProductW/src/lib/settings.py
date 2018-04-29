#! /usr/bin/env python3

import sqlite3,os,base64,sys,time

class settings:
    master=None
    dbName='settings.db'
    autosnap=False
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
 
    def insertNewDefault(self,db,setting,val):
        sql='''
        insert into defaultSetting(setting,val)
        values ("{}","{}")'''.format(setting,val)
        db['cursor'].execute(sql)
        db['db'].commit()

    def closeDb(self):
        self.master.db['db'].commit()
        self.master.db['db'].close()
    
    def initSettings(self):
        db=self.mkDb()
        self.mkTables(db)

        return db

    def getSettings(self,db):
        apikey=self.getDefaultSetting(db,'apikey')
        if apikey == None:
            apikey='No Api key available, please type one in and click "Add Key"'
        self.master.apikey=apikey

        autosnap=self.getDefaultSetting(db,'autosnap')
        if autosnap == None:
            self.insertNewDefault(db,'autosnap','False')
        else:
            print(autosnap,'settings')
            if autosnap == "True":
                self.autosnap=True
            else:
                self.autosnap=False

    def updateSettings(self,db,setting,val):
        sql='''
        update defaultSetting set val='{}' where setting='{}'
        '''.format(val,setting)
        db['cursor'].execute(sql)
        db['db'].commit()
