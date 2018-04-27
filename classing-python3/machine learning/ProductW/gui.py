#! /usr/bin/python3
#productw a homebrew product scanner to scan codes from various sources, this is just the gui, right now

import cv2,numpy
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os,sys,time,threading
from PyQt5.QtMultimediaWidgets import *

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
            self.master.setGeometry(300,300,300,300)
            self.master.setWindowTitle('ProductW')
            self.master.show()
    class labels:
        master=None

        def lbls(self):
            self.ctrLbl=QLabel('ProductW',self.master)

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
            print(self.master.camera.frame)
            self.master.img.pix.setPixmap(self.master.img.framy())

        def timer(self):
            timer=QTimer(self.master)
            timer.timeout.connect(self.timerAction)
            timer.start(0.01)
    class buttons:
        master=None
        def snapperAction(self):
            frame=self.master.camera.frame
            #the line below will be swapped later
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
            
    class layouts:
        master=None
        def tabs(self,widgetDict):
            tab=QTabWidget()
            for i in widgetDict.keys():
                tab.addTab(widgetDict[i],i)
            self.master.setCentralWidget(tab)

        def layout1(self):
            widget=QWidget(self.master)
            grid=QGridLayout()
            grid.setSpacing(10)
            #add widgets
            grid.addWidget(self.master.labels.ctrLbl,0,0,1,1)
            grid.addWidget(self.master.img.pix,0,1,1,1)
            grid.addWidget(self.master.buttons.snap,1,0,1,2)
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
            t=threading.Thread(target=self.master.camera.grab)
            t.start()
            self.master.buttons.snapper()
            self.master.buttons.quitBtn()
            self.master.img.display()
            self.master.labels.lbls()
            self.master.ti.timer()
            self.master.layouts.tabs({'Capture':self.master.layouts.layout1(),'Quit':self.master.layouts.layoutQuit()})
            self.master.win.initUi()

    def assembler(self):
        wa=self.void()
        wa.master=wa
        wa.win=self.win()
        wa.win.master=wa
        wa.docRoot="."
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

ap=QApplication(sys.argv)
if __name__ == "__main__":
    app=container()
    app.assembler()
    result=ap.exec_()
    app.camera.running=False
    sys.exit(result)
