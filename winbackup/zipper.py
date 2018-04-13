#! /usr/bin/env python3

import os,sys,argparse,zipfile

path='/srv/samba/php'
zipname='new.zip'

def createZip(zipName,path):
    arcpath=os.path.split(path)[0]
    z=zipfile.ZipFile(zipName,'w',compression=zipfile.ZIP_LZMA)
    for root,dir,fnames in os.walk(path,topdown=True):
        for fname in fnames:
            z.write(os.path.join(root,fname),os.path.join(root.replace(arcpath,''),fname))

createZip(zipname,path)
