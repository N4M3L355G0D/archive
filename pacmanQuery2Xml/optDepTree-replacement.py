#! /usr/bin/env python3
#NoGuiLinux
#this script is to replace the optDepTree.py script as this relies on an
#iterable based system rather than the massive reliance on recursion
#that is seen in optDepTree.py

import pyalpm
#loop through a list of pkgs, if the current pkg has deps add to list of pkgs, until for loop reaches end of list

#getDeps() will get the dependency list of the current package and return the list() if there is one, otherwise return None

pkgs=['mplayer']

def setHandle():
    h=pyalpm.Handle('/','/var/lib/pacman')
    return h

def setRemote(handle):
    dbs=['extra','community','core']
    db={}
    for d in dbs:
        db[d]=handle.register_syncdb(d,pyalpm.SIG_DATABASE_OPTIONAL)
    sync=handle.get_syncdbs()
    return db

def setLocal(handle):
    return handle.get_localdb()

def getDeps(pkg,db):
    deps=None
    for repo in db.keys():
        pk=db[repo].get_pkg(pkg)
        if pk != None:
            deps=pk.depends
            break
    return deps

def resolve(pkgs=[]):
    opk=len(pkgs)
    oPk=pkgs
    if pkgs != []:
        handle=setHandle()
        lDb=setLocal(handle)
        rDb=setRemote(handle)

        for pkg in pkgs:
            deps=getDeps(pkg,rDb)
            if deps:
                for pkg_sub in deps:
                    #ensure we are not adding duplicate pkg names to the list
                    if pkg_sub not in pkgs:
                        installed=lDb.get_pkg(pkg_sub)
                        if installed == None:
                            pkgs.append(pkg_sub)
            del(deps)
        if len(pkgs) > opk:
            return pkgs[opk:]
        else:
            return []
    else:
        return 'return empty pkgs list'

print(resolve(pkgs))
