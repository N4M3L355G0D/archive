#! /usr/bin/env python3

import urllib.request
import urllib.error
import urllib.parse
import gzip,os,sys
from bs4 import BeautifulSoup as bs
import time,base64,sqlite3
import argparse

sort='priceasc'
availability='0'
#mode 0 - immediately
#mode 1 - available in 30 days
#mode 2 - available beyond 30 days
minCost='600'
zipcode='93933'
#bug found -- duplicate data entries are deing displayed, i think it has problems in the scraper returning the data
#will fix soon

class container:
    class web:
        master=None
        #need to create a function to look at each result url, get the page, parse the page and scrape information pertaining
        #to the room for rent from the page
        #save the result into appropriate table rows
        #tString='2018-4-30 5:20pm'
        def fixTime(self,tString):
            dString=' '.join([i for i in tString.split(' ') if i != ''])
            date=dString.split(' ')[0]
            dTime=dString.split(' ')[1]
            if dTime[-2] == 'a':
                dTime=dTime[:-2]
            else:
                dTime=dTime.split(':')
                dTime=str(int(dTime[0])+12)+":"+dTime[1][:-2]    
            dString=date+" "+dTime
            dString=time.strptime(dString,'%Y-%m-%d %H:%M')
            dString=time.strftime('%d-%m-%Y %H:%M:%S',dString)
            return dString

        def genUrl(self,sort,availability,minCost,zipcode):
            url='''https://monterey.craigslist.org/search/roo?sort={}&availabilityMode={}&min_price={}&postal={}'''.format(
                    urllib.parse.quote(sort),
                    urllib.parse.quote(availability),
                    urllib.parse.quote(minCost),
                    urllib.parse.quote(zipcode)
                    )
            return url
        def getUrl2(self,url):
            dTime=''
            info={'attrs':'','desc':'','postDate':''}
            try:
                con=urllib.request.urlopen(url)
                data=con.read()
                soup=bs(data,'html.parser')
                attrs=[]
                desc=[]
                for target in soup.find_all('section',{'class':'userbody'}):
                    for attr in target.find_all('p',{'class':'attrgroup'}):
                        for span in attr.find_all('span'):
                            attrs.append(span.text)
                    for section in target.find_all('section',{'id':'postingbody'}):
                        desc.append(section.text) 
                    for section in target.find_all('time',{'class':'date timeago'}):
                        dTime=self.fixTime(section.text)
                attrs=','.join(attrs)
                desc=','.join(desc)
                desc=[i for i in desc.split('\n') if i != '']
                desc=' '.join(desc[1:])
                info={'attrs':attrs,'desc':desc,'postDate':dTime}
                return info
            except urllib.error.HTTPError as e:
                err=str(e)
                print(err)
                return info
            except OSError as e:
                err=str(e)
                print(err)
                return info

        def gatherGen(self,url):
            try:
                con=urllib.request.urlopen(url)
                data=con.read()
                soup=bs(data,'html.parser')
                for results in soup.find_all('p',{'class':'result-info'}):
                    resolution={}
                    if results != None:
                        for link in results.find_all('a',{'class':'result-title hdrlnk'}):
                            resolution['href']=link.get('href')
                            info=self.getUrl2(resolution['href'])
                            resolution['attrs']=info['attrs']
                            resolution['desc']=info['desc']
                            resolution['postDate']=info['postDate']
                            #integrate results from getUrl2 into resolution next
                        for meta in results.find_all('span',{'class':'result-meta'}):
                            for price in meta.find_all('span',{'class':'result-price'}):
                                resolution['price']=float(price.text.replace('$',''))
                        for hood in meta.find_all('span',{'class':'result-hood'}):
                                resolution['hood']=hood.text
                    yield resolution
            except urllib.error.HTTPError as e:
                print(str(e))
                return None
            except OSError as e:
                print(str(e))
                return None

    class dbManager:
        termSize=20
        invTblChar=['-',':',' ']
        master=None
        db={}
        dbname='roomResults-cache.db'
        currentTable=''
        def dbCon(self):
            self.db['db']=sqlite3.connect(self.dbname)
            self.db['cursor']=self.db['db'].cursor()

        #create insert entry [done]
        #create query entry
        #create table creation function [done]
        def mkTable(self,db):
            currentDate=self.currentDate()
            for char in self.invTblChar:
                if char in currentDate:
                    currentDate=currentDate.replace(char,'_')
            self.currentTable='ad_{}'.format(currentDate)
            sql='''create table if not exists {}(
            price real,
            attrs text,
            hood text,
            href text,
            desc text,
            currentDate text,
            postDate text,
            rowid INTEGER PRIMARY KEY AUTOINCREMENT);
            '''.format(self.currentTable)
            db['cursor'].execute(sql)
            db['db'].commit()
        def currentDate(self):
            currentDate=time.strftime('%d-%m-%Y %H:%M:%S',time.localtime())
            return currentDate

        def insertEntry(self,db,results):
            currentDate=self.currentDate()
            postDate=results['postDate']
            price=results['price']
            attrs=results['attrs']
            href=results['href']
            desc=results['desc']

            sql='''
            insert into {}(price,attrs,hood,desc,currentDate,postDate) values
            ({},"{}","{}","{}","{}","{}");'''.format(self.currentTable,price,attrs,href,base64.b64encode(gzip.compress(desc.encode())).decode(),currentDate,postDate);
            db['cursor'].execute(sql)
            db['db'].commit()
    
        def displayQuery(self,results):
            for i in results:
                print(self.termSize*'=')
                for num,x in enumerate(i):
                    if num == 4:
                        print('Description: {}'.format(gzip.decompress(base64.b64decode(x.encode())).decode()))
                    else:
                        if num == 0:
                            print("Price: {}".format(x))
                        elif num == 1:
                            print("attributes: {}".format(x))
                        elif num == 2:
                            print("Link: {}".format(x))
                        elif num == 3:
                            print("Hood: {}".format(x))
                        elif num == 5:
                            print("Current_Date: {}".format(x))
                        elif num == 7:
                            print("Result: {}".format(x))
                        elif num == 6:
                            print("Post_Date: {}".format(x))
                        else:
                            print(num,x)
        def queryEntry(self,db,params):
            sql='''select * from {} {};'''.format(self.currentTable,params)
            db['cursor'].execute(sql)
            results=db['cursor'].fetchall()
            if results != None:
                self.displayQuery(results)
            else:
                print("there were no results")
            db['db'].commit()

        def cleanup(self,db):
            db['db'].commit()
            db['db'].close()

    class void:
        master=None

    class cmdline:
        master=None
        def args(self):
            parser=argparse.ArgumentParser()
            parser.add_argument('-s','--sql',help='sql where')
            parser.add_argument('-S','--Sort',help='newest,oldest,priceasc,pricedesc')
            parser.add_argument('-a','--availability-mode',help='0 - {}, 1 - {}, 2 - {}'.format('ASAP','within 30 days','after 30 days'))
            parser.add_argument('-m','--mincost')
            parser.add_argument('-M','--maxcost',help='not implement yet, but coming soon!')
            parser.add_argument('-z','--zipcode')

            options,unknown=parser.parse_known_args()
            return options

    class run:
        master=None
        def run(self):
            args=self.master.cmdline.args()

            if args.Sort:
                sort=args.Sort
            else:
                sort=self.master.external.sort

            if args.availability_mode:
                availability=args.availability_mode
            else:
                availability=self.master.external.availability

            if args.mincost:
                minCost=args.mincost
            else:
                minCost=self.master.external.minCost
    
            if args.zipcode:
                zipcode=args.zipcode
            else:
                zipcode=self.master.external.zipcode


            url=self.master.web.genUrl(sort,availability,minCost,zipcode)
            results=self.master.web.gatherGen(url)
            self.master.dbm.dbCon()
            db=self.master.dbm.db
            self.master.dbm.mkTable(db)
            
            for result in results:
                self.master.dbm.insertEntry(db,result)
    
            if args.sql:
                sql=args.sql
            else:
                sql=''
            self.master.dbm.queryEntry(db,sql)

    def assembler(self):
        
        self.sort='priceasc'
        self.availability='0'
        self.minCost='600'
        self.zipcode='93933'
                
        self.wa=self.void()
        self.wa.master=self.wa
        #give access of lower classes to top level class container
        self.wa.external=self
        
        self.wa.cmdline=self.cmdline()
        self.wa.master=self.wa

        self.wa.web=self.web()
        self.wa.master=self.wa
        
        self.wa.dbm=self.dbManager()
        self.wa.dbm.master=self.wa

        self.wa.run=self.run()
        self.wa.run.master=self.wa
        self.wa.run.run()

run=container()
run.assembler()
