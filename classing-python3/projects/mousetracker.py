#! /usr/bin/env python3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os,sys
from events import *


class superior(QMainWindow):
    class win:
        master=None
        def __init__(self):
            super().__init__()
        
        def font(self):
            f=QFont('SansSerif',22)
            return f

        def initUI(self):
            self.master.setMouseTracking(True)
            self.master.setFont(self.font())
            self.master.setGeometry(300,300,300,300)
            self.master.setWindowTitle('Event Object')
            self.master.show()

    class layouts:
        master=None
        def tabs(self,widgetDict):
            tab=QTabWidget()
            for i in widgetDict.keys():
                tab.addTab(widgetDict[i],i)
            self.master.setCentralWidget(tab) 

        def layout(self):
            wid=QWidget(self.master)
            grid=QGridLayout()
            grid.setSpacing(10)
            #add widgets
            grid.addWidget(self.master.label.label('<b>X-Axis</b>'),0,1)
            grid.addWidget(self.master.label.label('<b>Y-Axis</b>'),0,0)
            grid.addWidget(self.master.lcdX,1,1)
            grid.addWidget(self.master.lcdY,1,0)
            #add widgets
            wid.setLayout(grid)
            return wid
    class labels:
        master=None
        def label(self,string):
            label=QLabel(string,self.master)
            return label

    class lcd:
        master=None
        def display(self):
            lcd=QLCDNumber(self.master)
            return lcd

    def mouseMoveEvent(self,event):
        y=event.y()
        x=event.x()

        self.lcdY.display(y)
        self.lcdX.display(x)

    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Escape:
            qApp.quit()

    def assembler(self):
        
        self.lcdObj=self.lcd()
        self.lcdObj.master=self
        self.lcdX=self.lcdObj.display()
        self.lcdY=self.lcdObj.display()

        self.label=self.labels()

        layout=self.layouts()
        layout.master=self
        layout.tabs({'Tab 1':layout.layout()})
        
        window=self.win()
        window.master=self
        window.initUI()

app=QApplication(sys.argv)
a=superior()
a.assembler()
sys.exit(app.exec_())
