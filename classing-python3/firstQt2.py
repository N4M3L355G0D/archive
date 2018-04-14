import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QApplication,QMainWindow,qApp,QAction,QMenu,QGridLayout,QLabel,QLineEdit,QTextEdit,QFormLayout,QTabWidget

import os,zipfile
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
#left off from context menus

class orvil(QMainWindow):
    ext="zip"
    class actions:
        okMsg="Okay"
        qMsg="Quit"
        #master will be populated with the object 'example'
        master=None
        ERR_BADPATH="{}:Path does not exist: '{}'"
        def backup(self,ipath,opath):
            if ipath == "rootFS":
                ipath="/"
            print("'{}' -> '{}'".format(ipath,opath))
            self.createZipCounter(ipath)
            self.createZip(opath,ipath)

        def createZipCounter(self,path):
            counter=0
            for root,dir,fnames in os.walk(path,topdown=True):
                for fname in fnames:
                    self.master.statusBar().showMessage("[{}] counting: {}".format(counter,os.path.join(root,fname)))
                    counter+=1
            self.master.statusBar().showMessage("{} files/dirs!".format(counter))
            self.fcount=counter

        def createZip(self,zipName,path,FULLPATH=False,custom=''):
            arcpath=os.path.split(path)[0]
            z=zipfile.ZipFile(zipName,'w',compression=zipfile.ZIP_LZMA)
            counter=0
            for root,dir,fnames in os.walk(path,topdown=True):
                for fname in fnames:
                    if custom == '':
                        if FULLPATH == False:
                            z.write(os.path.join(root,fname),os.path.join(root.replace(arcpath,''),fname))
                        else:
                            z.write(os.path.join(root,fname),os.path.join(root,fname))
                    else:
                        z.write(os.path.join(root,fname),os.path.join(custom,fname))
                    self.master.statusBar().showMessage("{}/{}".format(counter,self.fcount))
                    counter+=1


        def okay(self,statusBar,msg=None):
            if msg == None:
                text=self.master.edits.text.text()
                otextObj=self.master.edits.otext
                otext=otextObj.text()
                if os.path.exists(text):
                    print(self.okMsg,text)
                    statusBar.showMessage("{}: '{}'".format(self.okMsg,text))
                    if otext == '':
                        bname=os.path.basename(text)
                        if bname == '':
                            text='rootFS'
                        fname='{}.{}'.format(bname,self.master.ext)
                        otextObj.setText(fname)
                        otext=otextObj.text()
                        self.backup(text,otext)
                    else:
                        path=os.path.dirname(otext)
                        if path == '':
                            path='.'
                        if not os.path.exists(path):
                            print(self.ERR_BADPATH.format('otext',path))
                            statusBar.showMessage(self.ERR_BADPATH.format('otext',path))
                        else:
                            statusBar.showMessage("{}: '{}'".format(self.okMsg,otext))
                            self.backup(text,otext)
                else:
                    msg=self.ERR_BADPATH.format('itext',text)
                    print(msg)
                    statusBar.showMessage(msg)
            else:
                print(msg)
                statusBar.showMessage(self.okMsg+":"+msg)
    
        def updateStatBar(self,statusBar,msg):
            statusBar.showMessage(msg)

        def quit(self,statusBar,kill=None,msg=None):
            if msg == None:
                print(self.qMsg)
            else:
                print(msg)
            self.updateStatBar(statusBar,self.qMsg)
            if kill != None:
                kill.quit()
        def toggleStatBar(self,statusBar,action):
            if action.isChecked():
                statusBar.show()
            else:
                statusBar.hide() 
        def clear(self,statusBar):
            self.master.edits.text.setText('')
            self.master.edits.otext.setText('')
            statusBar.showMessage("Cleared!")

    class example(QMainWindow):
        newBtn=None
        cm=None
        buttons=None
        def __init__(self):
            super().__init__()
            #self.initUI()
            self.statusBar().showMessage('')

             
        def contextMenuEvent(self,event):
            cmenu = QMenu(self)
            opn=self.cm.contextMenuActOpen(cmenu)
            quit=self.cm.contextMenuActQuit(cmenu)
            action=cmenu.exec_(self.mapToGlobal(event.pos()))
        
        def initUi(self):
            QToolTip.setFont(QFont('SansSerif',11))
            self.setGeometry(300,300,400,200)
            self.setWindowTitle('Icon')
            self.setWindowIcon(QIcon('tays handscrub.png'))
            self.show()

    def initUI(self):
        #at this level, the var master found in other classes is self.Example
        self.Example=self.example()
        self.Example.ext=self.ext

        self.Example.cm=self.cm()
        self.Example.cm.master=self.Example

        self.Example.fm=self.fileMenu()
        self.Example.fm.master=self.Example
        self.Example.fm.mkMenuBar()

        self.Example.buttons=self.buttons()
        self.Example.buttons.master=self.Example

        self.Example.edits=self.edits()
        self.Example.edits.master=self.Example

        self.Example.act=self.actions()
        self.Example.act.master=self.Example


        self.Example.layout=self.layout()
        self.Example.layout.master=self.Example
        #self.Example.layout.setLayout()
        self.Example.layout.mkTabs()

        self.Example.toolbar=self.toolbar()
        self.Example.toolbar.master=self.Example
        self.Example.toolbar.mkToolBar()
        

        self.Example.initUi()
    class layout(example):
        master=None
        def mkTabs(self):
            tabs=QTabWidget()
            tabs.addTab(self.setLayoutZip(),"zip")
            tabs.addTab(QWidget(),"Pending")
            self.master.setCentralWidget(tabs)
        

        def setLayoutZip(self):
            wid=QWidget(self.master)
            self.master.setCentralWidget(wid)
            grid=QGridLayout()
            grid.setSpacing(10)
            grid.addWidget(self.master.buttons.okayBtn(),1,0,1,3)
            grid.addWidget(self.master.buttons.quitBtn(),1,3,1,1)
            grid.addWidget(self.master.buttons.clearBtn(),1,4,1,1)
            grid.addWidget(self.master.edits.label,2,0,1,4)
            grid.addWidget(self.master.edits.text,2,1,1,4)
            grid.addWidget(self.master.edits.olabel,3,0,1,4)
            grid.addWidget(self.master.edits.otext,3,1,1,4)
            wid.setLayout(grid)
            return wid
            
    class edits(example):
        master=None
        def __init__(self):
            self.lineText()
            self.lineTextLabel()
            self.lineTextOut()
            self.lineTextOutLabel()

        def lineTextOut(self):
            text=QLineEdit()
            self.otext=text

        def lineText(self):
            text=QLineEdit()
            self.text=text

        def lineTextOutLabel(self):
            label=QLabel('OutPath')
            self.olabel=label

        def lineTextLabel(self):
            label=QLabel('InPath')
            self.label=label

    class buttons(example):
        master=None
        #gui buttons
        def quitBtn(self):
            button=QPushButton('Quit')
            button.setToolTip('Quit!')
            button.resize(50,50)
            button.setStatusTip('Quit Button')
            button.clicked.connect(lambda: self.master.act.quit(self.master.statusBar(),QApplication.instance()))
            return button
       
        def okayBtn(self):
            button=QPushButton('Okay')
            button.setToolTip('Okay!')
            button.resize(50,50)
            button.setStatusTip('Okay Button')
            button.clicked.connect(lambda: self.master.act.okay(self.master.statusBar()))
            return button
        
        def clearBtn(self):
            button=QPushButton('Clear')
            button.setToolTip("clear inpath")
            button.resize(50,50)
            button.setStatusTip('cleared inpath')
            button.clicked.connect(lambda: self.master.act.clear(self.master.statusBar()))
            return button

    class fileMenu(example):
        #toolbar file menu
        master=None
        def exitAction(self):
            exitAct=QAction(QIcon('exit.png'),'&Exit',self.master)
            exitAct.setShortcut('Ctrl+Q')
            exitAct.setStatusTip('Exit Application')
            exitAct.triggered.connect(lambda: self.master.act.quit(self.statusBar(),qApp))
            return exitAct

        def mkMenuBar(self):
            menuBar=self.master.menuBar()
            self.mkFileMenu(menuBar)

        def mkFileMenu(self,menuBar):
            fileMenu=menuBar.addMenu('&File')
            fileMenu.addMenu(self.mkFileMenuSub_Import())
            fileMenu.addAction(self.exitAction())
            fileMenu.addAction(self.mkFileAction_TogStat())

        def mkFileMenuSub_ImportAct(self):
            action=QAction('Import Data',self.master)
            action.setShortcut('Ctrl+I')
            action.setStatusTip('Import Data')
            action.triggered.connect(lambda: self.master.act.quit(self.master.statusBar(),kill=None,msg='Import Data'))
            return action

        def mkFileMenuSub_Import(self):
            menu=QMenu('Import',self.master)
            menuAction=self.mkFileMenuSub_ImportAct()
            menu.addAction(menuAction)
            return menu

        def mkFileAction_TogStat(self):
            action=QAction('View Status Bar',self.master,checkable=True)
            action.setStatusTip('View Status Bar')
            action.setChecked(True)
            action.triggered.connect(lambda: self.master.act.toggleStatBar(self.master.statusBar(),action))
            return action

    class cm(example):
        #context menu
        master=None
        def contextMenuActQuit(self,cmenu):
            action=cmenu.addAction("Quit")
            action.triggered.connect(lambda: self.master.act.quit(self.statusBar(),qApp))
            return action

        def contextMenuActOpen(self,cmenu):
            action=cmenu.addAction("Open")
            self.master.setStatusTip("Open")
            return action

        def contextMenuActNew(self,cmenu):
            action=cmenu.addAction("New")
            #need to pass self into newBtn to make it aware of the window to connect to 
            action.triggered.connect(lambda: self.master.newBtn.newBtnStatus())
            self.setStatusTip("New")
            return action 

    class toolbar(example):
        master=None
        def mkToolBar(self):
            self.toolbar=self.master.addToolBar('exit')
            action=self.master.fm.exitAction()
            action.setShortcut('')
            self.toolbar.addAction(action)

    def __init__(self):
        super().__init__()
        self.initUI()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    orv=orvil()
    sys.exit(app.exec_())
