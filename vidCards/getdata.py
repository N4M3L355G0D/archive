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
    common=[ '205','210','gt-240','gts-240-oem-product','gts250','gtx-260','gtx-275','gtx-280','gtx-285','gtx-285-for-mac','gtx-295','310','315-oem','gt-320-oem','gt-330-oem','gt-340-oem','405-oem','gt-430','gt-440-channel','gts-450','gtx-465','gtx-470','510-oem','gt-520-oem','gt-530-oem','gt-545-ddr3','gt-545-oem-gddr5','gtx-550ti','gtx-555-oem','gtx-560-oem','gtx-560-ti-oem','gtx-570','gtx-580','gtx-590','605-oem','gt-620-oem','gt-630-oem']
    for model in common:
        getGeForce('https://www.geforce.com/hardware/desktop-gpus/geforce-{}/specifications'.format(model),model)

getMulti()

def getGeForceD(url=None,model='gt-610'):
    message(model)
    if url == None:
        url='https://www.geforce.com/hardware/desktop-gpus/geforce-gt-610/specifications'
    page=webpage(url)
    soup=bs(page,'html.parser')
    specdata=soup.find('div',{'class':'coloredTable'}).find_all('div',{'class':'row'})
    for i in specdata:
        rowVal=i.find_all('span')[0].text
        rowData=i.text.strip(rowVal)
        print(rowData,rowVal,sep='|')
def getMultiD():
    common=['gt-610','gt-620','gt-635-oem','gtx-645-oem','gtx-650','gtx-650ti','gtx-650ti-boost','gtx-660','gtx-660-oem','gtx-660ti','gtx-670','gtx-680','gtx-690']
    for model in common:
        getGeForceD('https://www.geforce.com/hardware/desktop-gpus/geforce-{}/specifications'.format(model),model)

getMultiD()
#geforce gtx460,gtx460-se,gtx560ti,gt630,gt640,gt640oem, has embedded tables needs special work
#geforce gtx480 has different code than then what getGeForce() looks for need special code for this one
#geforce gtx560 has embedded tables that need to be operated on differently
#geforece,gt610,gt620 has different code than what is supported by getGeforce() need different code

#getGTX950Specs()
