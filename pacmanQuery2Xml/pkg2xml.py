#! /usr/bin/env python3
#NoGuiLinux

import pyalpm, time
from xml.etree.ElementTree import Element as element, SubElement as subElement, tostring

class pac2xml:
    top=element("pkg",name="vim")
    package="vim"
    def setup(self):
        pkg=self.package
            
        databaseDir="/var/lib/pacman"
        handle=pyalpm.Handle('/',databaseDir)
        db=handle.get_localdb()
        
        pkG=db.get_pkg(pkg)
        return pkG

    def optDeps(self,pkg):
        opts=subElement(self.top,"optional_deps")
        for num,i in enumerate(pkg.optdepends):
            deps=subElement(opts,"dep",num=str(num))
            data=i.split(": ")[0]
            deps.text=data

    def deps(self,pkg):
        dep=subElement(self.top,"required_deps")
        for num, i in enumerate(pkg.depends):
            data=i.split(": ")[0]
            depend=subElement(dep,"dep",num=str(num))
            depend.text=data

    def requiredBy(self,pkg):
        needed=pkg.compute_requiredby()
        if needed != []:
            required_by=subElement(self.top,"required_by")
            for num,i in needed:
                required=subElement(required_by,"master",num=str(num))   
                required.text=i
    
    def conflicts(self,pkg):
        if pkg.conflicts != []:
            conflicts=subElement(self.top,"conflicts")
            for num,i in enumerate(pkg.conflicts):
                conflict=subElement(conflicts,"conflict",num=str(num))
                conflict.text=i

    def Pdetails(self,pkg):
        details={}
        details['name']=pkg.name
        details['version']=pkg.version
        details['desc']=pkg.desc
        details['arch']=pkg.arch
        details['url']=pkg.url
        details['isize']=pkg.isize
        details['size']=pkg.size
        details['download_size']=pkg.download_size
        details['install_script']=pkg.has_scriptlet
        singles=subElement(self.top,"misc")
        for detail in details.keys():
            child=subElement(singles,detail)
            child.text=str(details[detail])
    
    def backup(self,pkg):
        backs=pkg.backup
        if backs != []:
            bu=subElement(self.top,"backups")
            for num,i in enumerate(backs):
                bwu=subElement(bu,"backup",num=str(num))
                bwu.text=i
    
    def dates(self,pkg):
        times={}
        times['builddate']=time.ctime(pkg.builddate)
        times['installdate']=time.ctime(pkg.installdate)
        Dates=subElement(self.top,"dates")
        for date in times.keys():
            DatesChild=subElement(Dates,date)
            DatesChild.text=times[date]
    
    def files(self,pkg):
        Files=subElement(self.top,"files")
        for num,i in enumerate(pkg.files):
            fname=subElement(Files,"fname",num=str(num))
            fname.text=i[0]
        if pkg.filename != None:
            filename=subElement(Files,"filename")
            filename.text=pkg.filename
    
    def groups(self,pkg):
        Groups=pkg.groups
        if Groups != []:
            g=subElement(self.top,"groups")
            for num,i in Groups:
                gg=subElement(g,"group",num=str(num))
                gg.text=i

    def checksumsAndSigs(self,pkg):
        checkSums=subElement(self.top,"check_sums")
        if pkg.md5sum != None:
            checkSumsChild=subElement(checkSums,"md5sum")
            checkSumsChild=pkg.md5sum
        if pkg.sha256sum != None:
            checkSumsChild=subElement(checkSums,"sha256sum")
            checkSumsChild.text=pkg.sha256sum
        if pkg.base64_sig != None:
            checkSumsChild=subElement(checkSums,'base64_sig')
            checkSumsChild.text=pkg.base64_sig
        checkSumsChild=subElement(checkSums,"packager")
        checkSumsChild.text=pkg.packager

    def replaces(self,pkg):
        if pkg.replaces != []:
            replace=subElement(self.top,"replaces")
            for num,i in enumerate(pkg.replaces):
                replaceChild=subElement(replace,"replacement",num=str(num))
                replaceChild.text=i

    def reasons(self,pkg):
        reason=subElement(self.top,"reason")
        if pkg.reason == pyalpm.PKG_REASON_DEPEND:
            reason.text="depend"
        elif pkg.reason == pyalpm.PKG_REASON_EXPLICIT:
            reason.text="explicit"
    
    def provides(self,pkg):
        if pkg.provides != []:
           provide=subElement(self.top,"provides")
           for num,i in enumerate(pkg.provides):
               provided=subElement(provide,"provided",num=str(num))
               provided.text=i
    def allDump(self):    
        pkg=self.setup()
        self.optDeps(pkg)
        self.deps(pkg)
        self.requiredBy(pkg)
        self.conflicts(pkg)
        self.Pdetails(pkg)
        self.backup(pkg)
        self.dates(pkg)
        self.files(pkg)
        self.groups(pkg)
        self.checksumsAndSigs(pkg)
        self.replaces(pkg)
        self.reasons(pkg)
        self.provides(pkg)
        print(tostring(self.top).decode())

    def cmdline(self):
        true="store_true"
        parser=argparse.ArgumentParser()
        parser.add_argument('-p','--package')
        parser.add_argument('-o','--opt-deps',action=true)
        parser.add_argument('-d','--depends',action=true)
        parser.add_argument('-r','--required_by',action=true)
        parser.add_argument('-c','--conflicts',action=true)
        parser.add_argument('-m','--details',action=true)
        parser.add_argument('-b','--backup',action=true)
        parser.add_argument('-d','--dates',action=true)
        parser.add_argument('-f','--files',action=true)
        parser.add_argument('-g','--groups',action=true)
        parser.add_argument('-k','--checkSumsAndSigs',action=true)
        parser.add_argument('-R','--replaces',action=true)
        parser.add_argument('-e','--reason',action=true)
        parser.add_argument('-p','--provides',action=true)


data=pac2xml()
data.allDump()
