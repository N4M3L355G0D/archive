#! /usr/bin/env python3
#NoGuiLinux
#take data from csv file and input it into a sqlite3 db

import pandas as pd
import pandasql
import numpy
import os,sqlite3
import argparse
import string

class container:
    class data:
        master=None
        file=''
        invalidChars=string.punctuation+string.whitespace
        invalidCol=string.digits
        def loadData(self,file):
            data=pd.read_csv(file)
            for char in self.invalidChars:
                data.rename(columns=lambda x: x.replace(char,"_").lower(),inplace=True)
            data.rename(columns=lambda x: "c_"+x if x[0] in self.invalidCol else x,inplace=True)
            df=pd.DataFrame(data)
            return df

        def checkDb(self,dbName):
            if os.path.exists(dbName) and os.path.isfile(dbName):
                os.remove(dbName)

    class dbManager:
        master=None
        def mkTableCols(self,df):
            tableCols=[]
            dfCols=df.columns.get_values()
            for col in dfCols:
                if df[col].dtype != 'object':
                    tableCols.append("{} real".format(col))
                if df[col].dtype == 'object':
                    tableCols.append("{} text".format(col))
            return tableCols

        def mkTableName(self,file):
            tableName=os.path.splitext(file)[0].replace(' ',"_").lower()
            for char in self.master.data.invalidChars:
                tableName=tableName.replace(char,"_").lower()
            return tableName

        def mkTableSql(self,tableCols,tableName):
            tableSql="create table if not exists {}({},rowid INTEGER PRIMARY KEY AUTOINCREMENT);".format(tableName,','.join(tableCols))
            return tableSql

        def mkDbName(self,file):
            return os.path.splitext(file)[0]+".db"

        def mkDb(self,dbName):
            db={}
            db['db']=sqlite3.connect(dbName)
            db['cursor']=db['db'].cursor()
            return db

        def dbCleanup(self,db):
            db['db'].commit()
            db['db'].close()

        def insertEntry(self,sql,db):
            try:
                db['cursor'].execute(sql)
            except OSError as e:
                print(sql)
                print(e)
                exit(1)

        def mkEntries(self,tableName,df,db):
            counter=0
            valuesStr=None
            tableRows=len(df)
            dfCols=df.columns.get_values()
            values=[]
            msg="Processed Entries: "
            for i in range(tableRows):
                for x in range(len(dfCols)):
                    column=df.loc[i][dfCols[x]]
                    if type(column) != str:
                        if str(column) == 'nan':
                            column='Null'
                        values.append(str(column))
                    elif type(column) == str:
                        if column == '':
                            column='Null'
                        values.append('"{}"'.format(column))
                sql='insert into {} ({}) values({});'.format(tableName,','.join(dfCols),','.join(values))
                values=[]
                print(str(len(str(counter)+msg)*"\b")+msg+str(counter),end='')
                if ( counter % 1000 ) == 0:
                    db['db'].commit()
                counter+=1
                self.insertEntry(sql,db)

    class cmdline:
        master=None
        def getargs(self):
            parser=argparse.ArgumentParser()
            parser.add_argument("-f","--file",help="csv input file",required="yes")
            options,unknown=parser.parse_known_args()
            return options

    class void:
        master=None

    class tasks:
        master=None
        def run(self):
            options=self.master.cmd.getargs()
            self.master.data.file=options.file

            file=self.master.data.file

            dbName=self.master.db.mkDbName(file)
            self.master.data.checkDb(dbName)
            db=self.master.db.mkDb(dbName)
            df=self.master.data.loadData(file)
            
            tableName=self.master.db.mkTableName(file)
            tableCols=self.master.db.mkTableCols(df)
            tableSql=self.master.db.mkTableSql(tableCols,tableName)
            #make table
            self.master.db.insertEntry(tableSql,db)
            #add entries to table
            self.master.db.mkEntries(tableName,df,db)
            self.master.db.dbCleanup(db)
            print("\ncompleted! '{}' -> '{}'".format(file,dbName))

    def assembler(self):
        wa=self.void()
        wa.master=wa
        
        wa.cmd=self.cmdline()
        wa.cmd.master=wa

        wa.data=self.data()
        wa.data.master=wa

        wa.db=self.dbManager()
        wa.db.master=wa

        wa.tasks=self.tasks()
        wa.tasks.master=wa
        wa.tasks.run()

run=container()
run.assembler()

#sql='''select registrar,enrolment_agency from data limit 50'''
#solution=pandasql.sqldf(sql.lower(),locals())
#print(solution)
