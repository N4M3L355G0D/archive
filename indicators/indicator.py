#! /usr/bin/python3

import gi, os, sys
import subprocess as sp
gi.require_version("Gtk","3.0")
from gi.repository import Gtk as gtk

class window(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self,title="Pinbreak Indicator")
        gtk.Window.set_default_size(self,650,450)
        gtk.Window.set_border_width(self,10)

        grid=gtk.Grid()
        self.add(grid)

        progressbar = gtk.ProgressBar()
        progressbar.set_fraction(0.0)
        
        test=gtk.Button(label="Test")
        test.connect("clicked",self.presence,progressbar,test)
        grid.attach(test,1,2,1,1)

        grid.attach(progressbar,1,1,1,1)

    def presence(self,widget,progressbar,test):
        data_raw=sp.Popen("./pinger.sh",stdout=sp.PIPE,shell=True)
        i= data_raw.communicate()
        output=float(str(i[0].decode()).split("=")[1].rstrip("\n"))
        progressbar.set_fraction(output)
        progressbar.set_text(str(output))
        progressbar.set_show_text(test)
        return output

win=window()
win.connect("delete-event",gtk.main_quit)
win.show_all()
gtk.main()
