#! /usr/bin/env python3
import pandas as pd
import numpy


class container:
    class files:
        master=None
        file="baseballdatabank-master/core/People.csv"
        ofile='People.csv'

    class data:
        master=None
        def loadData(self,file):
            data=pd.read_csv(file)
            df=pd.DataFrame(data)
            return df

        def writeData(self,ofile,df):
            df.to_csv(ofile)

    class processing:
        def newColumn(self,df):
            df['playerFullName']=df['nameFirst']+" "+df['nameLast']
            return df

    class void:
        master=None
   
    class tasks:
        master=None
        def run(self):
            df=self.master.data.loadData(self.master.files.file)
            df=self.master.processing.newColumn(df)
            df.to_csv(self.master.files.ofile)
            print(df)

    def assembler(self):
        wa=self.void()
        wa.master=wa
        
        wa.files=self.files()
        wa.master=wa
        
        wa.data=self.data()
        wa.data.master=wa

        wa.processing=self.processing()
        wa.processing.master=wa

        wa.tasks=self.tasks()
        wa.tasks.master=wa
        wa.tasks.run()

        
run=container()
run.assembler()
