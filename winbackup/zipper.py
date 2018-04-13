#! /usr/bin/env python3

import os,sys,argparse,zipfile

path='/srv/samba/php'
zipname='new.zip'

def createZip(zipName,path,FULLPATH=None):
    arcpath=os.path.split(path)[0]
    z=zipfile.ZipFile(zipName,'w',compression=zipfile.ZIP_LZMA)
    for root,dir,fnames in os.walk(path,topdown=True):
        for fname in fnames:
            if FULLPATH == None:
                z.write(os.path.join(root,fname),os.path.join(root.replace(arcpath,''),fname))
            else:
                z.write(os.path.join(root,fname),os.path.join(root,fname))


createZip(zipname,path,FULLPATH=True)
