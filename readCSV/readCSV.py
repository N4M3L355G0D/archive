import csv, os, string


class findRowCSV:
    csvFile='xlsx.xlsx'
    filePath=''
    ERROR_NOTFILE="hmmm... that does not look like a file..."
    ERROR_JUST_DOESNOT_EXIST='''
    well, the file '{}', you specified does not exist!
    '''
    WARN_NODATA='no data was found!'
    ignore='\t\n\r'

    def processLongString(self,longer):
        #promote easier readability of the rest of the code
        return ' '.join([j for j in ''.join([ i for i in longer if i not in self.ignore]).split(' ') if j != ''])

    def checkPath(self):
        self.filePath=os.path.realpath(os.path.expanduser(self.csvFile))
        if os.path.exists(self.filePath):
            if os.path.isfile(self.filePath):
                return self.filePath
            else:
                exit(self.ERROR_NOTFILE)
        else:
            exit(self.processLongString(self.ERROR_JUST_DOESNOT_EXIST.format(self.csvFile)))

    def findData(self,searchTerm):
        file=self.checkPath()
        found=0
        with open(file,newline='') as csvfile:
            dialect=csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader=csv.reader(csvfile,dialect)
            for row in reader:
                if searchTerm in row:
                    print(','.join(row))
                    found+=1
            if found == 0:
                print(self.WARN_NODATA)
readit=findRowCSV()
readit.findData('am')
