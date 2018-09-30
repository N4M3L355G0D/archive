#! /usr/bin/env python3
#NoGuiLinux
import csv


class tideData:
    file='highesttide.txt'
    #if you want to access the data loaded from the text file
    #run getTide() ; each row will appended to allEntries as a list
    #since tideData will be used as an object, the data will be
    #persistent for the lifetime of the script
    allEntries=[]
    def getTide(self):
        rowColAcc=''
        time=''
        lowTimeM=0
        lowest=0
        lowTimeAcc=0
        lowTimeCounter=0
        lowTimeAvg=0
        highTimeM=0
        highest=0
        highTimeAcc=0
        highTimeCounter=0
        highTimeAvg=0
        dataTableSingleEntry=[]
        with open(self.file,'r') as data:
            dialect=csv.Sniffer().sniff(data.read(1024))
            data.seek(0)
            reader=csv.reader(data,dialect)
            for row in reader:
                if rowColAcc != row[0]:
                    if rowColAcc != '':
                        print('{0}: {1} meters at lowest ({2}) and {3} meters at highest ({4})'.format(rowColAcc,lowest,lowTimeM,highest,highTimeM))
                        dataTableSingleEntry=[rowColAcc,lowest,lowTimeM,highest,highTimeM]
                        self.allEntries.append(dataTableSingleEntry)
                    rowColAcc=row[0]
                    highest=float(row[2].split(' ')[0])
                    lowest=float(row[2].split(' ')[0])
                else:
                    if float(row[2].split(' ')[0]) > highest:
                        highest=float(row[2].split(' ')[0])
                        highTimeAcc+=float(row[1])
                        highTimeCounter+=1
                        highTimeM=row[1]
                    if float(row[2].split(' ')[0]) < lowest:
                        lowest=float(row[2].split(' ')[0])
                        lowTimeAcc+=float(row[1])
                        lowTimeCounter+=1
                        lowTimeM=row[1]
            #the last two rows get cut off in the display, so print here
            print('{0}: {1} meters at lowest ({2}) and {3} meters at highest ({4})'.format(rowColAcc,lowest,lowTimeM,highest,highTimeM))
            dataTableSingleEntry=[rowColAcc,lowest,lowTimeM,highest,highTimeM]
            self.allEntries.append(dataTableSingleEntry)
        print('\nOver the full period, on average the lowest\nand highest tides accurred at {}\nand {} hours after midnight"'.format(round(lowTimeAcc/lowTimeCounter,2),round(highTimeAcc/highTimeCounter,2)))

run=tideData()
run.getTide()
