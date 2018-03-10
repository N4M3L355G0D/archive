#! /urs/bin/env python3
#get the weather forecast in your textmode interface
#NoGuiLinux

import urllib.request
from bs4 import BeautifulSoup as bs
#address='https://www.wunderground.com/hourly/us/or/seaside?cm_ven=localwx_hour'
#url=urllib.request.urlopen(address)

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
    address='https://www.wunderground.com/hourly/us/ca/seaside?cm_ven=localwx_hour'

    def webpage(self,url):
        page=urllib.request.urlopen(url)
        return page

    def setTable(self):
        url=self.webpage(self.address)
        soup=bs(url,'html.parser')
        targetData=soup.find('table',{'id':'hourly-forecast-table'}).find_all('tr')
        if targetData != None:
            #set rowCast data
            for i in targetData:
                rowdata=i.find_all('td')
                if len(rowdata) > 0:
                    time=rowdata[0].find_all('span')[0].text
                    conditions=rowdata[1].find_all('span')[1].text
                    temp=rowdata[2].find_all('span')[0].text
                    feelsLike=rowdata[3].find_all('span')[0].text
                    precip=rowdata[4].find_all('span')[0].text
                    amount=rowdata[5].find_all('span')[0].text
                    cloudCover=rowdata[6].find_all('span')[0].text
                    dewpoint=rowdata[7].find_all('span')[0].text
                    humidity=rowdata[8].find_all('span')[0].text
                    wind=rowdata[9].find_all('span')[0].text
                    pressure=rowdata[10].find_all('span')[0].text.replace('\n','')
                    self.rowCast={'time':time,'conditions':conditions,'temp':temp,'feels_like':feelsLike,'precip':precip,'amount':amount,'cloud_cover':cloudCover,'dew_point':dewpoint,'humidity':humidity,'wind':wind,'pressure':pressure}
                    self.table.append(self.rowCast)
        else:
            self.Table=None


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
        specdata=soup.find('tbody')
        if specdata != None:
            specdata=specdata.find_all('tr')
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

hourly=hourlyForecast()
hourly.setTable()

tenDay=tenDayForecast()
tenDay.setTable()
#set the display interface
disp=display()

#display ten day forecast
disp.table=tenDay.table
disp.printTable()

#display hourly forecast
disp.table=hourly.table
disp.printTable()
