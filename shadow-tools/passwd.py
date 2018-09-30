import crypt, getpass, sys, os

def checkUser():
    user=getpass.getuser()
    if user != "root":
        print("you are not root/sudo...suck balls- I am quitting!")
        sys.exit()

def getPass():
    passW=getpass.getpass("Password: ")
    if passW != "":
        store=crypt.crypt(passW,crypt.mksalt())
    return store

def tmpPassFile(store,file="passwd.tmp"):
    ofile=open(file,"w")
    for i in store:
        ofile.write(i)
    ofile.close()

def entryUserGet():
    userC=getpass.getpass("what user is this for?: ")
    return userC

def entryShadow(store,userC):
    shadow=open("/etc/shadow","r")
    entry=list()
    
    for i in shadow:
        line=i.split(":")
        if line[0] == userC:
            line[1]=store
            for k,j in enumerate(line):
                entry.append(j)
                if k < len(line)-1:
                    entry.append(":")
    return entry

def tmpEntryFile(entry,file="shadow_entry.tmp"):
    ofile=open(file,"w")
    for i in ''.join(entry):
        ofile.write(i)
    ofile.close()


def cleanup():
    passT="passwd.tmp"
    if os.path.exists(passT):
        os.remove(passT)

def main():
    checkUser()
    passW=getPass()
    tmpPassFile(store=passW)
    userC=entryUserGet()
    entryL=entryShadow(passW,userC)
    tmpEntryFile(entry=entryL)
    print(''.join(entryL).rstrip("\n"))
    cleanup()

main()
