#! /usr/bin/env python3
#NoGuiLinux

from xml.etree.ElementTree import Element,SubElement, tostring
from bs4 import BeautifulSoup as bs
import urllib.request
import sqlite3,os,sys

if os.path.exists('urls.db'):
    os.remove('urls.db')

db=sqlite3.connect('urls.db')
cursor=db.cursor()
cursor.execute("create table if not exists webaddress(url text,location text,id INTEGER PRIMARY KEY AUTOINCREMENT);")

top=Element('location')

abrevsFile='stateAbbrevs.txt'
fillState=open(abrevsFile,'r')
#get state abbreviations from textfile
state=[i.rstrip('\n') for i in fillState]
fillState.close()

outfile='urls.xml'
ofile=open(outfile,'wb')

for x in state:
    for i in range(9999):
        num=str(i+1)
        if len(str(num)) < 4:
            num='0'*(4-len(str(num)))+num
        address='https://weather.com/weather/today/l/US{}{}:1:US'.format(x,num)
        try:
            #get desired info
            url=urllib.request.urlopen(address)
            soup=bs(url,'html.parser')
            location=soup.find('span',{'class':'styles-xz0ANuUJ__locationName__1t7rO'}).text
            printString='{}|{}'.format(location,address)
            sys.stdout.write(os.get_terminal_size().columns*'\b'+printString+' '*(os.get_terminal_size().columns-len(printString)-20))
            sys.stdout.flush()

            #write data to xml data structure
            geo=SubElement(top,'{}{}'.format(x,num))
            town=SubElement(geo,'where')
            town.text=location
            webaddress=SubElement(geo,'url')
            webaddress.text=address
            #write data to sqlite3Db
            cursor.execute('insert into webaddress(url,location) values ("{}","{}");'.format(address,location))
            db.commit()
        except OSError as err:
            #print('{} : 404'.format(address))
            #print(err)
            pass

db.commit()
db.close()

ofile.write(tostring(top))
ofile.close()
