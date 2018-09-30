from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

class tops(QMainWindow):
    def __init__(self):
        super().__init__()
    
    class layouts:
        master=None
        def tabs(self,widgets):
            tab=QTabWidget()
            for i in widgets.keys():
                tab.addTab(widgets[i],i)
            self.master.setCentralWidget(tab)
        
        def grid2(self):
            wid=QWidget()
            grid=QGridLayout()
            grid.setSpacing(10)
            grid.addWidget(self.master.lbl_2,0,0)
            grid.addWidget(self.master.button.fontsBtn('lbl2'),0,1)
            grid.addWidget(self.master.lbl_2Name,1,1)
            wid.setLayout(grid)
            return wid
        
        def grid1(self):
            wid=QWidget()
            grid=QGridLayout()
            grid.setSpacing(10)
            grid.addWidget(self.master.lbl_1,0,0)
            grid.addWidget(self.master.button.fontsBtn('lbl1'),0,1)
            grid.addWidget(self.master.lbl_1Name,1,1)
            wid.setLayout(grid)
            return wid

        def setLayouts(self):
            self.tabs({'tab 1':self.grid1(),'tab 2':self.grid2()})

    class main(QMainWindow):
        master=None
    
        def __init__(self):
            super().__init__()    

        def contextMenuEvent(self,event):
            cmenu=QMenu(self)
            quit=self.cm.contextMenuQuit(cmenu)
            self.statusBar().showMessage('context menu')
            action=cmenu.exec_(self.mapToGlobal(event.pos()))

        def initUI(self):
            self.statusBar().showMessage('')
            self.setGeometry(300, 300, 250, 180)
            self.setWindowTitle('Font dialog')
            self.show()

    class actionsBtn:
        master=None
        def displayFont(self,font):
            f=' - '.join([i for num,i in enumerate(font.toString().split(',')) if num < 2])
            return f

        def showFontDialog(self,lbl):
            sender=self.master.sender()
            self.master.statusBar().showMessage(sender.text())
            font, ok = QFontDialog.getFont()
            if ok:
                if lbl == 'lbl1':
                    self.master.lbl_1.setFont(font)
                    self.master.lbl_1Name.setText(self.displayFont(font))
                elif lbl == 'lbl2':
                    self.master.lbl_2.setFont(font)
                    self.master.lbl_2Name.setText(self.displayFont(font))
                self.master.statusBar().showMessage(self.displayFont(font))
        def actionQuit(self):
            sender=self.master.sender()
            print('user: {}'.format(sender.text()))
            qApp.quit()
   
    class fileMenu:
        #file menu toolbar
        master=None
        def mkMenuBar(self):
            menubar=self.master.menuBar()
            self.mkFileMenu(menubar)

        def exitAction(self):
            action=QAction(QIcon('exit.png'),'&Exit',self.master)
            action.setShortcut('Ctrl+Q')
            action.setStatusTip('Exit Application')
            action.triggered.connect(self.master.actBtn.actionQuit)
            return action

        def mkFileMenu(self,menuBar):
            fileMenu=menuBar.addMenu('&File')
            fileMenu.addAction(self.exitAction())

    class contextMenu:
        master=None
        #add context menu
        def contextMenuQuit(self,cmenu):
            action=cmenu.addAction('Quit')
            self.master.statusBar().showMessage('Quit')
            action.triggered.connect(self.master.actBtn.actionQuit)
            return action

    class labels:
        master=None
        def labels(self,string):
            lbl=QLabel(string,self.master)
            return lbl
        def mkLabels(self):
            self.master.lbl_1=self.labels("Knowledge is Power")
            self.master.lbl_1Name=self.labels('Default Font!')
            self.master.lbl_2=self.labels("Do not Waste it!")

            self.master.lbl_2Name=self.labels("Default Font!")

    class buttons:
        master=None
        def fontsBtn(self,lbl):
            btn=QPushButton('fonts',self.master)
            btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
            btn.clicked.connect(lambda: self.master.actBtn.showFontDialog(lbl))
            return btn

    def assembler(self):
        self.win=self.main()

        self.win.actBtn=self.actionsBtn()
        self.win.actBtn.master=self.win

        self.win.button=self.buttons()
        self.win.button.master=self.win
        
        self.win.lbl=self.labels()
        self.win.lbl.master=self.win
        self.win.lbl.mkLabels()
        
        self.win.cm=self.contextMenu()
        self.win.cm.master=self.win
        
        self.win.fileMenu=self.fileMenu()
        self.win.fileMenu.master=self.win
        self.win.fileMenu.mkMenuBar()

        self.win.layout=self.layouts()
        self.win.layout.master=self.win
        self.win.layout.setLayouts()

        self.win.initUI()

       
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = tops()
    ex.assembler()
    sys.exit(app.exec_())
