#! /usr/bin/env python3
# scan a directory -- create an xml manifest of its contents -- zip the xml manifest and the directory up into an archive -- send to a remote server
#need to add cmdline interface, add a prompt to ask if local zip copy is to be kept or deleted
#NoGuiLinux


from xml.etree.ElementTree import Element as element, SubElement as subElement, Comment as comment, tostring
import os, hashlib
import pwd,grp
import base64,paramiko
import zipfile,shutil

class ssh:
    keyFile=os.path.expanduser("~/.ssh/id_rsa")
    host="192.168.1.9"
    port=22
    username="carl"
    def client(self):
        Client=paramiko.SSHClient()
        Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        Client.connect(self.host,port=self.port,username=self.username,key_filename=self.keyFile)
        return Client

    def transfer(self,client,src=None,dest=None,mode="put"):
        sftp_client=client.open_sftp()
        if src != None:
            if dest != None:
                if mode == "put":
                    sftp_client.put(src,dest)
                elif mode == "get":
                    sftp_client.get(src,dest)
                else:
                    print("invalid mode")
            else:
                print("dest cannot be blank")
        else:
            print("src cannot be blank")

    def commander(self,client,cmd=None):
        if cmd != "None":
            stdin,stdout,stderr=client.exec_command(cmd)
            for line in stdout:
                yield line.rstrip("\n")
        else:
            print("there is no command to execute")
    
    def clientClose(self,client):
        client.close()

class docGen:
    manifest="manifest.xml"
    verbose=False
    def integrity(self,fname):
        obj=hashlib.sha512()
        with open(fname,"rb") as file:
            while True:
                data=file.read(1024)
                if not data:
                    break
                obj.update(data)
        return obj.hexdigest()

    def fsize(self,fname):
        return str(os.stat(fname).st_size)

    def getUserGroup(self,fname):
        gid=os.stat(fname).st_gid
        uid=os.stat(fname).st_uid
        group=grp.getgrgid(gid)[0]
        user=pwd.getpwuid(uid)[0]
        return (str(user),str(uid),str(group),str(gid))

    def getPermissions(self,fname):
        return str(oct(os.stat(fname)[0]))[4:]

    def getFileType(self,fname):
        num=str(oct(os.stat(fname)[0]))[2:4]
        types={"01":"FIFO","02":"character device","40":"Directory","60":"block device","10":"Regular file","12":"symbolic link","14":"socket","17":"bit mask for the file type bitfields"}
        keys=[key for key in types.keys()]
        if num in keys:
            return types[num]
        else:
            return num
    
    def genXml(self,dir='.'):
        path=os.path.realpath(dir)
        dirStrip=os.path.dirname(path)
        top = element("Directory",path=os.path.basename(path))
        counter=0
        dircounter=0
        for root,dirname,fnames in os.walk(path):
            dirs=subElement(top,'dir',num=str(dircounter),dpath=root.strip(dirStrip))
            counter=0
            dircounter+=1
            names=subElement(dirs,'dirname')
            names.text=root.strip(dirStrip)
            for fname in fnames:
                fpath=os.path.join(root,fname)
                if os.path.exists(fpath):
                    if self.verbose == True:
                        print(fpath)
                    names=subElement(dirs,'file',num=str(counter))
                    subNames=subElement(names,'fname')
                    subNames.text=fname
                    nameStat=subElement(names,'fsize')
                    nameStat.text=self.fsize(fpath)
                    integ=subElement(names,'integ')
                    integ.text=self.integrity(fpath)
                    uid=subElement(names,"uid")
                    uid.text=self.getUserGroup(fpath)[1]
                    user=subElement(names,"user")
                    user.text=self.getUserGroup(fpath)[0]
                    gid=subElement(names,"gid")
                    gid.text=self.getUserGroup(fpath)[3]
                    group=subElement(names,"group")
                    group.text=self.getUserGroup(fpath)[2]
                    permissions=subElement(names,"permissions")
                    permissions.text=self.getPermissions(fpath)
                    ftype=subElement(names,"ftype")
                    ftype.text=self.getFileType(fpath)
                    #do file integreity check and record
                    counter+=1    
                else:
                    print('path {} is a broken symlink'.format(fpath))
        file=open(self.manifest,"wb")
        file.write(tostring(top))

class zipUp:
    SRC="/home/carl/Documents"
    DST="tmp"
    oPath="torgen.zip"
    counter=1
    dirCounter=1
    manifest="manifest.xml"
    def prep(self):
        if not os.path.exists(self.DST):
            os.mkdir(self.DST)
        if not os.path.exists(os.path.join(self.DST,self.manifest)):
            shutil.copyfile(self.manifest,os.path.join(self.DST,self.manifest))
            #if manifest does not exist generate it

    def zipper(self):
        self.prep()
        if os.path.exists(self.SRC):
            if not os.path.exists(os.path.join(self.DST,os.path.split(self.SRC)[1])):
                shutil.copytree(self.SRC,os.path.join(self.DST,os.path.split(self.SRC)[1]))
            else:
                exit("Destination Dir '{}' Exists".format(self.DST))
        else:
            exit("Source Dir '{}' Does not Exist".format(self.SRC))
        
        try:
            zippy=zipfile.ZipFile(self.oPath,'w',zipfile.ZIP_DEFLATED)
            for root, dirname, fnames in os.walk(self.DST):
                for dir in dirname:
                    absolutePath=os.path.join(root,dir)
                    relativePath=absolutePath.replace(self.DST,os.path.splitext(self.oPath)[0])
                    zippy.write(absolutePath,relativePath)
                    print("directory {} : {} added.".format(self.dirCounter,dir))
                    self.dirCounter+=1
                for fname in fnames:
                    if fname == self.manifest:
                        print("file {} : manifest {} added.".format(self.counter,fname))
                    else:
                        print("file {} : {} added.".format(self.counter,fname))
                    absolutePath=os.path.join(root,fname)
                    relativePath=absolutePath.replace(self.DST,os.path.splitext(self.oPath)[0])
                    zippy.write(absolutePath,relativePath)
                    self.counter+=1
            print("{} created successfully.".format(self.oPath))
            print("Directories : {}\nFiles : {}".format(self.dirCounter,self.counter))
        except IOError as message:
            exit(message)
        except OSError as message:
            exit(message)
        except zipfile.BadZipFile as message:
            exit(message)
        finally:
            zippy.close()
            shutil.rmtree(self.DST)

class run:
    host="192.168.1.9"
    port=22
    username="carl"
    keyFile="~/.ssh/id_rsa"
    keyFile=os.path.realpath(os.path.expanduser(keyFile))
    src="/home/carl/Documents"

    def main(self):
        src=self.src
        src=os.path.realpath(src)
        gen=docGen()
        gen.verbose=True
        gen.genXml(src)
        Zip=zipUp()
        Zip.oPath=os.path.split(src)[1]+".zip"
        Zip.zipper()
        send=ssh()
        send.host=self.host
        send.port=self.port
        send.username=self.username
        send.keyFile=self.keyFile
        client=send.client()
        send.transfer(client,Zip.oPath,os.path.join("/home/carl",Zip.oPath),mode="put")
        send.clientClose(client)

Run=run()
Run.main()
