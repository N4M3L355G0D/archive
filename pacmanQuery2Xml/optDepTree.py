#! /usr/bin/env python3
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element as element,SubElement as subelement,tostring
import pyalpm

class optDepTree:
    pkg='vlc'
    pkgs=[]
    top=element('pkg',pname=pkg)
    counter=0
    def main(self,pk='',mode='opt',oType='xml'):
        h=pyalpm.Handle('/','/var/lib/pacman')
        dbs='core:community:extra'
        dbs=dbs.split(":")
        db = {'core':h.register_syncdb("core", pyalpm.SIG_DATABASE_OPTIONAL),'extra':h.register_syncdb("extra", pyalpm.SIG_DATABASE_OPTIONAL),'community':h.register_syncdb("community", pyalpm.SIG_DATABASE_OPTIONAL)}
        sync=h.get_syncdbs()
        fail=0
        for i in dbs:
            if fail < 3:
                pkg=db[i].get_pkg(pk)
                if pkg != None:
                    if mode == 'opt':
                        for x in pkg.optdepends:
                            if x not in self.pkgs:
                                x=x.split(":")[0]
                                if oType == 'xml':
                                    optDep=subelement(self.top,'optional_dependency',num=str(self.counter))
                                    optDep.text=x
                                elif oType == 'text':
                                    self.pkgs.append(x)
                                print(x)
                                self.counter+=1
                                self.main(x,mode=mode,oType=oType)
                    elif mode == 'req':
                        for x in pkg.depends:
                            if x not in self.pkgs:
                                x=x.split(":")[0]
                                if oType == 'xml':
                                    optDep=subelement(self.top,'optional_dependency',num=str(self.counter))
                                    optDep.text=x
                                elif oType == 'text':
                                    self.pkgs.append(x)
                                print(x)
                                self.counter+=1
                                self.main(x,mode=mode,oType=oType)
                else:
                    fail+=1
            else:
                return 0

a=optDepTree()
a.pkg='vlc'
a.main(a.pkg,mode='req',oType='text')
print(tostring(a.top).decode())
