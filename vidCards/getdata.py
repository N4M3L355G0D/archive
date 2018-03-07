#! /usr/bin/env python3

from bs4 import BeautifulSoup as bs
import urllib.request
from xml.etree.ElementTree import Element as element, SubElement as subElement, tostring as ts
import sys,os,argparse

#get the webpage data
class nvidiaCardGet:
    common=[ '205','210','gt-240','gts-240-oem-product','gts250','gtx-260','gtx-275','gtx-280','gtx-285','gtx-285-for-mac','gtx-295','310','315-oem','gt-320-oem','gt-330-oem','gt-340-oem','405-oem','gt-430','gt-440-channel','gts-450','gtx-465','gtx-470','510-oem','gt-520-oem','gt-530-oem','gt-545-ddr3','gt-545-oem-gddr5','gtx-550ti','gtx-555-oem','gtx-560-oem','gtx-560-ti-oem','gtx-570','gtx-580','gtx-590','605-oem','gt-620-oem','gt-630-oem','gtx-1070-ti','gtx-1080-ti']
    commonD=['gtx-480','gt-610','gt-620','gt-635-oem','gtx-645-oem','gtx-650','gtx-650ti','gtx-650ti-boost','gtx-660','gtx-660-oem','gtx-660ti','gtx-670','gtx-680','gtx-690','gt-705-oem','gt-710','gt-720','gtx-745-oem','gtx-750','gtx-750-ti','gtx-760','gtx-760-oem','gtx-760ti-oem','gtx-770','gtx-780','gtx-780-ti','gtx-titan-black','gtx-titan-z','gtx-950','gtx-950-oem','gtx-960','gtx-960-oem','gtx-970','gtx-980','gtx-980-ti','gtx-titan-x','gt-1030']
    common10=['gtx-1050','gtx-1060','gtx-1070','gtx-1080']
    url10='https://www.geforce.com/hardware/desktop-gpus/geforce-{}'
    url='https://www.geforce.com/hardware/desktop-gpus/geforce-{}/specifications'
    EXIT_NO_MOD_URL="no model/url provided"
    NOT_SUPPORTED='that particular Nvidia Card Model is not supported!'
    def webpage(self,url):
        data=urllib.request.urlopen(url)
        page=data.read()
        return page
    
    def message(self,model):
        cols=int(os.get_terminal_size().columns*0.3)*'='
        print('{}{}{}'.format(cols,model,cols))
    
    def getGeForce(self,url=None,model='205'):
        self.message(model)
        if url == None:
            exit(self.EXIT_NO_MOD_URL)
        page=self.webpage(url)
        soup=bs(page,'html.parser')
        specdata=soup.find_all('div',{'class':'field-group-format group_specifications_main field-group-div group-specifications-main specifications-main speed-fast effect-none'})[0]
        span=specdata.find_all('span')
        fieldLabels=specdata.find_all('div',{'class':'field-label'})
        fieldItems=specdata.find_all('div',{'class':'field-items'})
        for i in range(len(fieldLabels)):
            print(fieldLabels[i].text,fieldItems[i].text,sep='|')

    def getMulti(self):
        common=self.common
        for model in common:
            self.getGeForce(self.url.format(model),model)

    def getGeForceD(self,url=None,model='gt-610'):
        self.message(model)
        if url == None:
            exit(self.EXIT_NO_MOD_URL)
        page=self.webpage(url)
        soup=bs(page,'html.parser')
        specdata=soup.find('div',{'class':'coloredTable'}).find_all('div',{'class':'row'})
        for i in specdata:
            rowVal=i.find_all('span')[0].text
            rowData=i.text.strip(rowVal)
            print(rowData.replace('\n',''),rowVal,sep='|')
    
    def getMultiD(self):
        common=self.commonD
        for model in common:
            self.getGeForceD(self.url.format(model),model)
    
    def getGeForce1050Plus(self,url=None,model='gtx-1050'):
        self.message(model)
        if url == None:
            exit(self.EXIT_NO_MOD_URL)
        page=self.webpage(url)
        soup=bs(page,'html.parser')
        specdata=soup.find_all('div',{'class':'modal-body specsmodalbody',})[0].find_all('div',{'class':'specsrow'})
        for i in range(len(specdata)):
            left=','.join([x.text for x in specdata[i].find_all('span',{'class':'left'})])
            right=','.join([x.text for x in specdata[i].find_all('span',{'class':'right'})])
            print(left,right,sep='|')

    def getMulti10(self):
        common=self.common10    
        for model in common:
            self.getGeForce1050Plus(self.url10.format(model),model)

    def getAllSupported(self):
        self.getMulti()
        self.getMultiD()
        self.getMulti10()
    def getOne(self,model):
        if model in self.common:
            self.getGeForce(self.url.format(model),model)
        elif model in self.commonD:
            self.getGeForceD(self.url.format(model),model)
        elif model in self.common10:
            self.getGeForce1050Plus(self.url10.format(model),model)
        else:
            exit('"{}" : {}'.format(model,self.NOT_SUPPORTED))

    def listSupported(self):
        total=[]
        total.extend(self.common)
        total.extend(self.commonD)
        total.extend(self.common10)
        self.message('Supported Cards')
        for model in total:
            print("\t - {}".format(model))

    def getHelp(self,options):
        counter=0
        if not options.list_supported:
            counter+=1
        if not options.get_one_card:
            counter+=1
        if not options.get_all_cards:
            counter+=1
        if counter >= 3:
            exit('please see -h/--help')

    def cmdline(self):
        parser=argparse.ArgumentParser()
        parser.add_argument('-l','--list-supported',help='list supported cards',action='store_true')
        parser.add_argument('-1','--get-one-card',help='get one card model\'s specs')
        parser.add_argument('-a','--get-all-cards',help='get all card models',action='store_true')

        options=parser.parse_args()
        if options.list_supported:
            self.listSupported()
        if options.get_one_card:
            self.getOne(options.get_one_card)
        if options.get_all_cards:
            self.getAllSupported()
        self.getHelp(options)

get=nvidiaCardGet()
get.cmdline()
#get.getOne('gtx-680')
#get.getAllSupported()

## To-Do's ##
#titan v, titan Xp need seperate functions
#geforce gtx460,gtx460-se,gtx560ti,gt630,gt640,gt640oem,gt730,gt740, has embedded tables needs special work
#geforce gtx560 has embedded tables that need to be operated on differently
