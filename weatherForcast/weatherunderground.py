#! /urs/bin/env python3
#get the weather forecast in your textmode interface
#NoGuiLinux

import urllib.request
from bs4 import BeautifulSoup as bs
import sqlite3, pymysql, time

#terminal colorization for table output
class colors:
    formatReset='\033[0;m'
    formatFront='\033[1;32;40m'
    formatFrontCyan='\033[1;36;40m'
    colorFrontCell='\033[31;40m'

color=colors()

#get the hourly forecast
class hourlyForecast:
    table=[]
    rowCast={}
    address='https://weather.com/weather/hourbyhour/l/USCA1037:1:US'

    def webpage(self,url):
        page=urllib.request.urlopen(url)
        return page

    def setTable(self):
        url=self.webpage(self.address)
        soup=bs(url,'html.parser')
        targetData=soup.find('table',{'class':'twc-table'})
        if targetData != None:
            targetData=targetData.find('tbody').find_all('tr')
            #set rowCast data
            for i in targetData:
                #day column
                timeDay=''
                timeHour=''
                time=i.find('td',{'headers':'time'})
                timeDay=time.find('div',{'class':'hourly-date'}).text
                timeHour=time.find('div',{'class':'hourly-time'}).find('span',{'class':'dsx-date'}).text
                time='{} {}'.format(timeDay,timeHour)
                #description
                desc=i.find('td',{'headers':'description'}).text
                #temp
                temp=i.find('td',{'headers':'temp'})
                temp='/'.join([i.text for i in temp.find_all('span') if i.text != ''])
                #precip
                precip=i.find('td',{'headers':'precip'}).find('span',{'class':''}).text
                #feels like
                feels=i.find('td',{'headers':'feels'}).text
                #wind
                wind=i.find('td',{'headers','wind'}).find('span',{'class':''}).text
                #humidity
                humidity=i.find('td',{'headers','humidity'}).find('span',{'class':''}).text
                #append to table
                self.rowCast={'time':time,'desc':desc,'temp':temp,'feels_like':feels,'precip':precip,'wind':wind,'humidity':humidity}
                self.table.append(self.rowCast)
                #self.table=None
        else:
            self.table=None


class display:
    table=[]
    def printTable(self):
        if self.table != None:
            header=[color.formatFront+i+color.formatReset for i in self.table[0].keys()]
            orgHdLen=len(header)
            longest=0
            tableList=[]
            #get  the longest table cell
            for i in self.table:
                for x in i.keys():
                    if len(i[x]) > longest:
                        longest=len(i[x])
            #adjust all table cells to longest table cell
            for i in self.table:
                row=[]
                for x in i.keys():
                    if len(i[x]) <= longest:
                        i[x]+=' '*(longest-len(i[x]))
                        i[x]=color.colorFrontCell+i[x]+color.formatReset
                    row.append(i[x])
                tableList.append('|'.join(row))

            for num,i in enumerate(header):
                if len(i)-len(color.formatFront+color.formatReset) <= longest:
                    header[num]+=' '*(longest-((len(i)-len(color.formatFront+color.formatReset))))
        
            header='|'.join(header)
            separator='{}-'.format(color.formatFrontCyan)*((len(header)-(len(color.formatFront+color.formatReset)*orgHdLen))-3)+color.formatReset
            header=header.replace('|','{}|{}'.format(color.formatFrontCyan,color.formatReset))
            print(header,separator,sep='\n')
            for i in tableList:
                print('{}'.format(i.replace('|','{}|{}'.format(color.formatFrontCyan,color.formatReset))))
        else:
            print("no data available at this time")

class tenDayForecast:
    table=[]
    rowCast={}
    address='https://weather.com/weather/tenday/l/Seaside+CA+93955:4:US'
    def webpage(self,url):
        url=urllib.request.urlopen(url)
        return url

    def setTable(self):
        page=self.webpage(self.address)
        soup=bs(page,'html.parser')
        table=[]
        rowCast={}
        specdata=soup.find('table',{'class':'twc-table'})
        if specdata != None:
            specdata=specdata.find('tbody').find_all('tr')
            for i in specdata:
                #day column
                day=i.find('td',{'headers':'day'})
                dayName=day.find('span',{'class':'date-time'}).text
                dayDetail=day.find('span',{'class':'day-detail clearfix'}).text
                day='{} {}'.format(dayName,dayDetail)
                #description
                desc=i.find('td',{'headers':'description'}).text
                #temp
                temp=i.find('td',{'headers':'hi-lo'})
                temp='/'.join([i.text for i in temp.find_all('span') if i.text != ''])
                #precip
                precip=i.find('td',{'headers':'precip'}).find('span',{'class':''}).text
                #wind
                wind=i.find('td',{'headers','wind'}).find('span',{'class':''}).text
                #humidity
                humidity=i.find('td',{'headers','humidity'}).find('span',{'class':''}).text
                #append to table
                self.rowCast={'day':day,'desc':desc,'temp':temp,'precip':precip,'wind':wind,'humidity':humidity}
                self.table.append(self.rowCast)
        else:
            self.table=None

class recordTable:
    #save the statistics to local db
    table=[]
    dbName='stats.db'
    date=''
    DB={}
    def connect(self):
        db=sqlite3.connect(self.dbName)
        cursor=db.cursor()
        self.DB={'db':db,'cursor':cursor}

    def getTime(self):
        self.date=time.ctime()

    def mk10DayTable(self):
        db=self.DB['db']
        cursor=self.DB['cursor']
        sql='''
        create table if not exists tendayForecast(day text,temp text,description text,precip text,wind text,humidity text,
        date text, rowid INTEGER PRIMARY KEY AUTOINCREMENT);

        '''
        cursor.execute(sql)
        db.commit()
    def mkHourlyTable(self):
        db=self.DB['db']
        cursor=self.DB['cursor']
        sql='''
        create table if not exists hourlyForecast(time text, desc text, temp text, feels_like text, precip text, wind text,
        humidity text,date text,rowid INTEGER PRIMARY KEY AUTOINCREMENT);
        '''
        cursor.execute(sql)
        db.commit()
    def insertHourlyData(self):
        self.getTime()
        for i in self.table:
            sql='''
            insert into hourlyForecast(time,desc,temp,feels_like,precip,wind,humidity,date)
            values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}")
            '''.format(i['time'],i['desc'],i['temp'],i['feels_like'],i['precip'],i['wind'],i['humidity'],self.date)
            self.DB['cursor'].execute(sql)
            self.DB['db'].commit()

    def closeTable(self,DB={}):
        self.DB['db'].close()
        self.DB['db'].close()

    def insert10DayData(self):
        self.getTime()
        for i in self.table:
            sql='''insert into tendayForecast(day,temp,description,precip,wind,humidity,date)
            values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}");'''.format(i['day'],i['temp'],i['desc'],i['precip'],i['wind'],i['humidity'],self.date)
            self.DB['cursor'].execute(sql)
            self.DB['db'].commit()

disp=display()
tenday=tenDayForecast()
tenday.setTable()
hourly=hourlyForecast()
hourly.setTable()

record=recordTable()
record.connect()

record.mk10DayTable()
record.table=tenday.table
disp.table=tenday.table
disp.printTable()
record.insert10DayData()

record.mkHourlyTable()
record.table=hourly.table
disp.table=hourly.table
disp.printTable()
record.insertHourlyData()

record.closeTable()


