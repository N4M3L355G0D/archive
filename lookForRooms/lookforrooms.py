#! /usr/bin/env python3

import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup as bs
sort='priceasc'
availability='0'
#mode 0 - immediately
#mode 1 - available in 30 days
#mode 2 - available beyond 30 days
minCost='600'
zipcode='93933'
class container:
    class web:
        master=None
        #need to create a function to look at each result url, get the page, parse the page and scrape information pertaining
        #to the room for rent from the page
        #save the result into appropriate table rows
        def genUrl(self,sort,availability,minCost,zipcode):
            url='''https://monterey.craigslist.org/search/roo?sort={}&availabilityMode={}&min_price={}&postal={}'''.format(
                    urllib.parse.quote(sort),
                    urllib.parse.quote(availability),
                    urllib.parse.quote(minCost),
                    urllib.parse.quote(zipcode)
                    )
            return url

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
                        for meta in results.find_all('span',{'class':'result-meta'}):
                            for price in meta.find_all('span',{'class':'result-price'}):
                                resolution['price']=price.text
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
        master=None
        db={}
        dbname='roomResults-cache.db'
        def dbCon(self):
            self.db['db']=sqlite3.connect(self.dbname)
            self.db['cursor']=self.db['db'].cursor()

        #create insert entry
        #create query entry

        def cleanup(self,db):
            db['db'].commit()
            db['db'].close()

    class void:
        master=None

    class run:
        master=None
        def run(self):
            sort=self.master.external.sort
            availability=self.master.external.availability
            minCost=self.master.external.minCost
            zipcode=self.master.external.zipcode

            url=self.master.web.genUrl(sort,availability,minCost,zipcode)
            results=self.master.web.gatherGen(url)
            for result in results:
                print(result)

    def assembler(self):
        self.sort='priceasc'
        self.availability='0'
        self.minCost='600'
        self.zipcode='93933'

        self.wa=self.void()
        self.wa.master=self.wa
        #give access of lower classes to top level class container
        self.wa.external=self

        self.wa.web=self.web()
        self.wa.master=self.wa
        
        self.wa.run=self.run()
        self.wa.run.master=self.wa
        self.wa.run.run()

run=container()
run.assembler()
