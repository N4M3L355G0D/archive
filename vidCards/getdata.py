#! /usr/bin/env python3

from bs4 import BeautifulSoup as bs
import urllib.request
from xml.etree.ElementTree import Element as element, SubElement as subElement, tostring as ts
import sys,os

#get the webpage data
def webpage(url):
    data=urllib.request.urlopen(url)
    page=data.read()
    return page

def message(model):
    cols=int(os.get_terminal_size().columns*0.3)*'='
    print('{}{}{}'.format(cols,model,cols))

def getGTX950Specs():
    print('Geforce GTX 950')
    url='https://www.geforce.com/hardware/desktop-gpus/geforce-gtx-950/specifications'
    page=webpage(url) 
    #get the desired data
    soup=bs(page,'html.parser')
    specdata=soup.find('div',{'class':'coloredTable'}).find_all('div',{'class':'row'})
    for i in specdata:
        rowVal=i.find_all('span')[0].text
        rowData=i.text.strip(rowVal)
        print(rowData,rowVal,sep='|')

def getGeForce(url=None,model='205'):
    message(model)
    if url == None:
        url='https://www.geforce.com/hardware/desktop-gpus/geforce-205/specifications'
    page=webpage(url)
    soup=bs(page,'html.parser')
    specdata=soup.find_all('div',{'class':'field-group-format group_specifications_main field-group-div group-specifications-main specifications-main speed-fast effect-none'})[0]
    span=specdata.find_all('span')
    fieldLabels=specdata.find_all('div',{'class':'field-label'})
    fieldItems=specdata.find_all('div',{'class':'field-items'})
    for i in range(len(fieldLabels)):
        print(fieldLabels[i].text,fieldItems[i].text,sep='|')

def getMulti():
    common=[ '205','210','gt-240','gts-240-oem-product','gts250','gtx-260','gtx-275','gtx-280','gtx-285','gtx-285-for-mac','gtx-295','310','315-oem','gt-320-oem','gt-330-oem','gt-340-oem','405-oem','gt-430','gt-440-channel','gts-450','gtx-465','gtx-470']
    for model in common:
        getGeForce('https://www.geforce.com/hardware/desktop-gpus/geforce-{}/specifications'.format(model),model)

getMulti()

#geforce gtx460,geforce gtx460-se has embedded tables needs special work
#geforce gtx480 has different code than then what getGeForce() looks for need special code for this one
#def getGF210()

#getGTX950Specs()
