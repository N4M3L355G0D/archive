#! /usr/bin/env python3
#NoGuiLinux
import datetime
import csv,pandas as pd,numpy

class container:
    master=None
    class data:
        master=None
        filenames=["turnstile_110507.txt"]
        updateFileNames=[]
        masterFile="master-turnstile.csv"
        fields='C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n'
        chunk=5
        udKeyword="updated_"

    class processing:
        master=None
        def fixCsv(self):
            filenames=self.master.data.filenames
            udKeyword=self.master.data.udKeyword
            chunk=self.master.data.chunk
    
            updateFileNames=[]
            for file in filenames:
                updateFileNames.append(udKeyword+file)
                with open(file,'r') as idata, open(udKeyword+file,"wb") as odata:
                    data=csv.reader(idata,delimiter=",")
                    for row in data:
                        rowId=row[:3]
                        rowE=row[3:]
                        d=[rowE[i:i+chunk] for i in range(0,len(rowE),chunk)]
                        for i in d:
                            for num,l in enumerate(i):
                                i[num]=i[num].strip(' ')
                            rowA=[]
                            rowA.extend(rowId)
                            rowA.extend(i)
                            entry=','.join(rowA)+"\n"
                            odata.write(entry.encode())
            return updateFileNames

        def toMaster(self,masterFile,updateFileNames):
            fields=self.master.data.fields
            with open(masterFile, 'wb') as master_file:
                    master_file.write(fields.encode())
                    for filename in updateFileNames:
                        with open(filename,'rb') as idata:
                            while True:
                                data=idata.read(1024)
                                if not data:
                                    break
                                master_file.write(data)
        def loadData(self,masterfile):
            data=pd.read_csv(masterfile)
            data.fillna(1)
            df=pd.DataFrame(data)
            return df

        def returnReg(self,df):
            return df[df['DESCn'] == 'REGULAR']

        def entriesHourly(self,df):
            dfSeries=pd.Series(df['ENTRIESn'] - df['ENTRIESn'].shift(1))
            df['ENTRIESn_hourly']=dfSeries.fillna(1)
            return df

        def exitsHourly(self,df):
            dfSeries=pd.Series(df['EXITSn'] - df['EXITSn'].shift(1))
            df['EXITSn_hourly']=dfSeries.fillna(1)
            return df

        def hoursCol(self,df):
            dfSeries=df['TIMEn'].str.split(":",expand=False).apply(lambda x: int(x[0]))
            df['HOURn']=dfSeries
            return df

        def datesFix(self,df,useDt=True):
            #import datetime
            #date=datetime.datetime.strptime('2-20-2005','%m-%d-%Y')
            #print('-'.join([str(i) for i in [date.year,date.month,date.day]]))
            #date_reformatted='-'.join([str(i) for i in [i for num,i in enumerate(datetime.datetime.strptime('2-20-2005','%m-%d-%Y').timetuple()) if num < 3]])
            if useDt == True:
                #i love some of my one liners, until they fail, of course.
                #udacity drove to do allow for datetime or pandas options
                dfSeries=df['DATEn'].apply(lambda x: '-'.join([str(i) for i in [ '0'*(2-len(str(i)))+str(i) for num,i in enumerate(datetime.datetime.strptime(x,'%m-%d-%y').timetuple()) if num < 3]]))
            else:
                dfSeries=pd.to_datetime(df['DATEn'],yearfirst=True,format='%m-%d-%y')
            df['DATEn']=dfSeries
            return df

    class void:
        master=None

    class tasks:
        master=None
        def run(self):
            masterFile=self.master.data.masterFile

            filenames=self.master.processing.fixCsv()
            self.master.processing.toMaster(masterFile,filenames)
            df=self.master.processing.loadData(masterFile)
            regOnly=self.master.processing.returnReg(df)
            entriesHourly=self.master.processing.entriesHourly(regOnly)
            exitsHourly=self.master.processing.exitsHourly(entriesHourly)
            hoursCol=self.master.processing.hoursCol(exitsHourly)
            date=self.master.processing.datesFix(hoursCol)
            print(date)

    def assembler(self):
        wa=self.void()
        wa.master=wa
        wa.data=self.data()
        wa.data.master=wa
        wa.processing=self.processing()
        wa.processing.master=wa
        wa.run=self.tasks()
        wa.run.master=wa
        wa.run.run()

if __name__ == "__main__":
    c=container()
    c.assembler()
