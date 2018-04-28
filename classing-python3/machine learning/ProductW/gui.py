#! /usr/bin/python3
#productw a homebrew product scanner to scan codes from various sources, this is just the gui, right now

import cv2,numpy
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os,sys,time,threading
from PyQt5.QtMultimediaWidgets import *

#add local libs path
sys.path.insert(0,"src/lib")
#import local libs
import readbarCode
import settings

class container(QMainWindow):
    class camera:
        running=True
        master=None
        frame=None
        def grab(self):
            frame=cv2.VideoCapture(0)
            while self.running:
                frame.grab()
                retval,img=frame.retrieve(0)
                self.frame=img
    class win:
        master=None
        def __init__(self):
            super().__init__()

        def initUi(self):
            self.master.setGeometry(200,200,300,300)
            screenCenter=QDesktopWidget().availableGeometry().center()
            windowGeo=self.master.frameGeometry()
            windowGeo.moveCenter(screenCenter)
            self.master.move(windowGeo.topLeft())
            self.master.setWindowTitle('ProductW')
            self.master.statusBar()
            imgP=os.path.abspath(os.path.join(self.master.docRoot,"src/icons/windowIcon.png"))
            imgP=QIcon(imgP)
            self.master.setWindowIcon(imgP)
            self.master.show()

    class labels:
        master=None
        def run(self):
            self.lbls()
            self.lblCode()
            self.lblCodeData()
            self.lblApiKey()

        def lbls(self):
            self.ctrLbl=QLabel('ProductW',self.master)
        def lblCode(self):
            self.codeDataLbl=QLabel('Product Code:',self.master)
        def lblCodeData(self):
            self.codeDataData=QLabel('Nothing Scanned yet!',self.master)
        def lblApiKey(self):
            self.apiKey=QLabel("API Key:",self.master)

    class img:
        master=None
        pix=None
        def framy(self):
            frame=self.master.camera.frame
            while type(frame) != numpy.ndarray:
                frame=self.master.camera.frame
                print(type(frame))
            h=frame.shape[0]
            w=frame.shape[1]
            bpl=w*3
            qimg=QImage(self.master.camera.frame,
                    w,h,bpl,QImage.Format_RGB888)
            pix=QPixmap.fromImage(qimg)
            return pix

        def display(self):
            label=QLabel(self.master)
            pix=self.framy()
            label.setPixmap(pix)
            self.pix=label

    class timer:
        master=None
        def timerAction(self):
            self.master.labels.ctrLbl.setText(time.ctime())
            self.master.img.pix.setPixmap(self.master.img.framy())

        def timer(self):
            timer=QTimer(self.master)
            timer.timeout.connect(self.timerAction)
            timer.start(0.01)

    class lineEdits:
        master=None
        def codeData(self):
            self.codeDataData=QLineEdit()
            self.codeDataData.setReadOnly(True)

        def apiKey(self):
            self.apikey=QLineEdit()
            self.apikey.setText(self.master.apikey)
            self.apikey.setEnabled(False)

    class checkboxes:
        master=None
        def run(self):
            self.newKey()
        
        def newKeyAction(self):
            if self.newkey.isChecked():
                self.master.buttons.addKey.setEnabled(True)
                self.master.lineEdits.apikey.setEnabled(True)
            else:
                self.master.buttons.addKey.setEnabled(False)
                self.master.lineEdits.apikey.setEnabled(False)

        def newKey(self):
            self.newkey=QCheckBox('Add New API Key',self.master)
            self.newkey.stateChanged.connect(self.newKeyAction)

    class buttons:
        master=None
        def run(self):
            self.snapper()
            self.quitBtn()
            self.addKeyBtn()

        def snapperAction(self):
            frame=self.master.camera.frame
            #the line below will be swapped later
            result=self.master.reader.readbars(frame,mem=True)
            if result != False:
                result=result[0]
                self.master.lineEdits.codeDataData.setText(result.data.decode())
                self.master.layouts.tabs.setCurrentIndex(1)
            cv2.imwrite("snap.png",frame)
            self.master.statusBar().showMessage("img grabbed")
        def snapper(self):
            self.snap=QPushButton('Snap')
            self.snap.clicked.connect(self.snapperAction)
            self.snap.setIcon(QIcon(os.path.join(self.master.docRoot,'src/icons/snap.png')))

        def quitBtn(self):
            self.done=QPushButton("Quit")
            self.done.clicked.connect(self.quitAction)
            self.done.setIcon(QIcon(os.path.join(self.master.docRoot,'src/icons/exit.png')))
        def quitAction(self):
            qApp.quit()

        def addKeyAction(self):
            apikey=self.master.lineEdits.apikey.text()
            db=self.master.db
            if apikey != self.master.apikey:
                self.master.settings.insertNewDefault(db,'apikey',apikey)
                self.master.statusBar().showMessage('API Key added!')
            else:
                self.master.statusBar().showMessage('API Key is already set!')

        def addKeyBtn(self):
            self.addKey=QPushButton('Add Key')
            self.addKey.clicked.connect(self.addKeyAction)
            self.addKey.setIcon(QIcon(os.path.join(self.master.docRoot,'src/icons/key.png')))
            self.addKey.setEnabled(False)

    class layouts:
        master=None
        def tabs(self,widgetDict):
            self.tabs=QTabWidget()
            for i in widgetDict.keys():
                self.tabs.addTab(widgetDict[i],i)
            self.master.setCentralWidget(self.tabs)

        def layout1(self):
            widget=QWidget(self.master)
            grid=QGridLayout()
            grid.setSpacing(10)
            #add widgets
            grid.addWidget(self.master.labels.ctrLbl,0,0,1,1)
            grid.addWidget(self.master.img.pix,1,0,1,1)
            grid.addWidget(self.master.buttons.snap,2,0,1,1)
            widget.setLayout(grid)
            return widget
        
        def layoutData(self):
            widget=QWidget(self.master)
            grid=QGridLayout()
            grid.setSpacing(10)
            #widgets
            grid.addWidget(self.master.labels.codeDataLbl,0,0,1,2)
            grid.addWidget(self.master.lineEdits.codeDataData,0,3,1,4)
            widget.setLayout(grid)
            widget.setStyleSheet("border: 1px solid lightgray")
            return widget

        def layoutSettings(self):
            widget=QWidget(self.master)
            grid=QGridLayout()
            grid.setSpacing(5)
            #add settings widget
            grid.addWidget(self.master.labels.apiKey,0,0,1,1)
            grid.addWidget(self.master.lineEdits.apikey,0,1,1,3)
            grid.addWidget(self.master.buttons.addKey,0,4,1,1)
            grid.addWidget(self.master.checkboxes.newkey,1,0,1,1)
            widget.setLayout(grid)
            return widget

        def layoutQuit(self):
            widget=QWidget(self.master)
            grid=QGridLayout()
            grid.setSpacing(10)
            #add widgets
            grid.addWidget(self.master.buttons.done,0,1,1,5)
            widget.setLayout(grid)
            return widget

    class void(QMainWindow):
        master=None

    class tasks:
        master=None
        def run(self):
            self.master.db=self.master.settings.initSettings()
            self.master.settings.getSettings(self.master.db)
            t=threading.Thread(target=self.master.camera.grab)
            t.start()
            self.master.checkboxes.run()
            self.master.buttons.run()
            self.master.img.display()
            self.master.labels.run()
            self.master.lineEdits.codeData()
            self.master.lineEdits.apiKey()
            self.master.ti.timer()
            self.master.layouts.tabs(
            {
                'Capture':self.master.layouts.layout1(),
                'Data':self.master.layouts.layoutData(),
                'Settings':self.master.layouts.layoutSettings(),
                'Quit':self.master.layouts.layoutQuit(),
            }
            )
            self.master.win.initUi()

    def assembler(self):
        wa=self.void()
        wa.master=wa
        wa.win=self.win()
        wa.win.master=wa
        wa.docRoot="."
        
        wa.checkboxes=self.checkboxes()
        wa.checkboxes.master=wa

        wa.settings=settings.settings()
        wa.settings.master=wa

        wa.lineEdits=self.lineEdits()
        wa.lineEdits.master=wa

        wa.reader=readbarCode.readBars()
        wa.reader.master=wa

        wa.camera=self.camera()
        wa.camera.master=wa

        wa.img=self.img()
        wa.img.master=wa
        
        wa.buttons=self.buttons()
        wa.buttons.master=wa


        wa.ti=self.timer()
        wa.ti.master=wa

        wa.labels=self.labels()
        wa.labels.master=wa

        wa.layouts=self.layouts()
        wa.layouts.master=wa

        wa.tasks=self.tasks()
        wa.tasks.master=wa
        wa.tasks.run()
        self.closingAccess=wa

ap=QApplication(sys.argv)
if __name__ == "__main__":
    app=container()
    app.assembler()
    result=ap.exec_()
    app.camera.running=False
    app.closingAccess.settings.closeDb()
    sys.exit(result)
