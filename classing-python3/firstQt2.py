import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QApplication,QMainWindow,qApp,QAction,QMenu

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
#left off from context menus

class orvil(QMainWindow):
    class actions:
        okMsg="Okay"
        qMsg="Quit"
        #master will be populated with the object 'example'
        master=None
        def okay(self,statusBar,msg=None):
            if msg == None:
                print(self.okMsg)
            else:
                print(msg)
            statusBar.showMessage(self.okMsg)
    
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
            new=self.cm.contextMenuActNew(cmenu)
            opn=self.cm.contextMenuActOpen(cmenu)
            quit=self.cm.contextMenuActQuit(cmenu)
            action=cmenu.exec_(self.mapToGlobal(event.pos()))
        
        def initUi(self):
            QToolTip.setFont(QFont('SansSerif',12))
            self.setToolTip('This is is a <b>QWidget</b> widget')
            self.setGeometry(300,300,300,220)
            self.setWindowTitle('Icon')
            self.setWindowIcon(QIcon('tays handscrub.png'))
            self.show()

    def initUI(self):
        #at this level, the var master found in other classes is self.Example
        self.Example=self.example()

        self.Example.newBtn=self.nbt()
        self.Example.newBtn.master=self.Example
        
        self.Example.cm=self.cm()
        self.Example.cm.master=self.Example
        
        self.Example.act=self.actions()
        self.Example.act.master=self.Example

        self.Example.fm=self.fileMenu()
        self.Example.fm.master=self.Example
        self.Example.fm.mkMenuBar()

        self.Example.buttons=self.buttons()
        self.Example.buttons.master=self.Example
        self.Example.buttons.quitBtn()
        self.Example.buttons.okayBtn()

        self.Example.initUi()

    class buttons(example):
        master=None
        #gui buttons
        def quitBtn(self):
            button=QPushButton('Quit',self.master)
            button.setToolTip('<b>Quit</b>!')
            button.resize(100,50)
            button.move(150,150)
            button.setStatusTip('Quit Button')
            button.clicked.connect(lambda: self.master.act.quit(self.master.statusBar(),QApplication.instance()))
       
        def okayBtn(self):
            button=QPushButton('Okay',self.master)
            button.setToolTip('<b>Okay</b>!')
            button.resize(100,50)
            button.move(50,150)
            button.setStatusTip('Okay Button')
            button.clicked.connect(lambda: self.master.act.okay(self.master.statusBar()))

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
            fileMenu.addAction(self.mkFileAction_New())
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
    
        def mkFileAction_New(self):
            action=QAction('New',self.master)
            action.setStatusTip('New')
            action.setShortcut("Ctrl+N")
            action.triggered.connect(lambda: self.master.newBtn.newBtnStatus())
            return action

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
            action.setShortcut("Ctrl+N")
            #need to pass self into newBtn to make it aware of the window to connect to 
            action.triggered.connect(lambda: self.master.newBtn.newBtnStatus(self.master))
            self.setStatusTip("New")
            return action

    class nbt(example):
            newBtnCreated=False
            master=None 
            def newBtnHide(self,button):
                self.newBtnCreated=False
                button.hide()
        
            def newBtn(self):
                button=QPushButton('New',self.master)
                button.setToolTip('<b>It\'s a New button</b>!')
                button.resize(100,50)
                button.move(50,100)
                button.setStatusTip('New Button')
                button.clicked.connect(lambda: self.newBtnHide(button))

                return button
    
            def newBtnStatus(self):
                if self.newBtnCreated == False:
                    button=self.newBtn()
                    button.show()    
                    self.newBtnCreated=True
                print(self.newBtnCreated)


    def __init__(self):
        super().__init__()
        self.initUI()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    orv=orvil()
    sys.exit(app.exec_())
