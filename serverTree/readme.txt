#paramiko uses an sftp/scp client to perform filetransfers 

#a python3 script to:
scan a directory -> create an xml manifest of its contents -> zip the xml manifest and the directory up into an archive -> send to a remote server expecting a zipfile


#if id_rsa fails, attempt password authentication, if given password is provided with the -P option

#complete utility with all modules built in
#includes cmdline utility
serverTree.py

#useage

#get help menu
python3 serverTree.py -h

#general useage
python serverTree.py -u carl -k ~/.ssh/id_rsa -s ~/Documents/ -d /home/remote/Downloads -z try.zip 
#-d applies to the remote host only
#-z will take a filename with, or without, the zip extension and ensure the extension is added if needed
#-u is the remote server user
#-h is help

#expanded general useage
python serverTree.py -u carl -k ~/.ssh/id_rsa -s ~/Documents/resume -d /home/carl/Downloads -z try.zip -H 192.168.1.9 -p 22

#best of luck,
NoGuiLinux
