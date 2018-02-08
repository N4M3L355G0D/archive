#! /usr/bin/env python3

import pyalpm
import argparse
from xml.etree.ElementTree import Element as element, SubElement as subelement, tostring as ts
def getDb():
    h=pyalpm.Handle('/','/var/lib/pacman')
    dbs='core:community:extra'
    dbs=dbs.split(":")
    db = {'core':h.register_syncdb("core", pyalpm.SIG_DATABASE_OPTIONAL),'extra':h.register_syncdb("extra", pyalpm.SIG_DATABASE_OPTIONAL),'community':h.register_syncdb("community", pyalpm.SIG_DATABASE_OPTIONAL)}
    sync=h.get_syncdbs()
    return [db,dbs]

def getDepends(DB,pkg):
    db=DB[0]
    dbs=DB[1]
    deps=[]
    for i in dbs:
        pk=db[i].get_pkg(pkg)
        if pk != None:
            deps=pk.depends
    return deps

def getOptDepends(DB,pkg):
    db=DB[0]
    dbs=DB[1]
    deps=[]
    depsMod=[]
    for i in dbs:
        pk=db[i].get_pkg(pkg)
        if pk != None:
            deps=pk.depends
            for j in deps:
                j=j.split(":")[0]
                depsMod.append(j)
    return depsMod

def getOptionalDeps(db,pkg=''):
    final=[]
    total=[pkg,]
    commons=0
    counter=0
    for pk in total:
        counter+=1
        #print(pk,1)
        deps=getOptDepends(db,pk)
        depsTmp=[]
        for i in deps:
            total.extend(getOptDepends(db,pkg))
        deps=[]
        #print(pk,2)
        #exit init
        for i in total:
            tmp=getDepends(db,i)
            if tmp != []:
                deps.extend(tmp)
        total=[]
        #print(pk,3)
        for i in deps:
            if i not in total:
                #print("\t{}:{}:{}:{}:{}".format(pk,commons,len(total),len(deps),i))
                final.append(i)
                total.append(i)
            else:
                commons+=1
    final=sorted(set(final))
    #total.extend(deps)
    return final

def getRequiredDeps(db,pkg=''):
    final=[]
    total=[pkg,]
    commons=0
    counter=0
    for pk in total:
        counter+=1
        #print(pk,1)
        deps=getDepends(db,pk)
        depsTmp=[]
        for i in deps:
            total.extend(getDepends(db,pkg))
        deps=[]
        #print(pk,2)
        #exit init
        for i in total:
            tmp=getDepends(db,i)
            if tmp != []:
                deps.extend(tmp)
        total=[]
        #print(pk,3)
        for i in deps:
            if i not in total:
                #print("\t{}:{}:{}:{}:{}".format(pk,commons,len(total),len(deps),i))
                final.append(i)
                total.append(i)
            else:
                commons+=1
    final=sorted(set(final))
    #total.extend(deps)
    return final

db=getDb()
def mainPrime(db,pkg):
    c=[]
    b=[]
    a=getRequiredDeps(db,'k3b')
    total=[]
    for i in a:
        if i not in total:
            total.append(i)
            #print('!',i)
        b=getOptionalDeps(db,i)
        for j in b:
            if j not in total:
                total.append(j)
                #print('@',j)
            c=getRequiredDeps(db,j)
            for k in c:
                if k not in total:
                    total.append(k)
                    #print('#',k)
    return sorted(set(total))

def cmdline():
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--package",required='yes')
    options=parser.parse_args()
    return options

def xmlDump(data,package):
    top=element("pkg",{'name':package})
    for num,i in enumerate(data):
        dep=subelement(top,'dep',{'num':str(num),'name':str(i)})
        dep.text=i
    return ts(top).decode()

#need conflict resolution to display conflicting files
#need a function to gather conflicts from mainPrime's returned list
##that can be called within xmlDump to to modify data structure to display conflicts
cmd=cmdline()
a=mainPrime(db,cmd.package)
data=xmlDump(a,cmd.package)
print(data)
