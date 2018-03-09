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
    address='https://www.wunderground.com/hourly/us/or/seaside?cm_ven=localwx_hour'

    def webpage(self,url):
        page=urllib.request.urlopen(url)
        return page

    def setTable(self):
        url=self.webpage(self.address)
        soup=bs(url,'html.parser')
        targetData=soup.find('table',{'id':'hourly-forecast-table'}).find_all('tr')
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

    def printTable(self):
        self.setTable()
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
        header+='\n'+'{}-'.format(color.formatFrontCyan)*((len(header)-(len(color.formatFront+color.formatReset)*orgHdLen))-1)+color.formatReset
        header=header.replace('|','{}|{}'.format(color.formatFrontCyan,color.formatReset))
        header='>'+header
        print(header)
        for i in tableList:
            print('>{}<'.format(i.replace('|','{}|{}'.format(color.formatFrontCyan,color.formatReset))))

a=hourlyForecast()
a.printTable()
