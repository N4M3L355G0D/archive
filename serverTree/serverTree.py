#! /usr/bin/env python3
# scan a directory -- create an xml manifest of its contents -- zip the xml manifest and the directory up into an archive -- send to a remote server
#need to add cmdline interface, add a prompt to ask if local zip copy is to be kept or deleted
#NoGuiLinux


from xml.etree.ElementTree import Element as element, SubElement as subElement, Comment as comment, tostring
import os, hashlib
import pwd,grp
import base64,paramiko
import zipfile,shutil,argparse

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
            os.remove(self.manifest)

class run:
    host="127.0.0.1"
    port=22
    username=""
    keyFile=""
    src=""
    zipName=""
    dst=""
    def pathExpand(self,path):
        return os.path.realpath(os.path.expanduser(path))

    def zipnameMod(self):
        if self.zipName == "":
            self.zipName=os.path.split(self.src)[1]+".zip"
        else:
            if os.path.splitext(self.zipName)[1] == "":
                self.zipName+=".zip"
   
    def dstMod(self):
        if self.dst == "":
            self.dst=os.path.join(self.pathExpand('~'),self.zipName)
        else:
            self.dst=os.path.join(self.pathExpand(self.dst),self.zipName)
    def delPrompt(self):
        breakStates=['y','n']
        stupidCounter=0
        stupidTimeout=10
        ERR_FailToDelete="something went wrong and '{}' was not successfully deleted".format(self.zipName)
        if os.path.split(self.dst)[0] != self.pathExpand("."):
            user=input("do you wish to delete the generated zipfile in the current directory? : ")
            while user not in breakStates:
                stupidCounter+=1
                if stupidCounter <= stupidTimeout:
                    user=input("[ {}/{} ] do you wish to delete the generated zipfile in the current directory? [y/n] : ".format(stupidCounter,stupidTimeout))
                else:
                    print("the user apparently cannot read... not deleting the residue!")
                    break
            if user == 'y':
                os.remove(os.path.join(self.pathExpand("."),self.zipName))
                try:
                    if not os.path.exists(os.path.join(self.pathExpand("."),self.zipName)):
                        print("the residual zipfile '{}' was successfully deleted!".format(self.zipName))
                    else:
                        print(ERR_FailToDelete)
                except IOError as message:
                    print(ERR_FailToDelete)
                    exit(message)
                except OSError as message:
                    print(ERR_FailToDelete)
                    exit(message)
            else:
                print("user chose to keep the residual zip file.")


    def main(self):
        if self.username != "":
            if self.host != "":
                if self.keyFile != "":
                    if self.src != "":
                        if 1 < self.port < 65535:
                            self.zipnameMod()
                            self.dstMod()
                            #perform any necessary expansions 
                            self.keyFile=self.pathExpand(self.keyFile)
                            self.src=self.pathExpand(self.src)
                            src=self.src
                            if os.path.isdir(src):
                                gen=docGen()
                                gen.verbose=True
                                gen.genXml(src)
                                Zip=zipUp()
                                Zip.oPath=self.zipName
                                Zip.SRC=src
                                Zip.zipper()
                                send=ssh()
                                send.host=self.host
                                send.port=self.port
                                send.username=self.username
                                send.keyFile=self.keyFile
                                client=send.client()
                                print('SRC -> {}\nDST -> {}@{}:{}'.format(self.zipName,self.username,self.host,self.dst))
                                send.transfer(client,self.zipName,self.dst,mode="put")
                                send.clientClose(client)
                                self.delPrompt()
                            else:
                                exit("src directory provided is not a directory!")
                        else:
                            exit("port must be within 1-65535!")
                    else:
                        exit("src directory cannot be blank!")
                else:
                    exit("keyFile cannot be blank!")
            else:
                exit("hostname cannot be blank!")
        else:
            exit("username cannot be blank!")

    def cmdline(self):
        parser=argparse.ArgumentParser()
        parser.add_argument("-d","--dst")
        parser.add_argument("-z","--zipname")
        parser.add_argument("-H","--host")
        parser.add_argument("-p","--port")
        parser.add_argument("-k","--rsa-keyfile")
        parser.add_argument("-s","--src")
        parser.add_argument("-u","--username")
        options=parser.parse_args()

        if options.dst:
            self.dst=options.dst
        if options.zipname:
            self.zipName=options.zipname
        if options.host:
            self.host=options.host
        if options.port:
            self.port=options.port
        if options.rsa_keyfile:
            self.keyFile=options.rsa_keyfile
        if options.src:
            self.src=options.src
        if options.username:
            self.username=options.username

Run=run()
Run.cmdline()
Run.main()
