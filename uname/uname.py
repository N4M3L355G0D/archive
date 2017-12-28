#! /usr/bin/python3

import argparse, platform, hashlib

class Uname():
 def __init__(self):
  self.main()
        
 #arg strings used throughout

 str_system="--system"
 str_node="--node"
 str_release="--release"
 str_version="--version"
 str_processor="--processor"
 str_machine="--machine"
 
 def IDS(self):
  ids_obj=dict()
  ids=dict()
  #setup ids objects
  ids_obj[self.str_system]=hashlib.md5()
  ids_obj[self.str_node]=hashlib.md5()
  ids_obj[self.str_release]=hashlib.md5()
  ids_obj[self.str_version]=hashlib.md5()
  ids_obj[self.str_processor]=hashlib.md5()
  ids_obj[self.str_machine]=hashlib.md5()
  #add identifier strings
  ids_obj[self.str_system].update(self.str_system.encode())
  ids_obj[self.str_node].update(self.str_node.encode())
  ids_obj[self.str_release].update(self.str_release.encode())
  ids_obj[self.str_version].update(self.str_version.encode())
  ids_obj[self.str_processor].update(self.str_processor.encode())
  ids_obj[self.str_machine].update(self.str_machine.encode())
  #save last 5 digits of hex digests
  ids[self.str_system]=ids_obj[self.str_system].hexdigest()[-5:]
  ids[self.str_node]=ids_obj[self.str_node].hexdigest()[-5:]
  ids[self.str_release]=ids_obj[self.str_release].hexdigest()[-5:]
  ids[self.str_version]=ids_obj[self.str_version].hexdigest()[-5:]
  ids[self.str_processor]=ids_obj[self.str_processor].hexdigest()[-5:]
  ids[self.str_machine]=ids_obj[self.str_machine].hexdigest()[-5:]
  return ids
 
 #cmdline
 def cmdline(self):
  states=list()
  count=0
  parser=argparse.ArgumentParser()
  parser.add_argument("-s",self.str_system,action="store_true")
  parser.add_argument("-n",self.str_node,action="store_true")
  parser.add_argument("-r",self.str_release,action="store_true")
  parser.add_argument("-v",self.str_version,action="store_true")
  parser.add_argument("-p",self.str_processor,action="store_true")
  parser.add_argument("-m",self.str_machine,action="store_true")
  parser.add_argument("-I","--ids",action="store_true")
  parser.add_argument("-a","--all",action="store_true")
  parser.add_argument("-N","--names",action="store_true")
  options=parser.parse_args()
  states.append(options.system)
  states.append(options.node)
  states.append(options.release)
  states.append(options.version)
  states.append(options.processor)
  states.append(options.machine)
  states.append(options.ids)
  states.append(options.all)
  for i in states:
      if i == False:
          count+=1
  if count == 9:
      print("Please use -h/--help")
  return options
 
 def main(self):
  options=self.cmdline()
  uname=platform.uname()
  ids=self.IDS()
  
  odata=list()
  
  if options.system:
   system=uname.system
   if options.ids:
    odata.append((system,ids[self.str_system]))
   elif options.names:
    odata.append((system,"["+self.str_system+"]"))
   else:
    odata.append(system)
  if options.node:
   node=uname.node
   if options.ids:
    odata.append((node,ids[self.str_node]))
   elif options.names:
    odata.append((node,"["+self.str_node+"]"))
   else:
    odata.append(node)
  if options.release:
   release=uname.release
   if options.ids:
    odata.append((release,ids[self.str_release]))
   elif options.names:
    odata.append((release,"["+self.str_release+"]"))
   else:
    odata.append(release)
  if options.version:
   version=uname.version
   if options.ids:
    odata.append((version,ids[self.str_version]))
   elif options.names:
    odata.append((version,"["+self.str_version+"]"))
   else:
    odata.append(version)
  if options.machine:
   machine=uname.machine
   if options.ids:
    odata.append((machine,ids[self.str_machine]))
   elif options.names:
    odata.append((machine,"["+self.str_machine+"]"))
   else:
    odata.append(machine)
  if options.processor:
   processor=uname.processor
   if processor == "":
    processor="unknown"
   if options.ids:
    odata.append((processor,ids[self.str_processor]))
   elif options.names:
    odata.append((processor,"["+self.str_processor+"]"))
   else:
    odata.append(processor)
  if options.all:
   if options.ids:
    odata.append((uname.system,ids[self.str_system]))
    odata.append((uname.node,ids[self.str_node]))
    odata.append((uname.release,ids[self.str_release]))
    odata.append((uname.version,ids[self.str_version]))
    odata.append((uname.machine,ids[self.str_machine]))
    if uname.processor == "":
     odata.append(("unknown",ids[self.str_processor]))
    else:
     odata.append((uname.processor,ids[self.str_processor]))
   elif options.names:
    odata.append((uname.system,"["+self.str_system+"]"))
    odata.append((uname.node,"["+self.str_node+"]"))
    odata.append((uname.release,"["+self.str_release+"]"))
    odata.append((uname.version,"["+self.str_version+"]"))
    odata.append((uname.machine,"["+self.str_machine+"]"))
    if uname.processor == "":
     odata.append(("unknown","["+self.str_processor+"]"))
    else:
     odata.append((uname.processor,"["+self.str_processor+"]"))
   else:
    odata.append(uname.system)
    odata.append(uname.node)
    odata.append(uname.release)
    odata.append(uname.version)
    odata.append(uname.machine)
    if uname.processor == "":
     odata.append("unknown")
    else:
     odata.append(uname.processor)

  for info in odata:
   if options.ids or options.names: 
    print(info[1],info[0],sep=" , ")
   else:
    print(info)

a=Uname()
