#! /usr/bin/env python3
#NoGuiLinux

import pyalpm

#dump a list of pkgs installed on your arch linux system
#and determine if they belong to the official repos
#or to the AUR

def setupRemote():
    handle=pyalpm.Handle('/','/var/lib/pacman')
    repos=['core','community','extra']
    db={}

    for repo in repos:
        db[repo]=handle.register_syncdb(
                repo,
                pyalpm.SIG_DATABASE_OPTIONAL
                )
    sync=handle.get_syncdbs()
    return db

def setupLocal():
    handle=pyalpm.Handle('/','/var/lib/pacman')
    db=handle.get_localdb()
    return db

def checkOfficial(pk,db,skip404=True):
    fail=0
    for repo in db.keys():
        pkg=db[repo].get_pkg(pk)
        if pkg != None:
            print(pkg)
        else:
            if not skip404:
                print('{} : 404_{}'.format(pk,repo.upper()))
            fail+=1
    if fail >= 3:
        return '{}:AUR'.format(pk)
    else:
        return '{}:OFFICIAL'.format(pk)

def dumpLocalPkgList(db):
   pkglist=[i.name for i in db.pkgcache] 
   return pkglist

def display(data):
    if type(data) == type(list()):
        for pk in data:
            print(pk)
    else:
        exit('data provided is not a list')

def process():
    db=setupRemote()
    existant=[checkOfficial(i,db) for i in dumpLocalPkgList(setupLocal())]
    display(existant)

process()
