#! /usr/bin/python3

import os, argparse, sys, crypt, getpass

parser=argparse.ArgumentParser()
parser.add_argument("-c","--crypt",help="create passwd entry")
parser.add_argument("-d","--decrypt",help="verify passwd entry")
parser.add_argument("-s","--salt",help="provide salt for decrypt")
parser.add_argument("-f","--two-line-output",help="output data in a 2 line format",action="store_true")
parser.add_argument("-p","--prompt",help="prompt for user data",action="store_true")

options=parser.parse_args()

def error():
    print("please consult -h/--help")

if options.prompt:
    action=input("encrypt/decrypt: ")
    if action == "encrypt":
        passwd=getpass.getpass()
        salt=crypt.mksalt()
    elif action == "decrypt":
        passwd=getpass.getpass()
        salt=input("salt: ")
    else:
        print("unknown action")
        sys.exit("unknown action provide at prompt!")
elif options.crypt:
    passwd=options.crypt
    salt=crypt.mksalt()
elif options.decrypt:
    passwd=options.decrypt
    if options.salt:
        salt=options.salt
    else:
        error()
        sys.exit("no salt provide")
else:
    error()
    sys.exit("no action provide -c/-d")

result=crypt.crypt(passwd,salt)

if options.two_line_output:
    resultSplit=result.split("$")[1:]
    saltString="$"+resultSplit[0]+"$"+resultSplit[1]
    passwdHash=resultSplit[2]
    print("SALT:",saltString)
    print("PASSWD_HASH:",passwdHash)
else:
    print(result)
