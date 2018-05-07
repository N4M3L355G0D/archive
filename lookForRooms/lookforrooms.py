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
zipcode='93393'

url='''https://monterey.craigslist.org/search/roo?sort={}&availabilityMode={}&min_price={}&postal={}'''.format(
        urllib.parse.quote(sort),
        urllib.parse.quote(availability),
        urllib.parse.quote(minCost),
        urllib.parse.quote(zipcode)
        )
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
        print(resolution)
except urllib.error.HTTPError as e:
    print(str(e))
except OSError as e:
    print(str(e))
