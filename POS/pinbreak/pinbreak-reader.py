#! /usr/bin/python3

import gi,argparse, time,sql_tools
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import Pango
import os,sys,subprocess
sys.path.insert(0,"./helpers")
import dump2html
'''import dump2html_repeats'''
import checks,entryCheck
nl="\n"
hostname=""
uzer=""
database=""
password=""
table=""
icon=""

CFG="./pinbreak.cfg"
if os.path.exists(CFG) and os.path.isfile(CFG):
 with open(CFG,"r") as cfg:
  for i in cfg:
   if len(i.split("=")) > 1:
    varName=i.split("=")[0]
    varVal=i.split("=")[1]
    if varName == "hostname":
     hostname=varVal.rstrip(nl)
    if varName == "uzer":
     uzer=varVal.rstrip(nl)
    if varName == "database":
     database=varVal.rstrip(nl)
    if varName == "password":
     password=varVal.rstrip(nl)
    if varName == "table":
     table=varVal.rstrip(nl)
    if varName == "icon":
     icon=varVal.rstrip(nl)
else:
    print("configuration file does not exist! quitting!")
    exit()

sql2 = "SELECT * FROM "+str(table)+" WHERE ( PHONE_NUMBER = '"+str(checks.phoneNumber(8045911321))+"' and ORDER_NUMBER ='"+checks.orderNumber(12345678)+"' and "+"USER = '"+str("test")+"' and "+"PLAN = '"+str(39.95)+"' and PIN = '"+str(checks.pincheck("12345678912345"))+"' and BILL_DATE = '"+str("1-10-1000")+"' and ACTIVATION = '"+str(0)+"');"
if entryCheck.readEntry(hostname,uzer,password,database,sql2) == False:
 print("NoServer, "+hostname+", Exists!")
 exit()

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Pinbreak Reader")
        Gtk.Window.set_default_size(self,1050,450)
        if os.path.exists(icon) and os.path.isfile(icon):
         Gtk.Window.set_icon_from_file(self,icon)

        grid=Gtk.Grid()
        self.add(grid)

        display=Gtk.TextView()
        display.set_wrap_mode(True)
        display.set_editable(False)
        display.modify_font(Pango.FontDescription('Arial 12'))
        display_buffer=display.get_buffer()
        display_buffer.set_text("Nothing to display yet")

        scrollDisplay=Gtk.ScrolledWindow()
        scrollDisplay.add(display)
        scrollDisplay.set_hexpand(True)
        scrollDisplay.set_vexpand(True)
        grid.attach(scrollDisplay,0,0,7,1)

        fieldGet=Gtk.Entry()
        fieldGet.set_text("BILL_DATE")
        grid.attach(fieldGet,0,1,2,1)        

        rb1=Gtk.RadioButton.new_with_label_from_widget(None,label="BILL_DATE")
        rb1.connect("toggled",self.fields,"BILL_DATE",fieldGet)
        rb1.set_active(True)
        grid.attach(rb1,4,6,1,1)
        
        rb2=Gtk.RadioButton.new_from_widget(rb1)
        rb2.set_label("PHONE_NUMBER")
        rb2.connect("toggled",self.fields,"PHONE_NUMBER",fieldGet) 
        grid.attach(rb2,3,4,1,1)        
        
        rb3=Gtk.RadioButton.new_from_widget(rb1)
        rb3.set_label("ORDER_NUMBER")
        rb3.connect("toggled",self.fields,"ORDER_NUMBER",fieldGet)
        grid.attach(rb3,3,5,1,1)
        
        rb4=Gtk.RadioButton.new_from_widget(rb1)
        rb4.set_label("PLAN")
        rb4.connect("toggled",self.fields,"PLAN",fieldGet)
        grid.attach(rb4,3,6,1,1)
       
        rb5=Gtk.RadioButton.new_from_widget(rb1)
        rb5.set_label("USER")
        rb5.connect("toggled",self.fields,"USER",fieldGet)
        grid.attach(rb5,2,4,1,1)

        rb6=Gtk.RadioButton.new_from_widget(rb1)
        rb6.set_label("PIN")
        rb6.connect("toggled",self.fields,"PIN",fieldGet)
        grid.attach(rb6,2,5,1,1)


        rb7=Gtk.RadioButton.new_from_widget(rb1)
        rb7.set_label("ACTIVATION")
        rb7.connect("toggled",self.fields,"ACTIVATION",fieldGet)
        grid.attach(rb7,2,6,1,1)
 
        export=Gtk.CheckButton(label="Export")
        export.connect("toggled",self.Export)
        grid.attach(export,2,2,1,1)

        exportDisplay=Gtk.TextView()
        exportDisplay.set_editable(False)
        export_buffer=exportDisplay.get_buffer()
        exportDisplay.modify_font(Pango.FontDescription('Arial 12'))
        export_buffer.set_text("Errors: 0")        

        bold=export_buffer.create_tag("bold",weight=Pango.Weight.BOLD)
        grid.attach(exportDisplay,5,4,2,3)

        total=Gtk.CheckButton(label="Totals")
        total.connect("toggled",self.totalled,export)
        grid.attach(total,2,1,1,1)

        fieldValue=Gtk.Entry()
        fieldValue.set_text("Value")
        grid.attach(fieldValue,0,2,2,1)
        
        repeated=Gtk.Button.new_with_mnemonic("_Repeats")
        repeated.connect("clicked",self.repeats,display,display_buffer,total,export,export_buffer)
        grid.attach(repeated,0,5,2,1)

        
       
        submit=Gtk.Button.new_with_mnemonic("_Submit")
        submit.connect("clicked",self.dataGet,fieldGet,fieldValue,display,display_buffer,total,export,exportDisplay,export_buffer)
        grid.attach(submit,0,4,2,1)


        close=Gtk.Button.new_with_mnemonic("_Close")
        close.connect("clicked",Gtk.main_quit)
        grid.attach(close,0,6,2,1)
    def fields(self,widget,text,fieldGet):
     if widget.get_active():
      print(text+" selected" )
      fieldGet.set_text(text)

    def Export(self,widget):
     if widget.get_active():
      print("checked export")
     else:
      print("uncheck export")

    def repeats(self,widget,display,display_buffer,total,export,export_buffer):
        print("Repeats clicked")
        if total.get_active():
         if export.get_active():
          cmdString="python3 ./helpers/readDupsExport.py"
         else:
          cmdString="python3 ./helpers/readDupsTotal.py"
        else:
         if export.get_active():
          cmdString="python3 ./helpers/readDupsExport.py --nt"
         else:
          cmdString="python3 ./helpers/readDups.py"
        data=subprocess.Popen(cmdString,shell=True,stdout=subprocess.PIPE)
        dString,err=data.communicate()
        print(dString.decode())
        display_buffer.set_text("\t\t-=Field Order=-\n\nPHONE_NUMBER | PLAN | Renewals Count\n\n\t\t-=Fields=-\n\n"+dString.decode())
        if export.get_active():
         export_buffer.set_text("Exported to: "+dump2html.expo2())
        else:
         export_buffer.set_text("Errors: 0")
    def totalled(self,widget,export):
        if widget.get_active():
            #export.set_sensitive(False)
            print("checked totals")
        else:
            print("unchecked totals")
            export.set_sensitive(True)

    def dataGet(self,widget,fieldGet,fieldValue,display,display_buffer,total,export,exportDisplay,export_buffer):
        if export.get_active():
         if fieldGet.get_text() == "Field":
             display_buffer.set_text("Field cannot be 'Field'")
             export_buffer.set_text("ERRORS: 'Field'")
         elif fieldValue.get_text() == "Value":
             display_buffer.set_text("Value cannot be 'Value'")
             export_buffer.set_text("ERRORS: 'Value'")
         else:
             if total.get_active():
              cmdString="python ./helpers/readEntry.py -e -f "+str(fieldGet.get_text())+" -v "+str(fieldValue.get_text())+" | helpers/total.awk"
             else:
              cmdString="python ./helpers/readEntry.py -e -f "+str(fieldGet.get_text())+" -v "+str(fieldValue.get_text())
             data=subprocess.Popen(cmdString,shell=True,stdout=subprocess.PIPE)
             string,err=data.communicate()
             print(string.decode())
             display_buffer.set_text("Data was Exported to htmlexport.html\n\n\t\t-=Field  Order=-\n\nPHONE_NUMBER | ORDER_NUMBER | PLAN | USER | PIN | DATE | BILL_DATE | ACTIVATION\n\n\t\t-=Fields=-\n\n"+string.decode())
             export_buffer.set_text("Exported to: "+dump2html.expo())     
        else:
         if fieldGet.get_text() == "Field":
             display_buffer.set_text("Field cannot be 'Field'")
             export_buffer.set_text("ERRORS: 'Field'")
         elif fieldValue.get_text() == "Value":
             display_buffer.set_text("Value cannot be 'Value'")
             export_buffer.set_text("ERRORS: 'Value'")
         else:
             if total.get_active():
              cmdString="python ./helpers/readEntry.py -f "+str(fieldGet.get_text())+" -v "+str(fieldValue.get_text())+" | helpers/total.awk"
             else:
              cmdString="python ./helpers/readEntry.py -f "+str(fieldGet.get_text())+" -v "+str(fieldValue.get_text())
             data=subprocess.Popen(cmdString,shell=True,stdout=subprocess.PIPE)
             string,err=data.communicate()
             print(string.decode())
             display_buffer.set_text("\t\t-=Field  Order=-\n\nPHONE_NUMBER | ORDER_NUMBER | PLAN | USER | PIN | DATE | BILL_DATE | ACTIVATION\n\n\t\t-=Fields=-\n\n"+string.decode())
             export_buffer.set_text("ERRORS: 0")

win=Window()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()

