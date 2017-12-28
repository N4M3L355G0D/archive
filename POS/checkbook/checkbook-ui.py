#! /usr/bin/python3

import gi,argparse
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import Pango
import receipt,checks

class window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="CheckBook")
        Gtk.Window.set_default_size(self,400,600)
        Gtk.Window.set_border_width(self,5)
        Gtk.Window.set_hexpand(self,False)
        """
        if os.path.exists(icon) and os.path.isfile(icon):
            Gtk.Window.set_icon_from_file(self,icon)
        """

        grid=Gtk.Grid()
        self.add(grid)

        self.display=Gtk.TextView()
        self.display.set_wrap_mode(True)
        self.display.set_editable(False)
        self.display.modify_font(Pango.FontDescription('Arial 14'))
        self.displaybuffer=self.display.get_buffer()
        self.displaybuffer.set_text("Please enter the receipt details below")
        self.scrolldisplay=Gtk.ScrolledWindow()
        self.scrolldisplay.add(self.display)
        self.scrolldisplay.set_hexpand(True)
        self.scrolldisplay.set_vexpand(True)
        
        box1=Gtk.Box()
        box1.set_border_width(3)
        box1.add(self.scrolldisplay)

        grid.attach(box1,0,0,2,1)
        
        self.subtotal=Gtk.Entry()
        self.subtotal.set_text("Subtotal")
        grid.attach(self.subtotal,0,1,2,1)

        self.tax=Gtk.Entry()
        self.tax.set_text("Tax")
        grid.attach(self.tax,0,2,2,1)

        self.totalsale=Gtk.Entry()
        self.totalsale.set_text("Total Sale")
        grid.attach(self.totalsale,0,3,2,1)

        self.date=Gtk.Entry()
        self.date.set_text("Date")
        grid.attach(self.date,0,4,2,1)

        self.store=Gtk.Entry()
        self.store.set_text("Store")
        grid.attach(self.store,0,5,2,1)

        self.user=Gtk.Entry()
        self.user.set_text("User")
        grid.attach(self.user,0,6,2,1)
        
        self.notes=Gtk.TextView()
        self.notes.set_wrap_mode(True)
        self.notes.set_editable(True)
        self.notesbuffer=self.notes.get_buffer()
        self.notesbuffer.set_text("Notes")
        self.notesDisplay=Gtk.ScrolledWindow()
        self.notesDisplay.add(self.notes)
        self.notesDisplay.set_hexpand(True)
        self.notesDisplay.set_vexpand(True)
        box2=Gtk.Box()
        box2.set_border_width(3)
        box2.add(self.notesDisplay)
        grid.attach(box2,0,7,2,1)
        
        ### start check buttons
        box3=Gtk.Box()
        box3.set_border_width(3)
        grid2=Gtk.Grid()
        box3.add(grid2)
        ## st
        self.clearSubtotal=Gtk.CheckButton(label="Subtotal Clr.")
        self.clearSubtotal.connect("toggled",self.clear,"Subtotal clr. checked")
        grid2.attach(self.clearSubtotal,0,0,1,1)
        ## tax
        self.clearTax=Gtk.CheckButton(label="Tax Clr.")
        self.clearTax.connect("toggled",self.clear,"Tax clr. checked")
        grid2.attach(self.clearTax,0,1,1,1)
        ## totalsale
        self.clearTotalsale=Gtk.CheckButton(label="Total Sale Clr.")
        self.clearTotalsale.connect("toggled",self.clear,"Total Sale clr. checked")
        grid2.attach(self.clearTotalsale,0,2,1,1)
        ## date
        self.clearDate=Gtk.CheckButton(label="Date Clr.")
        self.clearDate.connect("toggled",self.clear,"Date clr. checked")
        grid2.attach(self.clearDate,0,3,1,1)
        ##store
        self.clearStore=Gtk.CheckButton(label="Store Clr.")
        self.clearStore.connect("toggled",self.clear,"Store clr. checked")
        grid2.attach(self.clearStore,0,4,1,1)
        ##user
        self.clearUser=Gtk.CheckButton(label="User Clr.")
        self.clearUser.connect("toggled",self.clear,"User clr. checked")
        grid2.attach(self.clearUser,0,5,1,1)
        ## notes
        self.clearNotes=Gtk.CheckButton(label="Notes Clr.")
        self.clearNotes.connect("toggled",self.clear,"Notes clr. checked")
        grid2.attach(self.clearNotes,0,6,1,1)
        ## clear button
        self.clear=Gtk.Button.new_with_mnemonic(label="Clear")
        self.clear.connect("clicked",self.clearAction)
        grid2.attach(self.clear,0,7,1,1)

        grid.attach(box3,2,0,8,8)
        ### end checkbuttons
        submit=Gtk.Button.new_with_mnemonic("_Submit")
        submit.connect("clicked",self.submit)
        grid.attach(submit,0,8,1,1)

        close=Gtk.Button.new_with_mnemonic("_Close")
        close.connect("clicked",Gtk.main_quit)
        grid.attach(close,1,8,1,1)
    def clearAction(self,widget):
        ##set default text
        defaults=dict()
        defaultsList=["Subtotal","Tax","Total Sale","Date","Store","User","Notes"]
        for i in defaultsList:
            defaults[i]=i
        dAcc=""
        if self.clearSubtotal.get_active():
            self.subtotal.set_text(defaults["Subtotal"])
            dAcc=dAcc+defaults["Subtotal"]+" Cleared\n"
        if self.clearTax.get_active():
            self.tax.set_text(defaults["Tax"])
            dAcc=dAcc+defaults["Tax"]+" Cleared\n"
        if self.clearTotalsale.get_active():
            self.totalsale.set_text(defaults["Total Sale"])
            dAcc=dAcc+defaults["Total Sale"]+" Cleared\n"
        if self.clearDate.get_active():
            self.date.set_text(defaults["Date"])
            dAcc=dAcc+defaults["Date"]+" Cleared\n"
        if self.clearStore.get_active():
            self.store.set_text(defaults["Store"])
            dAcc=dAcc+defaults["Store"]+" Cleared\n"
        if self.clearUser.get_active():
            self.user.set_text(defaults["User"])
            dAcc=dAcc+defaults["User"]+" Cleared\n"
        if self.clearNotes.get_active():
            self.notesbuffer.set_text(defaults["Notes"])
            dAcc=dAcc+defaults["Notes"]+" Cleared\n"
        self.displaybuffer.set_text(dAcc)

    def clear(self,widget,text):
        if widget.get_active():
            print(text)
        else:
            print("!"+text)

    def submit(self,widget):
        fail=False
        try:
            test=float(self.subtotal.get_text())
        except:
            self.displaybuffer.set_text("Subtotal must be a number")
            fail=True
        try:
            test=float(self.tax.get_text())
        except:
            self.displaybuffer.set_text("Tax must be a number")
            fail=True
        try:
            test=float(self.totalsale.get_text())
        except:
            self.displaybuffer.set_text("Total Sale must be a number")
            fail=True

        if self.subtotal.get_text() == "Subtotal":
            self.displaybuffer.set_text("Subtotal cannot be 'Subtotal'")
        elif self.tax.get_text() == "Tax":
            self.displaybuffer.set_text("Tax cannot be 'Tax'")
        elif self.totalsale.get_text() == "Total Sale":
            self.displaybuffer.set_text("Total Sale cannot be 'Total Sale'")
        elif self.date.get_text() == "Date":
            self.displybuffer.set_text("Date cannot be 'Date'")
        elif self.store.get_text() == "Store":
            self.displaybuffer.set_text("Store cannot be 'Store'")
        elif self.user.get_text() == "User":
            self.displaybuffer.set_text("User cannot be 'User'")
        else:
            if fail == False:
                start,end=self.notesbuffer.get_bounds()
                text=self.notesbuffer.get_text(start,end,include_hidden_chars=False)
                data="Subtotal: "+self.subtotal.get_text()+"\nTax: "+self.tax.get_text()+"\nTotal Sale: "+self.totalsale.get_text()+"\nDate: "+self.date.get_text()+"\nStore: "+self.store.get_text()+"\nUser: "+self.user.get_text()+"\n=== Notes ===\n"+text
                print(data)
                receipt.checkRun(float(self.subtotal.get_text()),float(self.tax.get_text()),float(self.totalsale.get_text()),self.date.get_text(),self.store.get_text(),self.user.get_text(),text)
                self.displaybuffer.set_text(data)          
win=window()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
