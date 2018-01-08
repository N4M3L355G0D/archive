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
            self.varDump("textConfig")
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

    def xmlConfig(self,versionOverride=None):
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
                    self.CD=node.text
                if node.tag == "IMG":
                    self.IMG=node.text
                if node.tag == "IMG_Size":
                    self.IMG_SIZE=node.text
                if node.tag == "CMD":
                    self.CMD=node.text
                if node.tag == "cpu":
                    self.cpu=node.text
                if node.tag == "accel":
                    self.accel=node.text
                if node.tag == "ram":
                    self.ram=node.text
                if node.tag == "cores":
                    self.cores=node.text
                if node.tag == "vga":
                    self.vga=node.text
                if node.tag == "display":
                    self.display=node.text
                if node.tag == "DB":
                    self.DB=node.text
                if node.tag == "name":
                    self.name=node.text
                if node.tag == "nicModel":
                    self.nicModel=node.text
                if node.tag == "soundHW":
                    self.soundHW=node.text
            self.varDump("xmlConfig")
    #need to create sqlite3Config
    #need to create sqlite3ConfigGen
    #need to create selector
    #need to create detector
    #for better info, please see config.sh

cfg=conf()
cfg.textConfig()
cfg.xmlConfig(versionOverride=2)
