#! /usr/bin/python3

import sys, os, argparse
### a google services site echoer for the browser_wrapper.sh script

def config():
 eof="\n"
 txt_file="google-sites.cfg"
 urls=dict()
 CONF=open(txt_file,"r")
 for option in CONF:
  if len(option.split(" ")) >= 2:
   opt1=option.split(" ")[0]
   opt2=option.split(" ")[1]
   if opt1 == "drive":
    urls["drive"]=opt2.rstrip(eof)
   elif opt1 == "gmail":
    urls["gmail"]=opt2.rstrip(eof)
   elif opt1 == "contacts":
    urls["contacts"]=opt2.rstrip(eof)
   elif opt1 == "hangouts":
    urls["hangouts"]=opt2.rstrip(eof)
  else:
   break
 return urls

def cmdline():
 parser=argparse.ArgumentParser()
 parser.add_argument("-d","--drive",help="print the url for Google Drive",action="store_true")
 parser.add_argument("-g","--gmail",help="print the url for GMail",action="store_true")
 parser.add_argument("-c","--contacts",help="print the url Google Contacts",action="store_true")
 parser.add_argument("-H","--hangouts",help="print the url for Google Hangouts",action="store_true")

 options=parser.parse_args()
 return options

def echo():
 options=cmdline()
 conf=config()
## if drive option, print prive
 if options.drive:
  if "drive" in conf.keys():
   print(conf.__getitem__("drive"))
## if $1 == gmail
### print mail.google.com
 if options.gmail:
  if "gmail" in conf.keys():
   print(conf.__getitem__("gmail"))
## if $1 == contacts
### print contacts.google.com
 if options.contacts:
  if "contacts" in conf.keys():
   print(conf.__getitem__("contacts"))
## if $1 == hangouts
### print contacts.google.com
 if options.hangouts:
  if "hangouts" in conf.keys():
    print(conf.__getitem__("hangouts"))


echo()
