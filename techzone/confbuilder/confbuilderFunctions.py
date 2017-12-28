#! /usr/bin/python3

import os

def detect(path):
    if os.path.exists(str(path)):
        if os.path.isfile(str(path)):
            return True
        else:
            return False
    else:
        return False


def detect_list(files=("#NEEDFILES",)):
    fails=list()
    for element in files:
        if detect(element) == False:
            fails.append(element)
    if len(fails) > 0 :
        return fails
    else:
        return True


def whatismissing():
 files=("/usr/bin/smbd","/usr/bin/nmbd","/etc/samba/smb.conf","/etc/samba/smb.conf.default","/etc/httpd/conf/httpd.conf","/usr/bin/httpd") 
 faillist=detect_list(files)
 return faillist


def smbConf_global(workgroup="MANJARO",srv_str="Samba Server",log_file="/var/log/samba/%m.log",mx_log_sz="50",security="user",map2guest="Bad User",guest_account="root",usershare_path="/var/lib/samba/usershare",usershare_mx_share="100",usershare_allow_guests="yes",usershare_owner_only="yes"):
    globalString=list()
    globalString_str=""
    globalString.append("[global]\n")
    globalString.append("\tworkgroup = "+workgroup+"\n")
    globalString.append("\tserver string = "+srv_str+"\n")
    globalString.append("\tlog file = "+log_file+"\n")
    globalString.append("\tmax log size = "+mx_log_sz+"\n")
    globalString.append("\tsecurity = "+security+"\n")
    globalString.append("\tmap to guest = "+map2guest+"\n")
    globalString.append("\tguest account = "+guest_account+"\n")
    globalString.append("\tusershare path = "+usershare_path+"\n")
    globalString.append("\tusershare max shares = "+usershare_mx_share+"\n")
    globalString.append("\tusershare owner only = "+usershare_owner_only+"\n")
    
    for i in globalString:
         print(i)
         globalString_str=globalString_str+i
    return globalString_str

def shareCreate(share="homes",workgroup="deskos",srv_str="desk os server",browseable="yes",writable="yes",path="/srv/samba/techzone",public="yes",guest_account="root",force_user="root"):
    shareString=list()
    shareString.append("["+share+"]\n")
    if workgroup != "":
        shareString.append("\tworkgroup = "+workgroup+"\n")
        shareString.append("\tserver string = "+srv_str+"\n")
    shareString.append("\twritable = "+writable+"\n")
    shareString.append("\tpath = "+path+"\n")
    shareString.append("\tpublic = "+public+"\n")
    if guest_account != "":
        shareString.append("\tguest account = "+guest_account+"\n")
    if force_user != "":
        shareString.append("\tforce user = "+force_user+"\n")

