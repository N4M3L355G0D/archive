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

    def varDump(self,style,suppressHeader=False):
        if suppressHeader == False:
            self.header(style)
        Vars={'CD':self.CD,'IMG':self.IMG,'IMG_SIZE':self.IMG_SIZE,'CMD':self.CMD,'cpu':self.cpu,'accel':self.accel,'ram':self.ram,'cores':self.cores,'vga':self.vga,'display':self.display,'DB':self.DB,'name':self.name,'nicModel':self.nicModel,'soundHW':self.soundHW}
        for i in Vars.keys():
            if Vars[i] != None:
                print(i,Vars[i].rstrip("\n"),sep="#")
            else:
                print(i,"",sep='#')

    def cfgExist(self,cfgStyle):
        for i in self.cnfFiles.keys():
            if i == cfgStyle:
                if os.path.exists(self.cnfFiles[i]):
                    return True
                else:
                    return False
        #if for-loop exits due to unknown format, do a return
        return None

    def textConfig(self,singleX=None):
        fileStatus=self.cfgExist("text")
        if fileStatus == True:
            with open(cnf,"r") as data:
                for i in data:
                    i=i.split("=")
                    if i[0] == "CD":
                        if singleX == None:
                            self.CD=i[1]
                        else:
                            self.CD=i[1]
                            break

                    if i[0] == "IMG":
                        if singleX == None:
                            self.IMG=i[1]
                        else:
                            self.IMG=i[1]
                            break

                    if i[0] == "IMG_Size":
                        if singleX == None:
                            self.IMG_SIZE=i[1]
                        else:
                            self.IMG_SIZE=i[1]
                            break

                    if i[0] == "CMD":
                        if singleX == None:
                            self.CMD=i[1]
                        else:
                            self.CMD=i[1]
                            break

                    if i[0] == "cpu":
                        if singleX == None:
                            self.cpu=i[1]
                        else:
                            self.cpu=i[1]
                            break

                    if i[0] == "accel":
                        if singleX == None:
                            self.accel=i[1]
                        else:
                            self.accel=i[1]
                            break

                    if i[0] == "ram":
                        if singleX == None:
                            self.ram=i[1]
                        else:
                            self.ram=i[1]
                            break

                    if i[0] == "cores":
                        if singleX == None:
                            self.cores=i[1]
                        else:
                            self.cores=i[1]
                            break

                    if i[0] == "vga":
                        if singleX == None:
                            self.vga=i[1]
                        else:
                            self.vga=i[1]
                            break

                    if i[0] == "display":
                        if singleX == None:
                            self.display=i[1]
                        else:
                            self.display=i[1]
                            break

                    if i[0] == "DB":
                        if singleX == None:
                            self.DB=i[1]
                        else:
                            self.DB=i[1]
                            break

                    if i[0] == "name":
                        if singleX == None:
                            self.name=i[1]
                        else:
                            self.name=i[1]
                            break

                    if i[0] == "nicModel":
                        if singleX == None:
                            self.nicModel=i[1]
                        else:
                            self.nicModel=i[1]
                            break

                    if i[0] == "soundHW":
                        if singleX == None:
                            self.soundHW=i[1]
                        else:
                            self.soundHW=i[1]
                            break
        else:
            if fileStatus == False:
                print("textfile:configuration file does not exist")
        return 'text'

    #next function definition set will be for xmlCnf
    def xmlGetLatestConfig(self,root):
        self.latestVersion=0
        #get latest version
        for child in root:
            attr=child.attrib
            if int(attr['num']) > self.latestVersion:
                self.latestVersion=int(child.attrib['num'])

    def xmlConfig(self,versionOverride=None,singleX=None):
        singleNode=singleX
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
            return 'xml'

    def sqlite3GetLatestVersion(self,db=None,cursor=None):
        if db == None and cursor == None:
            self.latestVersion=0
            db=sqlite3.connect(cnfDb)
            cursor=db.cursor()
            sql="select count(version) from "+self.table+";"
            cursor.execute(sql)
            self.latestVersion=cursor.fetchone()[0]
            if self.latestVersion == 0:
                exit("no configuration data")

    def sqlite3GetCol(self,column,db,cursor):
        sql="select "+column+" from "+self.table+" where version="+str(self.latestVersion)+";"
        cursor.execute(sql)
        val=cursor.fetchone()
        if val[0] == None:
            val=''
        else:
            val=val[0]
        return val

    def sqlite3Config(self,versionOverride=None,singleX=None):
        singleCol=singleX
        fileStatus=self.cfgExist("sqlite3")
        if fileStatus == True:
            if versionOverride != None:
                self.sqlite3GetLatestVersion()
                if 0 < versionOverride <= self.latestVersion:
                    self.latestVersion=versionOverride

            db=sqlite3.connect(cnfDb)
            cursor=db.cursor()
            if versionOverride == None:
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


        elif fileStatus == False:
            pass
        return 'sqlite3'

    def sqlite3ConfigGen(self):
        ignores=("version",)
        sqllist=list()
        sqllistData=list()
        tableValsList=list()
        sql=''
        final=''
        tabloid=''
        sqlInsert=''
        idiotCounter=0
        maxIdiotCount=10
        rt="text"
        errEarlyExit='user exited wizard prematurely... nothing will be written!'
        rows={'CD':{'rt':rt,'data':self.CD},'IMG':{'rt':rt,'data':self.IMG},'IMG_SIZE':{'rt':rt,'data':self.IMG_SIZE},'CMD':{'rt':rt,'data':self.CMD},'cpu':{'rt':rt,'data':self.cpu},'accel':{'rt':rt,'data':self.accel},'ram':{'rt':rt,'data':self.ram},'cores':{'rt':rt,'data':self.cores},'vga':{'rt':rt,'data':self.vga},'display':{'rt':rt,'data':self.display},'DB':{'rt':rt,'data':self.DB},'name':{'rt':rt,'data':self.name},'nicModel':{'rt':rt,'data':self.nicModel},'soundHW':{'rt':rt,'data':self.soundHW},'version':{'rt':"INTEGER PRIMARY KEY AUTOINCREMENT",'data':self.latestVersion}}
        while final != "yes":
            counterPrompt=0
            for opt in rows.keys():
                if opt != "version":
                    counterPrompt+=1
                    rows[opt]['data']=str(input(opt+" "+str(counterPrompt)+" : "))
                if rows[opt]['data'] == '#quit':
                    exit(errEarlyExit)
            #print the wizard header
            self.header('sqlite3ConfigGen')
            final=input("is this final? : ")
            if final == "#quit":
                exit(errEarlyExit)
            while final not in ('yes','no','#quit'):
                if idiotCounter < maxIdiotCount:
                    idiotCounter+=1
                    final=input("[ Retry "+str(idiotCounter)+"-"+str(maxIdiotCount)+" ] "+"is this final? [yes/no/#quit] : ")
                    if final == "#quit":
                        exit(errEarlyExit)
                else:
                    print("you apparently do not know how to read, dUm6@55 617Ch!,use 'yes' or 'no' to answer the 3ff1n9 prompt. Restarting wizzzzaaaarrrrrd!")
                    break
        db=sqlite3.connect(cnfDb)
        cursor=db.cursor()

        #create the table sql
        rowsLen=len(rows.keys())-len(ignores)
        for num,i in enumerate(rows.keys()):
            if 0 < num < rowsLen:
                sqllist.append(",")
            sqllist.append(''.join((i," ",rows[i]['rt'])))
        sqlCreateTable="create table if not exists "+self.table+"("+''.join(sqllist)+");"
        #run sql
        cursor.execute(sqlCreateTable)
        #if ignores is len of 1, it throws an err for code that is len of 2+
        if len(ignores) < 2:
                rowsLen=rowsLen-1
        #begin generating values()
        for num,i in enumerate(rows.keys()):
            if i not in ignores:
                if num < rowsLen:
                    if type(rows[i]['data']) == type(str()):
                        sqllistData.append('"'+rows[i]['data']+'",')
                    elif type(rows[i]['data']) == type(int()):
                        sqllistData.append(str(rows[i]['data'])+",")
                else:
                   if type(rows[i]['data']) == type(str()):
                       sqllistData.append('"'+rows[i]['data']+'"')
                   elif type(rows[i]['data']) == type(int()):
                       sqllistData.append(str(rows[i]['data']))
        values="values("+''.join(sqllistData)+");"
        
        #generate table insert string
        for num,i in enumerate(rows.keys()):
            if i not in ignores:
                if num < rowsLen:
                    tableValsList.append(i+",")
                else:
                    tableValsList.append(i)

        tabloid=self.table+"("+''.join(tableValsList)+") "
        sqlInsert="insert into "+tabloid+values
        #execute sqlInsert, now that it is fully generated
        cursor.execute(sqlInsert)
        db.commit()

    def detector(self,style):
        cmds=[i for i in self.cnfFiles.keys()]
        if style not in cmds:
            exit('cmd not available')
                
        cfg={'CD':self.CD,'IMG':self.IMG,'IMG_SIZE':self.IMG_SIZE,'CMD':self.CMD,'cpu':self.cpu,'accel':self.accel,'ram':self.ram,'cores':self.cores,'vga':self.vga,'display':self.display,'DB':self.DB,'name':self.name,'nicModel':self.nicModel,'soundHW':self.soundHW}
        for cf in cfg.keys():
            if cfg[cf] == '':
                #if a blank config is detected, pull config from the next available configuration file
                self.selector(ignore=style,singleXX=cf)

    def selector(self,preferred=None,ignore=None,versionOverridE=None,singleXX=None):
        cnfType=''
        counter=0
        errNoCmdExist='config/cmd file does not exist'
        if preferred != None:
            #use only the desired configuration format
            fileStatus=self.cfgExist(preferred)
            if fileStatus != None:
                if fileStatus == True:
                    if preferred == 'xml':
                        cnfType=self.xmlConfig(versionOverride=versionOverridE,singleX=singleXX)
                    elif preferred == 'sqlite3':
                        cnfType=self.sqlite3Config(versionOverride=versionOverridE,singleX=singleXX)
                    elif preferred == 'text':
                        cnfType=self.textConfig(singleX=singleXX)
                else:
                    print(errNoCmdExist)
                    exit(1)
            else:
                counter+=1
                        
        elif ignore != None:
            #ignore specified configuration file and choose from one of the other two format
            for cnf in self.cnfFiles.keys():
                if cnf != ignore:
                    fileStatus=self.cfgExist(cnf)
                    if fileStatus != None:
                        if cnf == 'xml' and fileStatus == True:
                            cnfType=self.xmlConfig(versionOverride=versionOverridE,singleX=singleXX)
                            break
                        elif cnf == 'sqlite3' and fileStatus == True:
                            cnfType=self.sqlite3Config(versionOverride=versionOverridE,singleX=singleXX)
                            break
                        elif cnf == 'text' and fileStatus == True:
                            cnfType=self.textConfig(singleX=singleXX)
                            break
                        else:
                            print(errNoCmdExist)
                            exit(1)
                    else:
                        counter+=1
        else:
            #autoselector
            for cnf in self.cnfFiles.keys():
                fileStatus=self.cfgExist(cnf)
                if fileStatus != None:
                    if cnf == 'xml' and fileStatus == True:
                        cnfType=self.xmlConfig(versionOverride=versionOverridE)
                        break
                    elif cnf == 'sqlite3' and fileStatus == True:
                        cnfType=self.sqlite3Config(versionOverride=versionOverridE)
                        break
                    elif cnf == 'text' and fileStatus == True:
                        cnfType=self.textConfig(singleX=singleXX)
                        break
                    else:
                        print(errNoCmdExist)
                        exit(1)
                else:
                    counter+=1
        if counter == len(self.cnfFiles.keys()):
            exit("no configuration files")
        else:
            return cnfType
            
    #need to create selector [selector needs to be created first
    #     need ignore conf - to choose from anything but the specified ignore
    #     need prefer conf - to use only the specified conf
    #need to create detector [detector is next]
    #for better info, please see config.sh

cfg=conf()
#cfg.textConfig()

#get individual cfg cols for sqlite3
#cfg.sqlite3Config(singleCol='soundHW')
#cfg.sqlite3Config(singleCol="CD")

# for xml and sqlite3 configuration options: 
#if versionOverride is out of range, it will default to using the latest configuration
#cfg.sqlite3Config(versionOverride=1)

#cfg.sqlite3ConfigGen()
#cfg.sqlite3Config(versionOverride=1)

#get individual elements for xml 
#cfg.xmlConfig(versionOverride=2,singleNode="CD")
#cfg.xmlConfig(versionOverride=2,singleNode="IMG_Size")

#versionOverridE applies to xml and sqlite3 formats
#singleXX applies to all formats
Format="sqlite3"
stile=cfg.selector(preferred='sqlite3')
cfg.detector(stile)
cfg.varDump(stile+'Config',suppressHeader=True)
