#! /usr/bin/env python3
import tarfile, argparse, os, platform, sys

def error():
 print("please see -h/--help")
 sys.exit()


supportedFormats_str="xz,gz,bz2"

if platform.uname().system == 'Windows':
    osslash="\\"
else:
    osslash="/"
print(sys.argv[0]+" running on system: "+platform.uname().system+", release: "+platform.uname().release+", version: "+platform.uname().version)
defaultExtract="."

parser=argparse.ArgumentParser()
parser.add_argument("-i","--infile",help="infile")
parser.add_argument("-c","--command",help="what does tar.py do? [z -> compress, la -> list all, l -> list member, xa -> extract all, x -> extract member]")
parser.add_argument("-m","--member",help="for commands that require a member [a single member, or comma delimited list of members]")
parser.add_argument("-f","--compression",help="what compression algorithm to use, default is xz [supports "+supportedFormats_str+"]")
parser.add_argument("-p","--path",help="where to extract to. defaults to ["+defaultExtract+"]")
parser.add_argument("-s","--list-commands",help="list commands for -c/--command",action="store_true")
options=parser.parse_args()



if options.list_commands:
 cmds=["z -> compress","la -> list all","l -> list member [requires -m/--member]","xa -> extract all","x -> extract member [requires -m/--member]"]
 for i in cmds:
  print(i)
 sys.exit()
elif not options.infile:
 error()
elif not options.command:
 error()

supportedFormats=supportedFormats_str.split(",")
defaultFormat=os.path.splitext(options.infile)[1].strip(".")
if defaultFormat == '':
 defaultFormat='xz'
if options.compression:
 if options.compression in supportedFormats:
  defaultFormat=options.compression
 else:
  print("[WARN] [ "+options.compression+" ] not supported. Please review -h/--help. Will use default format [ "+defaultFormat+" ]")
print("[WARN] using "+defaultFormat+" for compression.")

if options.path:
 if os.path.exists(options.path):
  defaultExtract=options.path
 else:
  print("[WARN] [ "+options.path+" ] does not exist. using default extraction path [ "+defaultExtract+" ]")
print("[WARN] using "+defaultExtract+" for extraction path.")

if options.command:
 if options.command == "z":
  opath=defaultExtract+osslash+os.path.basename(options.infile+".tar."+defaultFormat)
  if not os.path.exists(opath):
   print(opath)
   file=tarfile.open(opath,"w:"+defaultFormat)
   file.add(options.infile)
   file.close()
  else:
   print(opath+" -> Exists!")
 elif options.command == "xa":
  print("extracting:",options.infile)
  file=tarfile.open(options.infile,"r:"+defaultFormat)
  file.extractall(defaultExtract+osslash+os.path.basename(options.infile.strip(".tar."+defaultFormat)))
  file.close()
 elif options.command == "x":
  if options.member:
   file=tarfile.open(options.infile,"r:"+defaultFormat)
   for i in options.member.split(","):
    print("extracting [ "+i+" ] member from:",options.infile)
    file.extract(i,path=defaultExtract)
   file.close()
  else:
   print("[ERROR] please specify a member, or comma delimited list of members to extract with -m")
 elif options.command == "la":
  print("listing:",options.infile)
  file=tarfile.open(options.infile,"r:"+defaultFormat)
  print(file.list(members=file.getmembers()))
  file.close()
 elif options.command == "l":
  print("list member from: ",options.infile)
  file=tarfile.open(options.infile,"r:"+defaultFormat)
  if options.member:
   m3mbers=options.member.split(",")
   for i in m3mbers:
       m3m=[file.getmember(i)]
       print(file.list(members=m3m))
  else:
   print("[ERROR] please specify a member, or a comma delimited listed of members with -m")
 else:
  print("[ERROR] that is not a valid command operation, please view -s/--list-commands") 
