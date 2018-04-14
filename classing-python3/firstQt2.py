import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QApplication,QMainWindow,qApp,QAction,QMenu,QGridLayout


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
            self.setGeometry(300,300,400,400)
            self.setWindowTitle('Icon')
            self.setWindowIcon(QIcon('tays handscrub.png'))
            self.show()

    def initUI(self):
        #at this level, the var master found in other classes is self.Example
        self.Example=self.example()
        
        self.Example.cm=self.cm()
        self.Example.cm.master=self.Example
        
        self.Example.act=self.actions()
        self.Example.act.master=self.Example

        self.Example.fm=self.fileMenu()
        self.Example.fm.master=self.Example
        self.Example.fm.mkMenuBar()

        self.Example.buttons=self.buttons()
        self.Example.buttons.master=self.Example
        '''
        self.Example.buttons.quitBtn()
        self.Example.buttons.okayBtn()
        '''
        self.Example.layout=self.layout()
        self.Example.layout.master=self.Example
        self.Example.layout.setLayout()

        self.Example.toolbar=self.toolbar()
        self.Example.toolbar.master=self.Example
        self.Example.toolbar.mkToolBar()

        self.Example.initUi()
    class layout(example):
        master=None
        def setLayout(self):
            self.wid=QWidget(self.master)
            self.master.setCentralWidget(self.wid)
            self.grid=QGridLayout()
            self.grid.addWidget(self.master.buttons.okayBtn(),1,0)
            self.grid.addWidget(self.master.buttons.quitBtn(),1,1)
            self.wid.setLayout(self.grid)
            
    class buttons(example):
        master=None
        #gui buttons
        def quitBtn(self):
            button=QPushButton('Quit')
            button.setToolTip('<b>Quit</b>!')
            button.resize(50,50)
            #button.move(150,150)
            button.setStatusTip('Quit Button')
            button.clicked.connect(lambda: self.master.act.quit(self.master.statusBar(),QApplication.instance()))
            return button
       
        def okayBtn(self):
            button=QPushButton('Okay')
            button.setToolTip('<b>Okay</b>!')
            button.resize(50,50)
            #button.move(50,150)
            button.setStatusTip('Okay Button')
            button.clicked.connect(lambda: self.master.act.okay(self.master.statusBar()))
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
