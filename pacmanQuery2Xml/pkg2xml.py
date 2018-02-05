#! /usr/bin/env python3
#NoGuiLinux

import pyalpm
from xml.etree.ElementTree import Element as element, SubElement as subElement, tostring

top=element("pkg",name="vim")

def setup():
    pkg='vim'
        
    databaseDir="/var/lib/pacman"
    handle=pyalpm.Handle('/',databaseDir)
    db=handle.get_localdb()
    
    pkG=db.get_pkg(pkg)
    return pkG

def optDeps(pkg):
    opts=subElement(top,"optional_deps")
    for num,i in enumerate(pkg.optdepends):
        deps=subElement(opts,"dep",num=str(num))
        data=i.split(": ")[0]
        #print(data)
        deps.text=data
def deps(pkg):
    dep=subElement(top,"required_deps")
    for num, i in enumerate(pkg.depends):
        data=i.split(": ")[0]
        depend=subElement(dep,"dep",num=str(num))
        depend.text=data

def requiredBy(pkg):
    needed=pkg.compute_requiredby()
    if needed != []:
        required_by=subElement(top,"required_by")
        for num,i in needed:
            required=subElement(required_by,"master",num=str(num))   
            required.text=i

def conflicts(pkg):
    if pkg.conflicts != []:
        conflicts=subElement(top,"conflicts")
        for num,i in enumerate(pkg.conflicts):
            conflict=subElement(conflicts,"conflict",num=str(num))
            conflict.text=i
def Pdetails(pkg):
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
    singles=subElement(top,"misc")
    for detail in details.keys():
        child=subElement(singles,detail)
        child.text=str(details[detail])


pkg=setup()
optDeps(pkg)
deps(pkg)
requiredBy(pkg)
conflicts(pkg)
Pdetails(pkg)
print(tostring(top).decode())
