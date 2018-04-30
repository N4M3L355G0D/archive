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
import dataTab,getproduct

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
            self.master.setStyleSheet('font: 14pt Sans Serif')
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
            self.apiKey=QLabel("API Key",self.master)

    class img:
        master=None
        pix=None
        write=False
        def lastBarcode(self):
            self.lastbar=QLabel(self.master)

        def lastBarcodeUpdate(self,frame):
            qimg=self.framy(frame)
            qimg=QPixmap(qimg)
            qimg=qimg.scaled(50,50,Qt.KeepAspectRatio,Qt.FastTransformation)
            self.lastbar.setPixmap(qimg)
            self.lastbar.setStyleSheet("border: 0px solid black")

        def framy(self,frame=None):
            if type(frame) == None:
                frame=self.master.camera.frame
            if self.write == True:
                cv2.imwrite(os.path.join(self.master.docRoot,"src/tmp/snap.png"),frame)
                self.write=False
            while type(frame) != numpy.ndarray:
                frame=self.master.camera.frame
                #print(type(frame))
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
        reset=True
        def timerAction(self):
            self.master.labels.ctrLbl.setText(time.ctime())
            self.master.img.pix.setPixmap(self.master.img.framy())
            if self.master.settings.autosnap == True:
                self.master.buttons.snapperAction()
        
        def timer(self):
            timer=QTimer(self.master)
            timer.timeout.connect(self.timerAction)
            timer.start(0.001)

    class lineEdits:
        master=None
        def codeData(self):
            self.codeDataData=QTextEdit()
            self.codeDataData.setReadOnly(True)

        def apiKey(self):
            self.apikey=QLineEdit()
            self.apikey.setText(self.master.apikey)
            self.apikey.setStyleSheet('font: 10pt Sans Serif')
            self.apikey.setEnabled(False)

    class checkboxes:
        master=None
        def run(self):
            self.newKey()
            self.autoSnap()
        
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

        def autoSnap(self):
            self.autosnap=QCheckBox('Auto Snap',self.master)
            if self.master.settings.autosnap == False:
                self.autosnap.setChecked(False)
            else:
                self.autosnap.setChecked(True)
            self.autosnap.stateChanged.connect(self.autoSnapAction)

        def autoSnapAction(self):
            if self.autosnap.isChecked():
                self.master.buttons.snap.setEnabled(False)
                self.master.settings.autosnap=True
                self.master.settings.updateSettings(self.master.db,'autosnap','True')
            else:
                self.master.buttons.snap.setEnabled(True)
                self.master.settings.autosnap=False
                self.master.settings.updateSettings(self.master.db,'autosnap','False')

    class buttons:
        master=None
        def run(self):
            self.snapper()
            self.quitBtn()
            self.addKeyBtn()

        def snapperAction(self):
            frame=self.master.camera.frame
            result=self.master.reader.readbars(frame,mem=True)
            if result != False:
                result=result[0]
                res=result.data.decode()
                if type(res) == str:
                    if len(res) > 0:
                        if res[0] == '0':
                            res=res[1:]
                self.master.lineEdits.codeDataData.setText(res)
                if self.master.layouts.tabs.currentIndex() < 1:
                    self.master.img.write=True
                    self.master.img.lastBarcodeUpdate(frame)
                    data=self.master.getproduct.flattenData(res)
                    self.master.datTab.labelsUpdate(data)
                    self.master.layouts.tabs.setCurrentIndex(1)
                    self.master.statusBar().showMessage("Done!")

        def snapper(self):
            self.snap=QPushButton('Snap')
            self.snap.clicked.connect(self.snapperAction)
            self.snap.setIcon(QIcon(os.path.join(self.master.docRoot,'src/icons/camera.png')))
            self.snap.setIconSize(QSize(40,40))
            self.snap.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            if self.master.settings.autosnap == True:
                self.snap.setEnabled(False)
            else:
                self.snap.setEnabled(True)

        def quitBtn(self):
            self.done=QPushButton("  Quit")
            self.done.clicked.connect(self.quitAction)
            self.done.setIcon(QIcon(os.path.join(self.master.docRoot,'src/icons/exit.png')))
            self.done.setIconSize(QSize(80,80))
            self.done.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
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
            self.addKey=QPushButton(' Add Key')
            self.addKey.clicked.connect(self.addKeyAction)
            self.addKey.setIcon(QIcon(os.path.join(self.master.docRoot,'src/icons/key.png')))
            self.addKey.setIconSize(QSize(40,40))
            self.addKey.setStyleSheet('font: 10pt Sans Serif')
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
            grid.addWidget(self.master.buttons.snap,2,0,3,1)
            widget.setLayout(grid)
            return widget
        
        def layoutData(self):
            widget=QWidget(self.master)
            grid=QGridLayout()
            grid.setSpacing(10)
            #widgets
            
            grid.addWidget(self.master.labels.codeDataLbl,0,0,1,1)
            grid.addWidget(self.master.lineEdits.codeDataData,0,1,1,1)
            grid.addWidget(self.master.img.lastbar,0,5,1,1)
            for num,lbl in enumerate(self.master.datTab.lbls.keys()):
                grid.addWidget(self.master.datTab.lbls[lbl],1+num,0,1,1)
            for num,lbl in enumerate(self.master.datTab.edits.keys()):
                grid.addWidget(self.master.datTab.edits[lbl],1+num,1,1,1)

            widget.setLayout(grid)
            widget.setStyleSheet("border: 1px solid lightgray")
            
            scroll=QScrollArea()
            scroll.setWidget(widget)
            scroll.setWidgetResizable(True)
            scroll.setStyleSheet("""border: 1px solid black;
                                    font-size: 12px;""")
            return scroll

        def layoutSettings(self):
            widget=QWidget(self.master)
            grid=QGridLayout()
            grid.setSpacing(5)
            #add settings widget
            div1=QWidget(self.master)
            grid1=QGridLayout()
            grid1.setSpacing(5)
            #add widgets here
            grid1.addWidget(self.master.labels.apiKey,0,0,1,1)
            grid1.addWidget(self.master.lineEdits.apikey,0,1,1,3)
            grid1.addWidget(self.master.buttons.addKey,0,4,1,1)
            grid1.addWidget(self.master.checkboxes.newkey,1,4,1,1)
            grid1.addWidget(self.master.checkboxes.autosnap,1,3,1,1)
            div1.setLayout(grid1)

            div2=QWidget(self.master)
            grid2=QGridLayout()
            grid2.setSpacing(5)
            #add widgets here
            div2.setLayout(grid2)

            div3=QWidget(self.master)
            grid3=QGridLayout()
            grid3.setSpacing(5)
            #add widgets here
            div3.setLayout(grid3)

            
            grid.addWidget(div1,0,0,1,1)
            grid.addWidget(div2,1,0,1,1)
            grid.addWidget(div3,2,0,1,1)

            widget.setLayout(grid)
            return widget

        def layoutQuit(self):
            widget=QWidget(self.master)
            grid=QGridLayout()
            grid.setSpacing(10)

            div1=QWidget(self.master)
            grid1=QGridLayout()
            grid1.setSpacing(5)
            #add widgets here
            div1.setLayout(grid1)

            div2=QWidget(self.master)
            grid2=QGridLayout()
            grid2.setSpacing(5)
            #add widgets here
            div2.setLayout(grid2)

            div3=QWidget(self.master)
            grid3=QGridLayout()
            grid3.setSpacing(5)
            #add widgets here
            div3.setLayout(grid3)

            div4=QWidget(self.master)
            grid4=QGridLayout()
            grid4.setSpacing(5)
            #add widgets here
            div4.setLayout(grid4)

            div5=QWidget(self.master)
            grid5=QGridLayout()
            grid5.setSpacing(5)
            grid5.addWidget(self.master.buttons.done,0,0,3,2) 
            #add widgets here
            div5.setLayout(grid5)

            div6=QWidget(self.master)
            grid6=QGridLayout()
            grid6.setSpacing(5)
            #add widgets here
            div6.setLayout(grid6)

            div7=QWidget(self.master)
            grid7=QGridLayout()
            grid7.setSpacing(5)
            #add widgets here
            div7.setLayout(grid7)

            div8=QWidget(self.master)
            grid8=QGridLayout()
            grid8.setSpacing(5)
            #add widgets here
            div8.setLayout(grid8)

            div9=QWidget(self.master)
            grid9=QGridLayout()
            grid9.setSpacing(5)
            #add widgets here
            div9.setLayout(grid9)

            #add widgets
            grid.addWidget(div1,0,0,1,1)
            grid.addWidget(div2,0,1,1,1)
            grid.addWidget(div3,0,2,1,1)

            grid.addWidget(div4,1,0,1,1)
            grid.addWidget(div5,1,1,1,1)
            grid.addWidget(div6,1,2,1,1)

            grid.addWidget(div7,2,0,1,1)
            grid.addWidget(div8,2,1,1,1)
            grid.addWidget(div9,2,2,1,1)
            widget.setLayout(grid)
            return widget

    class void(QMainWindow):
        master=None

    class tasks:
        master=None
        def run(self):
            if not os.path.exists(os.path.realpath(os.path.join(self.master.docRoot,'src/tmp'))):
                os.mkdir(os.path.realpath(os.path.join(self.master.docRoot,'src/tmp')))
            self.master.db=self.master.settings.initSettings()
            self.master.settings.getSettings(self.master.db)
            t=threading.Thread(target=self.master.camera.grab)
            t.start()
            self.master.getproduct.apikey=self.master.apikey
            data=self.master.getproduct.initFields()
            self.master.datTab.labels(data)
            self.master.checkboxes.run()
            self.master.buttons.run()
            self.master.img.display()
            self.master.img.lastBarcode()
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
        
        wa.getproduct=getproduct.getproducts()
        wa.getproduct.master=wa

        wa.checkboxes=self.checkboxes()
        wa.checkboxes.master=wa

        wa.settings=settings.settings()
        wa.settings.master=wa

        wa.datTab=dataTab.dataTab()
        wa.datTab.master=wa
        
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
