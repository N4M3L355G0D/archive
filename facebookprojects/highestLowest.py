#! /usr/bin/env python3

import csv


class tideData:
    file='highesttide.txt'
    def getTide(self):
        with open(self.file,'r') as data:
            dialect=csv.Sniffer().sniff(data.read(1024))
            data.seek(0)
            reader=csv.reader(data,dialect)
            rowColAcc=''
            highest=0
            lowest=0
            for row in reader:
                if rowColAcc != row[0]:
                    if rowColAcc != '':
                        print('{0}: {1} meters at lowest and {2} meters at highest'.format(rowColAcc,lowest,highest))
                    rowColAcc=row[0]
                    highest=0
                    lowest=float(row[2].split(' ')[0])
                else:
                    if float(row[2].split(' ')[0]) > highest:
                        highest=float(row[2].split(' ')[0])
                    if float(row[2].split(' ')[0]) < lowest:
                        lowest=float(row[2].split(' ')[0])

run=tideData()
run.getTide()
