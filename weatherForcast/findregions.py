#! /usr/bin/env python3
#NoGuiLinux

from xml.etree.ElementTree import Element,SubElement, tostring
from bs4 import BeautifulSoup as bs
import urllib.request
import sqlite3,os,sys

db=sqlite3.connect('urls.db')
cursor=db.cursor()
cursor.execute("create table if not exists e404(hourlyUrl text, id INTEGER PRIMARY KEY AUTOINCREMENT);")
cursor.execute("create table if not exists webaddress(hourlyUrl text,tendayUrl text,location text,id INTEGER PRIMARY KEY AUTOINCREMENT);")

top=Element('location')

abrevsFile='stateAbbrevs.txt'
fillState=open(abrevsFile,'r')
#get state abbreviations from textfile
state=[i.rstrip('\n') for i in fillState]
fillState.close()

failedLog='fails.txt'
failed=open(failedLog,'w')
outfile='urls.xml'
ofile=open(outfile,'wb')
counter404=0
max404=9999
for x in state:
    for i in range(9999):
        num=str(i+1)
        if len(str(num)) < 4:
            num='0'*(4-len(str(num)))+num
        addressTenDay='https://weather.com/tenday/l/US{}{}:1:US'.format(x,num)
        address='https://weather.com/weather/hourbyhour/l/US{}{}:1:US'.format(x,num)
        cursor.execute('select hourlyUrl from webaddress where hourlyUrl="{}";'.format(address))
        result=cursor.fetchone()
        if result == None:
            cursor.execute('select hourlyUrl from webaddress where hourlyUrl="{}";'.format(address))
            result=cursor.fetchone()
            if result == None:
                try:
                    url=urllib.request.urlopen(address)
                    soup=bs(url,'html.parser')
                    location=soup.find('span',{'class':'styles-xz0ANuUJ__locationName__1t7rO'})
                    if location != None:
                        #get web page
                        location=location.text
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
                        cursor.execute('insert into webaddress(hourlyUrl,tendayUrl,location) values ("{}","{}","{}");'.format(address,addressTenDay,location))
                        db.commit()
                        #if within max404, a new region is found, reset counter404 to zero, we need to try to find all regions
                        counter404=0
                    else:
                        failed.write(address) 
                except OSError as err:
                    print('{} : {} : 404'.format(counter404,address))
                    print(err)
                    cursor.execute('insert into e404(hourlyUrl) values ("{}");'.format(address))
                    db.commit()
                    if counter404 <= max404:
                        counter404+=1
                    else:
                        break
            else:
                counter404=0
                print('\'{}\' : already stored in {}'.format(address,'urls.db'))
        else:
            print('\'{}\' : already stored in {}.e404 as NotFound'.format(address,'urls'))
db.commit()
db.close()

ofile.write(tostring(top))
ofile.close()
prog.close()
failed.close()
