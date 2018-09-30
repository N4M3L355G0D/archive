#! /usr/bin/env python3
#NoGuiLinux
import os,gzip,base64,argparse
import xml.etree.ElementTree as ET

class resume:
    xmlFile="resume.xml"
    data=""
    def dataContainerDump(self):
        data=self.data       
        file=open(self.xmlFile,'wb')
        xmlData=gzip.decompress(base64.b64decode(data.encode()))
        file.write(xmlData)
        file.close()

    def rootSet(self):
        if not os.path.exists(self.xmlFile):
            self.dataContainerDump()
        tree=ET.parse(self.xmlFile)
        root=tree.getroot()
        return root

    def banner(self,header=''):
        return '-'*len(header)*2+'\n'+' '*int(len(header)/2)+header+'\n'+'-'*len(header)*2
    
    def education(self,i):
        print(self.banner("Education"))
        for x in i:
            data=x.text.replace("\t","")
            if x.tag == "degree":
                print("\t\t- "+data)
            else:
                print("\t",x.text)
    
    def workXP(self,i):
        print(self.banner("Work Experience"))
        for x in i:
            data=x.text.replace("\t","") 
            for z in x:
                dataZ=z.text.replace("\t","")
                if z.tag == "desc":
                    desc=[d for d in dataZ.split("\n")]
                    for j in desc:
                        print("\t\t- "+j)
                else:
                    print("\t"+dataZ)

    def contact(self,i):
        print(self.banner(i.tag))
        for x in i:
            data=x.text.replace("\t","")
            if x.tag == "phone":
                print("\tPhone [{}]:".format(x.attrib['num']),data)
            elif x.tag == "name":
                print("\tName:",data)
            elif x.tag == "email":
                print("\tEmail [{}]:".format(x.attrib['num']),data)
            elif x.tag == "link":
                print("\tLink [{}]:".format(x.attrib['num']),data)
    def skills(self,i):
        print(self.banner(i.tag))
        skills=[x for x in i.text.replace("\t","").split("\n")]
        for j in skills:
            print("\t- "+j)
    
    def certs(self,i):
        print(self.banner(i.tag))
        for x in i:
            for z in x:
                data=z.text.replace("\t","")
                if z.tag == "name":
                    print("\t"+data)
                elif z.tag == "date":
                    print("\t"+data)
                elif z.tag == "desc":
                    text=[d for d in data.split("\n")]
                    for j in text:
                        print("\t\t- "+j)

    def dataParse(self,root,section=None):
        for i in root:
            if i.tag =="education":
                if section == "education":
                    self.education(i)
                elif section == None:
                    self.education(i)
            elif i.tag == "workXP":
                if section == "workXP":
                    self.workXP(i) 
                elif section == None:
                    self.workXP(i)
            elif i.tag == "skills":
                if section == "skills":
                    self.skills(i)
                elif section == None:
                    self.skills(i)
            elif i.tag == "contact":
                if section == "contact":
                    self.contact(i)
                elif section == None:
                    self.contact(i)
            elif i.tag == "certs":
                if section == "certs":
                    self.certs(i)
                elif section == None:
                    self.certs(i)

    def cmdline(self):
        parser=argparse.ArgumentParser()
        parser.add_argument("-r","--resume",action="store_true")
        parser.add_argument("-s","--skills",action="store_true")
        parser.add_argument("-e","--education",action="store_true")
        parser.add_argument("-w","--workXP",action="store_true")
        parser.add_argument("-c","--certifications",action="store_true")
        parser.add_argument("-C","--contact",action="store_true")
    
        options=parser.parse_args()
        return options

    def main(self):
        root=self.rootSet()
        options=self.cmdline()
        noFail=[]

        if options.skills == False:
            noFail.append(False)
        if options.education == False:
            noFail.append(False)
        if options.workXP == False:
            noFail.append(False)
        if options.certifications == False:
            noFail.append(False)
        if options.contact == False:
            noFail.append(False)
        if options.resume == False:
            noFail.append(False)

        if len(noFail) < 6:
            if options.resume:
                self.dataParse(root)
            else:
                if options.skills:
                    self.dataParse(root,"skills")
                if options.education:
                    self.dataParse(root,"education")
                if options.workXP:
                    self.dataParse(root,"workXP")
                if options.certifications:
                    self.dataParse(root,"certs")
                if options.contact:
                    self.dataParse(root,"contact")
            os.remove(self.xmlFile)
        else:
            exit("please see -h/--help")
resumE=resume()
#resume data
#data is equivalent to `cat data.xml | gzip - -f | base64 -` 
#where data.xml is a edited version of the resume.xml.template

resumE.data="""
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
R5OZjXGn3/R5/b9f/gs4PVc4iBkAAA==
"""
resumE.main()
