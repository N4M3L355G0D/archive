#! /usr/bin/env python3

import os,sys,zipfile

path='/srv/samba/php'
zipname='new.zip'

def createZip(zipName,path,FULLPATH=False,custom=''):
    arcpath=os.path.split(path)[0]
    z=zipfile.ZipFile(zipName,'w',compression=zipfile.ZIP_LZMA)
    for root,dir,fnames in os.walk(path,topdown=True):
        for fname in fnames:
            if custom == '':
                if FULLPATH == False:
                    z.write(os.path.join(root,fname),os.path.join(root.replace(arcpath,''),fname))
                else:
                    z.write(os.path.join(root,fname),os.path.join(root,fname))
            else:
                z.write(os.path.join(root,fname),os.path.join(custom,fname))



createZip(zipname,path)
