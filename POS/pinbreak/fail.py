#! /usr/bin/python3

import gi,os,sys,argparse
import subprocess
gi.require_version("Gtk","3.0")
from gi.repository import Gtk as gtk
from gi.repository import Pango as pango


nl="\n"
hostname=""
port=0

CFG="./pinbreak.cfg"
if os.path.exists(CFG) and os.path.isfile(CFG):
 with open(CFG,"r") as cfg:
  for i in cfg:
   if len(i.split("=")) > 1:
    varName=i.split("=")[0]
    varVal=i.split("=")[1]
    if varName == "hostname":
     hostname=varVal.rstrip(nl)
    if varName == "port":
     port=int(varVal.rstrip(nl))
    if varName == "icon":
     icon=varVal.rstrip(nl)
else:
    print("configuration file does not exist! quitting!")
    exit()

class window(gtk.Window):
 def message(self):
  parser=argparse.ArgumentParser()
  parser.add_argument("-m","--message")
  parser.add_argument("-t","--title")
  options=parser.parse_args()
  if options.message:
   if options.title:
    return [str(options.message),str(options.title)]
   else:
    return [str(options.message),str("Default ERROR Dialog")]
  else:
   if options.title:
    return [str("No Message"),str(options.title)]
   else:
    return [str("No Message"),str("Default ERROR Dialog")]

 def __init__(self):
  gtk.Window.__init__(self,title="Pinbreak "+self.message()[1])
  gtk.Window.set_default_size(self,300,300)
  gtk.Window.set_border_width(self,10)
  if os.path.exists(icon) and os.path.isfile(icon):
   gtk.Window.set_icon_from_file(self,icon)

  grid=gtk.Grid()
  self.add(grid)
  
  display=gtk.TextView()
  display.set_wrap_mode(True)
  display.set_editable(False)
  display.modify_font(pango.FontDescription('Arial 12'))
  displayBuffer=display.get_buffer()
  displayBuffer.set_text(self.message()[0])
  
  scrollDisplay=gtk.ScrolledWindow()
  scrollDisplay.add(display)
  scrollDisplay.set_hexpand(True)
  scrollDisplay.set_vexpand(True) 
  grid.attach(scrollDisplay,0,0,1,1)
 
  ok=gtk.Button(label="Okay")
  ok.connect("clicked",self.Error)
  grid.attach(ok,0,2,1,1)
  
 def Error(self,widget):
  print("Error confirmed")
  gtk.main_quit()
 
win=window()
win.connect("delete_event",gtk.main_quit)
win.show_all()
gtk.main()
