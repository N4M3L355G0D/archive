#! /usr/bin/python3

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import passgen


class Window(Gtk.Window):
 def __init__(self):
  Gtk.Window.__init__(self,title="Keygen.sh")
  Gtk.Window.set_default_size(self,300,200)  
  self.set_border_width(10)
  
  headerbar=Gtk.HeaderBar()
  headerbar.set_show_close_button(True)
  headerbar.props.title="Keygen"
  self.set_titlebar(headerbar)
  
  grid=Gtk.Grid()
  self.add(grid)

  display=Gtk.TextView()
  display.set_wrap_mode(True)
  display.set_editable(False)
  display_buffer=display.get_buffer()
  display_buffer.set_text("Password not Generated yet")

  scrollDisplay=Gtk.ScrolledWindow()
  scrollDisplay.add(display)
  scrollDisplay.set_hexpand(True)
  scrollDisplay.set_vexpand(True)
  grid.attach(scrollDisplay,1,0,1,1)
  
  button1=Gtk.Button.new_with_mnemonic(label="_Generate Key")
  button1.connect("clicked",self.key,display,display_buffer)
  grid.attach(button1,1,1,1,1)

  close=Gtk.Button.new_with_mnemonic(label="_Close")
  close.connect("clicked",Gtk.main_quit)
  grid.attach(close,1,2,1,1)
  
 def key(self,widget,display,display_buffer):
  result=passgen.keygen()
  display_buffer.set_text(str(result))

win=Window()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
