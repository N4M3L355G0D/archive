import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QApplication,QMainWindow,qApp,QAction,QMenu

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
#left off from context menus

class orvil(QMainWindow):
    class actions:
        okMsg="Okay"
        qMsg="Quit"
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

    act=actions()

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
            new=self.cm.contextMenuActNew(cmenu,self)
            opn=self.cm.contextMenuActOpen(cmenu,self)
            quit=self.cm.contextMenuActQuit(cmenu,self)
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
        nbt=self.nbt()
        self.Example.newBtn=nbt
        self.Example.cm=self.cm()
        self.Example.act=self.actions()
        self.Example.fm=self.fileMenu()
        self.Example.fm.mkMenuBar(self.Example)
        self.Example.buttons=self.buttons()
        self.Example.buttons.quitBtn(self.Example)
        self.Example.buttons.okayBtn(self.Example)
        self.Example.initUi()

    class buttons(example):
        #gui buttons
        def quitBtn(self,master):
            button=QPushButton('Quit',master)
            button.setToolTip('<b>Quit</b>!')
            button.resize(100,50)
            button.move(150,150)
            button.setStatusTip('Quit Button')
            button.clicked.connect(lambda: master.act.quit(master.statusBar(),QApplication.instance()))
       
        def okayBtn(self,master):
            button=QPushButton('Okay',master)
            button.setToolTip('<b>Okay</b>!')
            button.resize(100,50)
            button.move(50,150)
            button.setStatusTip('Okay Button')
            button.clicked.connect(lambda: master.act.okay(master.statusBar()))

    class fileMenu(example):
        #toolbar file menu
        def exitAction(self,master):
            exitAct=QAction(QIcon('exit.png'),'&Exit',master)
            exitAct.setShortcut('Ctrl+Q')
            exitAct.setStatusTip('Exit Application')
            exitAct.triggered.connect(lambda: master.act.quit(self.statusBar(),qApp))
            return exitAct

        def mkMenuBar(self,master):
            menuBar=master.menuBar()
            self.mkFileMenu(menuBar,master)

        def mkFileMenu(self,menuBar,master):
            fileMenu=menuBar.addMenu('&File')
            fileMenu.addAction(self.mkFileAction_New(master))
            fileMenu.addMenu(self.mkFileMenuSub_Import(master))
            fileMenu.addAction(self.exitAction(master))
            fileMenu.addAction(self.mkFileAction_TogStat(master))

        def mkFileMenuSub_ImportAct(self,master):
            action=QAction('Import Data',master)
            action.setShortcut('Ctrl+I')
            action.setStatusTip('Import Data')
            action.triggered.connect(lambda: master.act.quit(master.statusBar(),kill=None,msg='Import Data'))
            return action

        def mkFileMenuSub_Import(self,master):
            menu=QMenu('Import',master)
            menuAction=self.mkFileMenuSub_ImportAct(master)
            menu.addAction(menuAction)
            return menu
    
        def mkFileAction_New(self,master):
            action=QAction('New',master)
            action.setStatusTip('New')
            action.setShortcut("Ctrl+N")
            action.triggered.connect(lambda: master.newBtn.newBtnStatus(master))
            return action

        def mkFileAction_TogStat(self,master):
            action=QAction('View Status Bar',master,checkable=True)
            action.setStatusTip('View Status Bar')
            action.setChecked(True)
            action.triggered.connect(lambda: master.act.toggleStatBar(master.statusBar(),action))
            return action

    class cm(example):
        #context menu
        def contextMenuActQuit(self,cmenu,master):
            action=cmenu.addAction("Quit")
            action.triggered.connect(lambda: master.act.quit(self.statusBar(),qApp))
            return action

        def contextMenuActOpen(self,cmenu,master):
            action=cmenu.addAction("Open")
            master.setStatusTip("Open")
            return action

        def contextMenuActNew(self,cmenu,master):
            action=cmenu.addAction("New")
            action.setShortcut("Ctrl+N")
            #need to pass self into newBtn to make it aware of the window to connect to 
            action.triggered.connect(lambda: master.newBtn.newBtnStatus(master))
            self.setStatusTip("New")
            return action

    class nbt(example):
            newBtnCreated=False
    
            def newBtnHide(self,button):
                self.newBtnCreated=False
                button.hide()
        
            def newBtn(self,master):
                button=QPushButton('New',master)
                button.setToolTip('<b>It\'s a New button</b>!')
                button.resize(100,50)
                button.move(50,100)
                button.setStatusTip('New Button')
                button.clicked.connect(lambda: self.newBtnHide(button))

                return button
    
            def newBtnStatus(self,master):
                if self.newBtnCreated == False:
                    button=self.newBtn(master)
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
