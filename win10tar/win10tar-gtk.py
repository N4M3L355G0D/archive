#! /usr/bin/python3

import gi, os, sys, platform, win10tarDev
gi.require_version('Gtk','3.0')
from gi.repository import Gtk as gtk

class window(gtk.Window):
    win10tar=win10tarDev.win10tar()
    if platform.uname().system != 'Windows':
        osslash="./"
    else:
        osslash="\\"
    actFail="cancel"
    actSuccess="Input file/directory"
    compressor="XZ"
    selectedBrowser="[selected in file browser]"
    fail=False
    try:
    	opath=os.environ['HOME']
    except:
        fail=True
    if fail == True:
     try:
      opath=os.environ['USERPROFILE']
      fail=False
     except:
      fail=True
      opath="."
    def __init__(self):
        gtk.Window.__init__(self,title="win10tar")
        
        self.box = gtk.Box(spacing=6)
        self.add(self.box)

        grid = gtk.Grid()
        self.box.add(grid)
        
        self.infile=gtk.Entry()
        self.infile.set_text(self.actSuccess)
        grid.attach(self.infile,0,0,1,1)
        #browse for files
        self.browse=gtk.Button(label="Browse Files")
        self.browse.connect("clicked",self.browseFile)
        grid.attach(self.browse,1,0,1,1)
        #browse for dirs
        self.browseDir=gtk.Button(label="Browse Dirs")
        self.browseDir.connect("clicked",self.browseFolder)
        grid.attach(self.browseDir,2,0,1,1)
        #postive reaction
        self.button0 = gtk.Button(label="Compress")
        self.button0.connect("clicked",self.action,self.actSuccess)
        grid.attach(self.button0,3,0,1,1)
        #extract
        self.extract = gtk.Button(label="Extract")
        self.extract.connect("clicked",self.extractFile)
        grid.attach(self.extract,4,0,1,1)
        #negative reaction
        self.button1 = gtk.Button(label="Close")
        self.button1.connect("clicked",self.action,self.actFail)
        grid.attach(self.button1,5,0,1,1)

        #compression options
        self.button3 = gtk.RadioButton.new_with_label_from_widget(None,"XZ")
        self.button3.connect("toggled",self.compression,"XZ")
        grid.attach(self.button3,0,1,1,1)

        self.button4 = gtk.RadioButton.new_from_widget(self.button3)
        self.button4.set_label("GZ")
        self.button4.connect("toggled",self.compression,"GZ")
        grid.attach(self.button4,1,1,1,1)

        self.button5 = gtk.RadioButton.new_from_widget(self.button3)
        self.button5.set_label("BZ2")
        self.button5.connect("toggled",self.compression,"BZ2")
        grid.attach(self.button5,2,1,1,1)
        #output dir
        self.odir=gtk.Entry()
        self.odir.set_text(self.opath)
        grid.attach(self.odir,0,3,1,1)
        #output path setting
        self.odirButton=gtk.Button()
        self.odirButton.set_label("Browse")
        self.odirButton.connect("clicked",self.output)
        grid.attach(self.odirButton,1,3,1,1)

    def output(self,widget):
        dialog=gtk.FileChooserDialog("Please Select a file to extract",self,gtk.FileChooserAction.SELECT_FOLDER,(gtk.STOCK_CANCEL,gtk.ResponseType.CANCEL,gtk.STOCK_OPEN,gtk.ResponseType.OK))
        response=dialog.run()
        if response == gtk.ResponseType.OK:
            print(dialog.get_filename(),self.selectedBrowser)
            self.odir.set_text(dialog.get_filename())
            dialog.destroy()
        elif response == gtk.ResponseType.CANCEL:
            print("user selection cancelled")
            dialog.destroy()

    def extractFile(self,widget):
            cmd=self.osslash+"win10tar.py -i "+self.infile.get_text()+" -c xa"+" -f "+self.compressor.lower()+" -p "+self.odir.get_text()
            print(cmd)
            #os.system(cmd)
            #here is the update[start]
            if self.infile.get_text() != self.actSuccess and self.infile.get_text() != '':
                if os.path.exists(self.infile.get_text()):
                    self.win10tar.command="xa"
                    self.win10tar.compression=self.compressor.lower()
                    self.win10tar.defaultExtract=self.odir.get_text()
                    self.win10tar.path=self.odir.get_text()
                    self.win10tar.infile=self.infile.get_text()
                    self.win10tar.main()
                    #here is the update[end]
                else:
                    print(self.infile.get_text(),"[NONEXISTANT]")
            else:
                self.errorNB()

    def browseFolder(self,widget):
        dialog=gtk.FileChooserDialog("Please Select a file to compress",self,gtk.FileChooserAction.SELECT_FOLDER,(gtk.STOCK_CANCEL,gtk.ResponseType.CANCEL,gtk.STOCK_OPEN,gtk.ResponseType.OK))
        response=dialog.run()
        if response == gtk.ResponseType.OK:
            print(dialog.get_filename(),self.selectedBrowser)
            self.infile.set_text(dialog.get_filename())
            dialog.destroy()
        elif response == gtk.ResponseType.CANCEL:
            print("user selection cancelled")
            dialog.destroy()

    def browseFile(self,widget):
        dialog=gtk.FileChooserDialog("Please Select a file to compress",self,gtk.FileChooserAction.OPEN,(gtk.STOCK_CANCEL,gtk.ResponseType.CANCEL,gtk.STOCK_OPEN,gtk.ResponseType.OK))
        response=dialog.run()
        if response == gtk.ResponseType.OK:
            print(dialog.get_filename(),self.selectedBrowser)
            self.infile.set_text(dialog.get_filename())
            dialog.destroy()
        elif response == gtk.ResponseType.CANCEL:
            print("user selection cancelled")
            dialog.destroy()

    def compression(self,widget,compressor):
        self.compressor=compressor

    def errorNB(self):
        print("'",self.actSuccess,"' cannot be left blank")

    def action(self,widget,action):
        if action == "cancel":
            gtk.main_quit()
        elif action == self.infile.get_text():
            self.errorNB()
        elif self.infile.get_text() == '':
            self.errorNB()
        else:
            if os.path.exists(self.infile.get_text()):
                print(self.infile.get_text(),self.compressor)
            else:
                print(self.infile.get_text(),": [INEXISTANT]")
            blacklist=[self.opath,'']
            cmd=self.osslash+"win10tar.py -i "+self.infile.get_text()+" -c z"+" -f "+self.compressor.lower()+" -p "+self.odir.get_text()
            #os.system(cmd)
            self.win10tar.command='z'
            self.win10tar.compression=self.compressor.lower()
            self.win10tar.defaultExtract=self.odir.get_text()
            self.win10tar.path=self.odir.get_text()
            self.win10tar.infile=self.infile.get_text()
            self.win10tar.main()
            print(cmd)
            
win = window()
win.connect("delete-event",gtk.main_quit)
win.show_all()
gtk.main()
