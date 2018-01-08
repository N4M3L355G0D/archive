#! /usr/bin/env python3
import sqlite3
import os
import xml.etree.ElementTree as ET

#NoGuiLinux
#equivalent of config.sh
cnfError="configuration error: option is blank"
cnfDb="useable-qemu_cnf.db"
cnf="useable-qemu.cnf"
xmlCnf="useable-qemu_cnf.xml"
class conf:
    def __init__(self):
        pass
    #globals
    cnfFiles={'xml':xmlCnf,'sqlite3':cnfDb,'text':cnf}
    version=''
    CD=''
    IMG=''
    IMG_SIZE=''
    CMD=''
    cpu=''
    accel=''
    ram=''
    cores=''
    vga=''
    display=''
    DB=''
    name=''
    nicModel=''
    soundHW=''
    latestVersion=0
    table='qemuCnf'

    def header(self,string):
         print("-->"+string+"<--")

    def varDump(self,style):
        self.header(style)
        Vars={'CD':self.CD,'IMG':self.IMG,'IMG_SIZE':self.IMG_SIZE,'CMD':self.CMD,'cpu':self.cpu,'accel':self.accel,'ram':self.ram,'cores':self.cores,'vga':self.vga,'display':self.display,'DB':self.DB,'name':self.name,'nicModel':self.nicModel,'soundHW':self.soundHW}
        for i in Vars.keys():
            print(i,Vars[i].rstrip("\n"),sep="#")

    def cfgExist(self,cfgStyle):
        for i in self.cnfFiles.keys():
            if i == cfgStyle:
                if os.path.exists(self.cnfFiles[i]):
                    return True
                else:
                    return False
        #if for-loop exits due to unknown format, do a return
        return None

    def textConfig(self):
        fileStatus=self.cfgExist("text")
        if fileStatus == True:
            with open(cnf,"r") as data:
                for i in data:
                    i=i.split("=")
                    if i[0] == "CD":
                        self.CD=i[1]
                    if i[0] == "IMG":
                        self.IMG=i[1]
                    if i[0] == "IMG_Size":
                        self.IMG_SIZE=i[1]
                    if i[0] == "CMD":
                        self.CMD=i[1]
                    if i[0] == "cpu":
                        self.cpu=i[1]
                    if i[0] == "accel":
                        self.accel=i[1]
                    if i[0] == "ram":
                        self.ram=i[1]
                    if i[0] == "cores":
                        self.cores=i[1]
                    if i[0] == "vga":
                        self.vga=i[1]
                    if i[0] == "display":
                        self.display=i[1]
                    if i[0] == "DB":
                        self.DB=i[1]
                    if i[0] == "name":
                        self.name=i[1]
                    if i[0] == "nicModel":
                        self.nicModel=i[1]
                    if i[0] == "soundHW":
                        self.soundHW=i[1]
            #self.varDump("textConfig")
        else:
            if fileStatus == False:
                print("textfile:configuration file does not exist")
    #next function definition set will be for xmlCnf
    def xmlGetLatestConfig(self,root):
        self.latestVersion=0
        #get latest version
        for child in root:
            attr=child.attrib
            if int(attr['num']) > self.latestVersion:
                self.latestVersion=int(child.attrib['num'])

    def xmlConfig(self,versionOverride=None,singleNode=None):
        #need version override
        fileStatus=self.cfgExist('xml')
        if fileStatus == True:
            tree=ET.parse(xmlCnf)
            root=tree.getroot()
            if versionOverride != None:
                self.xmlGetLatestConfig(root)
                if 0 < versionOverride < self.latestVersion:
                    self.latestVersion=versionOverride
                    #might do an else to warn that override will not be used
            else:
                self.xmlGetLatestConfig(root)                   
            #use latest version
            child=root[self.latestVersion-1]
            for node in child:
                if node.tag == "CD":
                    if singleNode == None:
                        self.CD=node.text
                    elif singleNode == "CD":
                        self.CD=node.text
                        break

                if node.tag == "IMG":
                    if singleNode == None:
                        self.IMG=node.text
                    elif singleNode == "IMG":
                        self.IMG=node.text
                        break

                if node.tag == "IMG_Size":
                    if singleNode == None:
                        self.IMG_SIZE=node.text
                    elif singleNode == "IMG_Size":
                        self.IMG_SIZE=node.text
                        break

                if node.tag == "CMD":
                    if singleNode == None:
                        self.CMD=node.text
                    elif singleNode == "CMD":
                        self.CMD=node.text
                        break

                if node.tag == "cpu":
                    if singleNode == None:
                        self.cpu=node.text
                    elif singleNode == "cpu":
                        self.cpu=node.text
                        break

                if node.tag == "accel":
                    if singleNode == None:
                        self.accel=node.text
                    elif singleNode == "accel":
                        self.accel=node.text
                        break

                if node.tag == "ram":
                    if singleNode == None:
                        self.ram=node.text
                    elif singleNode == "ram":
                        self.ram=node.text
                        break

                if node.tag == "cores":
                    if singleNode == None:
                        self.cores=node.text
                    elif singleNode == "cores":
                        self.cores=node.text
                        break

                if node.tag == "vga":
                    if singleNode == None:
                        self.vga=node.text
                    elif singleNode == "vga":
                        self.vga=node.text
                        break

                if node.tag == "display":
                    if singleNode == None:
                        self.display=node.text
                    elif singleNode == "display":
                        self.display=node.text
                        break

                if node.tag == "DB":
                    if singleNode == None:
                        self.DB=node.text
                    elif singleNode == "DB":
                        self.DB=node.text
                        break

                if node.tag == "name":
                    if singleNode == None:
                        self.name=node.text
                    elif singleNode == "name":
                        self.name=node.text
                        break

                if node.tag == "nicModel":
                    if singleNode == None:
                        self.nicModel=node.text
                    elif singleNode == "nicModel":
                        self.nicModel=node.text
                        break

                if node.tag == "soundHW":
                    if singleNode == None:
                        self.soundHW=node.text
                    elif singleNode == "soundHW":
                        self.soundHW=node.text
                        break
            #if singleNode == None:
            #self.varDump("xmlConfig")

    def sqlite3GetLatestVersion(self,db=None,cursor=None):
        if db == None and cursor == None:
            self.latestVersion=0
            db=sqlite3.connect(cnfDb)
            cursor=db.cursor()
            sql="select count(version) from "+self.table+";"
            cursor.execute(sql)
            self.latestVersion=cursor.fetchone()[0]
            if self.latestVersion == None:
                self.latestVersion=0
    def sqlite3GetCol(self,column,db,cursor):
        sql="select "+column+" from "+self.table+" where version="+str(self.latestVersion)+";"
        cursor.execute(sql)
        val=cursor.fetchone()[0]
        return val

    def sqlite3Config(self,versionOverride=None,singleCol=None):
        fileStatus=self.cfgExist("sqlite3")
        if fileStatus == True:
            if versionOverride != None:
                self.sqlite3GetLatestVersion()
                if 0 < versionOverride <= self.latestVersion:
                    self.latestVersion=versionOverride

            db=sqlite3.connect(cnfDb)
            cursor=db.cursor()
            self.sqlite3GetLatestVersion()

            if singleCol == None:
                self.CD=self.sqlite3GetCol('CD',db,cursor)
            elif singleCol == "CD":
                self.CD=self.sqlite3GetCol("CD",db,cursor)

            if singleCol == None:
                self.IMG=self.sqlite3GetCol('IMG',db,cursor)
            elif singleCol == "IMG":
                self.IMG=self.sqlite3GetCol('IMG',db,cursor)

            if singleCol == None:
                self.IMG_SIZE=self.sqlite3GetCol('IMG_SIZE',db,cursor)
            elif singleCol == 'IMG_SIZE':
                self.IMG_SIZE=self.sqlite3GetCol('IMG_SIZE',db,cursor)

            if singleCol == None:
                self.CMD=self.sqlite3GetCol('CMD',db,cursor)
            elif singleCol == "CMD":
                self.CMD=self.sqlite3GetCol('CMD',db,cursor)

            if singleCol == None:
                self.cpu=self.sqlite3GetCol('cpu',db,cursor)
            elif singleCol == "cpu":
                self.cpu=self.sqlite3GetCol('cpu',db,cursor)

            if singleCol == None:
                self.accel=self.sqlite3GetCol('accel',db,cursor)
            elif singleCol == "accel":
                self.accel=self.sqlite3GetCol('accel',db,cursor)

            if singleCol == None:
                self.ram=self.sqlite3GetCol('ram',db,cursor)
            elif singleCol == "ram":
                self.ram=self.sqlite3GetCol('ram',db,cursor)

            if singleCol == None:
                self.cores=self.sqlite3GetCol('cores',db,cursor)
            elif singleCol == "cores":
                self.cores=self.sqlite3GetCol('cores',db,cursor)

            if singleCol == None:
                self.vga=self.sqlite3GetCol('vga',db,cursor)
            elif singleCol == "vga":
                self.vga=self.sqlite3GetCol('vga',db,cursor)

            if singleCol == None:
                self.display=self.sqlite3GetCol('display',db,cursor)
            elif singleCol == "display":
                self.display=self.sqlite3GetCol('display',db,cursor)

            if singleCol == None:
                self.DB=self.sqlite3GetCol('DB',db,cursor)
            elif singleCol == "DB":
                self.DB=self.sqlite3GetCol('DB',db,cursor)

            if singleCol == None:
                self.name=self.sqlite3GetCol('name',db,cursor)
            elif singleCol == "name":
                self.name=self.sqlite3GetCol('name',db,cursor)

            if singleCol == None:
                self.nicModel=self.sqlite3GetCol('nicModel',db,cursor)
            elif singleCol == "nicModel":
                self.nicModel=self.sqlite3GetCol('nicModel',db,cursor)

            if singleCol == None:
                self.soundHW=self.sqlite3GetCol('soundHW',db,cursor)
            elif singleCol == "soundHW":
                self.soundHW=self.sqlite3GetCol('soundHW',db,cursor)

            #self.varDump('sqlite3')
        elif fileStatus == False:
            pass
    #modify sqlite3Config with versionOverride
    #      modified to get individual config options
    #      modified self.sqlite3ConfigGen() with versionOverride
    #need to create sqlite3ConfigGen 
    #need to create selector
    #need to create detector
    #for better info, please see config.sh

cfg=conf()
#cfg.textConfig()
stile="sqlite3"

#get individual cfg cols for sqlite3
#cfg.sqlite3Config(singleCol='soundHW')
#cfg.sqlite3Config(singleCol="CD")
# for xml and sqlite3 configuration options: 
#if versionOverride is out of range, it will default to using the latest configuration
#cfg.sqlite3Config(versionOverride=1)

#get individual elements for xml 
#cfg.xmlConfig(versionOverride=2,singleNode="CD")
#cfg.xmlConfig(versionOverride=2,singleNode="IMG_Size")
cfg.varDump(stile+'Config')

