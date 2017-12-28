#! /usr/bin/python3


import hashlib, gi,os,datetime,pwd, extraparts
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

pile="/path/to/file"

class window(Gtk.Window):
 def __init__(self):
  Gtk.Window.__init__(self,title="SecureFile")
  Gtk.Window.set_default_size(self,600,250) 
  date_obj=datetime.datetime.now()
  w=6
  grid=Gtk.Grid()
  self.add(grid)

  display=Gtk.TextView()
  display.set_wrap_mode(True)
  display.set_editable(False)
  display_buffer=display.get_buffer()
  display_buffer.set_text("Copy and Paste Data will be Here!!")
#  grid.attach(display,0,0,w,1)

  scrolldisplay=Gtk.ScrolledWindow()
  scrolldisplay.add(display)
  grid.attach(scrolldisplay,0,0,w,1)

  entry_write=Gtk.Entry()
  entry_write.set_text("securefile-output-xml-tagged.txt")
  grid.attach(entry_write,0,1,w,1)

  entry_file=Gtk.Entry()
  entry_file.set_text(pile)
  grid.attach(entry_file,0,2,w,1)

  entry_date=Gtk.Entry()
  entry_date.set_text(str(date_obj.month)+"."+str(date_obj.day)+"."+str(date_obj.year))
  entry_date.set_hexpand(True)
  grid.attach(entry_date,0,3,w,1)
  
  entry_owner=Gtk.Entry()
  entry_owner.set_text(pwd.getpwuid(os.getuid())[0])
  grid.attach(entry_owner,0,4,w,1)
  

  notes=Gtk.TextView()
  notes.set_wrap_mode(True)
  textbuffer=notes.get_buffer()
  textbuffer.set_text("notes...\n")
  #grid.attach(notes,0,5,w,1)

  notescroll=Gtk.ScrolledWindow()
  notescroll.add(notes)
  grid.attach(notescroll,0,5,w,1)

  filebutton=Gtk.Button.new_with_mnemonic("_Generate Entry")
  filebutton.connect("clicked",self.integral,entry_file,entry_owner,entry_write,notes,textbuffer,display,display_buffer)
  grid.attach(filebutton,0,6,w,1)

  
  FileManager=Gtk.Button.new_with_mnemonic("_File Manager")
  FileManager.connect("clicked",self.chooser,entry_file)
  grid.attach(FileManager,0,7,w,1)

  CloseButton=Gtk.Button.new_with_mnemonic("_Close")
  CloseButton.connect("clicked",Gtk.main_quit)
  grid.attach(CloseButton,0,8,w,1)


 def chooser(self,widget,entry_file):
  dialog=Gtk.FileChooserDialog("Choose a File",self,Gtk.FileChooserAction.OPEN,(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN,Gtk.ResponseType.OK))
  response=dialog.run()
  
  if response == Gtk.ResponseType.OK:
   print("Selected")
   pile=str(dialog.get_filename())
   entry_file.set_text(pile)
   return str(dialog.get_filename()), dialog.destroy()
  elif response == Gtk.ResponseType.CANCEL:
   print("Okay")
   dialog.destroy()

 def integral(self,widget,File_name,owner,entry_write,notes,textbuffer,display,display_buffer):
  
  comment=textbuffer.get_text(textbuffer.get_start_iter(),textbuffer.get_end_iter(),notes)

  if comment.rstrip("\n") == "notes..." :
   print("The default comment was used")
   comment_tag="\t<notes>"+"No Comments or Notes!"+"</notes>\n"
  else:
   comment_tag="\t<notes>"+str(comment)+"</notes>\n"
  
  xclass_name=["\t<data_name>","</data_name>\n"]
  xclass_integ=["\t<integ>","</integ>\n"]
  xclass_owner=["\t<integ_owner>","</integ_owner>\n"]
  xclass_date=["\t<date>","</date>\n"]
  xclass_entry=["<"+str(datetime.datetime.now())+">\n","</"+str(datetime.datetime.now())+">\n"]
  phile=str(File_name.get_text())
  owner_name=str(owner.get_text()) 
  writefile=str(entry_write.get_text())
  writer=open(writefile,"a")

  if os.path.exists(phile):
   with open(phile,"r+b") as File:
    File_data=File.read(2048)
    hash_obj=hashlib.sha512()
    while File_data != b"":
     hash_obj.update(File_data)
     File_data=File.read(2048)
   integridity=hash_obj.hexdigest()
 
   data_name=str(File_name.get_text()) 
       ## add dialog stating name is required later
   integ=str(integridity)
  
   date_obj=datetime.datetime.now()
   date=str(date_obj.month)+"."+str(date_obj.day)+"."+str(date_obj.year)
   entrie=list()
   entrie.append(xclass_entry[0])
   entrie.append(xclass_name[0]+phile+xclass_name[1])
   entrie.append(xclass_integ[0]+integ+xclass_integ[1])
   entrie.append(xclass_owner[0]+owner_name+xclass_owner[1])
   entrie.append(xclass_date[0]+date+xclass_date[1])
   entrie.append(extraparts.date_extended())
   entrie.append(extraparts.interface_ip())
   entrie.append(extraparts.macaddress())
   entrie.append(extraparts.hostname())
   entrie.append(comment_tag)
   entrie.append(xclass_entry[1])
  
   entrie_buffer=""

   for i in entrie:
    #print(i)
    writer.write(i)
    entrie_buffer=entrie_buffer+i
   print(entrie_buffer)
   display_buffer.set_text(entrie_buffer)

  else:
   ##put a recovery dialog here
   print("Error! that file does not exist!")

win=window()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
