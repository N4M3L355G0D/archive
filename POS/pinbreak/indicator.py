#! /usr/bin/python3

import gi, os, sys, socket
import subprocess as sp
gi.require_version("Gtk","3.0")
from gi.repository import Gtk as gtk
from gi.repository import Pango as pango
sys.path.insert(0,"./ping")

import host2ip

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
     icon=varVal.rstrip("\n")
else:
    print("configuration file does not exist! quitting!")
    exit()


class window(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self,title="Pinbreak Indicator")
        gtk.Window.set_default_size(self,220,160)
        gtk.Window.set_border_width(self,10)
        if os.path.exists(icon) and os.path.isfile(icon):
         gtk.Window.set_icon_from_file(self,icon)
        grid=gtk.Grid()
        self.add(grid)

        display=gtk.TextView()
        display.set_wrap_mode(True)
        display.set_editable(False)
        display.modify_font(pango.FontDescription('Arial 12'))
        display_buffer=display.get_buffer()
        display_buffer.set_text("Nothing to display yet")

        scrollDisplay=gtk.ScrolledWindow()
        scrollDisplay.add(display)
        scrollDisplay.set_hexpand(True)
        scrollDisplay.set_vexpand(True)
        grid.attach(scrollDisplay,1,0,1,1)

        test=gtk.Button(label="Test")
        test.connect("clicked",self.presence,test,display,display_buffer)
        grid.attach(test,1,2,1,1)

        close=gtk.Button(label="Close")
        close.connect("clicked",gtk.main_quit)
        grid.attach(close,1,3,1,1)

    def logcheck(self,log):
        if not os.path.exists(log):
            print(log+" [Does not exist]\n\t[making it]")
            os.mkdir(os.path.split(log)[0])
            file = open(log,'w')
            file.write('')
            file.close()
            print(log+" [Done]")
    def increaseError(self,log):
        error_count=0
        max_error_count=10
        self.logcheck(log)
        with open(log) as f:
            for line in f:
                error_count = line
        error_count = int(int(error_count) +1)
        print("error counter: "+str(error_count))
        file = open(log,'w')
        file.write(str(error_count))
        file.close()
        if int(error_count) >= max_error_count:
            print("sending notification")
            # send notification
            file=open(log,'w')
            file.write('0')
            file.close()
            file=open(log+".message","w")
            file.write("non-existant port:address")
            file.close()


    def presence(self,widget,test,display,display_buffer):
        log="error/error.log"
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((hostname,port))

        if result != 0:
            output="Server Port "+str(port)+" on "+hostname+" is Unavailable"
            self.increaseError(log)

        version=sp.Popen("python3 ./helpers/getVersion.py",shell=True,stdout=sp.PIPE)
        result,err=version.communicate()
        travelTime=host2ip.linuxPing(hostname)
        display_buffer.set_text(result.decode()+"\n"+travelTime)
        return True

win=window()
win.connect("delete-event",gtk.main_quit)
win.show_all()
gtk.main()
