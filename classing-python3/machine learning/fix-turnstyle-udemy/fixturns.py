#! /usr/bin/env python3

import csv,pandas

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
    class void:
        master=None

    class tasks:
        master=None
        def run(self):
            masterFile=self.master.data.masterFile

            filenames=self.master.processing.fixCsv()
            self.master.processing.toMaster(masterFile,filenames)

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
