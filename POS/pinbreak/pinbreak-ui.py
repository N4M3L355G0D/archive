#! /usr/bin/python3

import gi,pinbreak,argparse, time,sql_tools
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import Pango
import os,sys
sys.path.insert(0,"./helpers")
import checks, entryCheck

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

"""
hostname="techzone.org"
uzer="store"
password="avalon"
database="cellular"
table="TRACKING"
"""
log="./log"
noSql=False
sql2 = "SELECT * FROM "+str(table)+" WHERE ( PHONE_NUMBER = '"+str(checks.phoneNumber(8045911321))+"' and ORDER_NUMBER ='"+checks.orderNumber(12345678)+"' and "+"USER = '"+str("test")+"' and "+"PLAN = '"+str(39.95)+"' and PIN = '"+str(checks.pincheck("12345678912345"))+"' and BILL_DATE = '"+str("1-10-1000")+"' and ACTIVATION = '"+str(0)+"');"
if entryCheck.readEntry(hostname,uzer,password,database,sql2) == False:
 print("NoServer, "+hostname+", Exists!")
 exit()


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Pinbreak")
        Gtk.Window.set_default_size(self,650,450)
        if os.path.exists(icon) and os.path.isfile(icon):
         Gtk.Window.set_icon_from_file(self,icon)

        grid=Gtk.Grid()
        self.add(grid)

        display=Gtk.TextView()
        display.set_wrap_mode(True)
        display.set_editable(False)
        display.modify_font(Pango.FontDescription('Arial 20'))
        display_buffer=display.get_buffer()
        display_buffer.set_text("Please enter a pin below")

        scrolldisplay=Gtk.ScrolledWindow()
        scrolldisplay.add(display)
        scrolldisplay.set_hexpand(True)
        scrolldisplay.set_vexpand(True)
        grid.attach(scrolldisplay,0,0,6,1)

        phoneNumber=Gtk.Entry()
        phoneNumber.set_text("Phone Number")
        grid.attach(phoneNumber,0,1,2,1)

        entry_write=Gtk.Entry()
        entry_write.set_text("Pin")
        grid.attach(entry_write,0,2,2,1)

        entryUser=Gtk.Entry()
        entryUser.set_text("User")
        grid.attach(entryUser,0,3,2,1)

        ordernumber=Gtk.Entry()
        ordernumber.set_text("Order Number")
        grid.attach(ordernumber,0,4,2,1)

        plan=Gtk.Entry()
        plan.set_text("Plan")
        grid.attach(plan,0,5,2,1)
        
        billdate=Gtk.Entry()
        billdate.set_text("Bill Date")
        grid.attach(billdate,0,6,2,1)

        activation=Gtk.CheckButton(label="New Activation")
        activation.connect("toggled",self.act)
        grid.attach(activation,3,1,2,1)

        result=Gtk.Button.new_with_mnemonic("_Okay")
        result.connect("clicked",self.pin,entry_write,display,display_buffer,entryUser,phoneNumber, ordernumber,plan,billdate,activation)
        grid.attach(result,0,7,2,1)

        close=Gtk.Button.new_with_mnemonic("_Close")
        close.connect("clicked",Gtk.main_quit)
        grid.attach(close,0,8,2,1)
        
        ping=Gtk.Button.new_with_mnemonic("_Ping")
        ping.connect("clicked",self.ping)
        grid.attach(ping,0,10,2,1)

        viewer=Gtk.Button.new_with_mnemonic("_Data Viewer")
        viewer.connect("clicked",self.readviewer)
        grid.attach(viewer,3,2,2,1)
        
    def readviewer(self,widget):
        print("Data Viewer clicked")
        os.system("python3 ./pinbreak-reader.py")
        print("Data Viewer closed")

    def act(self,widget):
        if widget.get_active():
            print("checked new activation")
        else:
            print("unchecked new activation")

    def ping(self,widget):
        print("Server Presence Indicator clicked")
        os.system("python3 indicator.py")
        print("Server Presence Indicator closed")

    def pin(self,widget,entry_write,display,display_buffer,entryUser,phoneNumber,ordernumber,plan,billdate,activation):
        if activation.get_active():
            activate=1
        else:
            activate=0
        """  logfile=open(log,"a") """
        if entry_write.get_text() == "Pin":
            display_buffer.set_text("Pin Cannot be Empty!")
        elif entryUser.get_text() == "User":
            display_buffer.set_text("User Cannot be Empty!")
        elif phoneNumber.get_text() == "Phone Number":
            display_buffer.set_text("Phone Number Cannot be Empty!")
        elif ordernumber.get_text() == "Order Number":
            display_buffer.set_text("Order Number Cannot be Empty!")
        elif plan.get_text() == "Plan":
            display_buffer.set_text("Plan cannot be Empty!")
        elif billdate.get_text() == "Bill Date":
            display_buffer.set_text("Bill Date cannot be Empty!")
        elif checks.phoneNumber(phoneNumber.get_text()) == "PN_long":		display_buffer.set_text("phone number is too long") 
        elif checks.phoneNumber(phoneNumber.get_text()) == "PN_short":
         display_buffer.set_text("phone number is too short")
        elif checks.pincheck(entry_write.get_text()) == "pin_!numbers_only":
         display_buffer.set_text("pin is not numbers only")
        elif checks.pincheck(entry_write.get_text()) == "pin_long":
         display_buffer.set_text("pin is too long")
        elif checks.pincheck(entry_write.get_text()) == "pin_short":
         display_buffer.set_text("pin is too short")
        elif checks.orderNumber(ordernumber.get_text()) == "on_!numbers_only":
         display_buffer.set_text("order number is not numbers only")
        elif checks.orderNumber(ordernumber.get_text()) == "ON_short":
         display_buffer.set_text("order number is too short")
        elif checks.orderNumber(ordernumber.get_text()) == "ON_long":
         display_buffer.set_text("order number is too long")
        else:
         a=pinbreak.pinbreak(entry_write.get_text(),entryUser.get_text())
         sql2 = "SELECT * FROM "+str(table)+" WHERE ( PHONE_NUMBER = '"+str(checks.phoneNumber(phoneNumber.get_text()))+"' and ORDER_NUMBER ='"+checks.orderNumber(ordernumber.get_text())+"' and "+"USER = '"+str(entryUser.get_text())+"' and "+"PLAN = '"+str(plan.get_text())+"' and PIN = '"+str(checks.pincheck(entry_write.get_text()))+"' and BILL_DATE = '"+str(billdate.get_text())+"' and ACTIVATION = '"+str(activate)+"');"
         if entryCheck.readEntry(hostname,uzer,password,database,sql2) == None:
          if noSql == False:
           ##sql support start
           sql=" INSERT INTO "+table+"(PHONE_NUMBER, ORDER_NUMBER, USER, PLAN, PIN, DATE,BILL_DATE,ACTIVATION) VALUES ("+"'"+checks.phoneNumber(phoneNumber.get_text())+"'"+",'"+checks.orderNumber(ordernumber.get_text())+"','"+entryUser.get_text()+"','"+plan.get_text()+"','"+checks.pincheck(entry_write.get_text())+"','"+time.ctime()+"','"+billdate.get_text()+"','"+str(activate)+"')"
           sql_tools.insertEntry(hostname,uzer,password,database,sql)
           print(sql)
           ## sql support end
 
          data="Order Number: "+str(checks.orderNumber(ordernumber.get_text()))+"\nPlan: "+str(plan.get_text())+str("\nPhone Number: "+checks.phoneNumber(phoneNumber.get_text()))+"\n"+str(a)+"\nBill Date: "+str(billdate.get_text()+"\nNew Activation: "+str(activate))
          display_buffer.set_text(data)
         else:
          display_buffer.set_text("that entry already exists")

          """         logfile.write(data+"\n--------------------\n")
          logfile.close() """
 
parser=argparse.ArgumentParser()
parser.add_argument("-l","--log",help="where to save the logfile")
parser.add_argument("-n","--no-sql",help="do not use sql support",action="store_true")
options=parser.parse_args()

if options.log:
    log=str(options.log)
if options.no_sql:
    noSql=True

win=Window()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()


