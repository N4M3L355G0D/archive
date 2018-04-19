import sys
from PyQt5.QtWidgets import * 

import os,zipfile
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

#insert plugins dir
sys.path.insert(0,"lib")
#import encryption plugin
import capsule2

class orvil(QMainWindow):
    ext="zip"
    class unzip:
        master=None
        def externalTasks(self,statusBar,msg,noclear=True):
            statusBar.showMessage(msg)
            if noclear == False:
                self.master.act.clear(statusBar,"unzip")

        def unzip(self,statusBar,fname,opath):
            if os.path.exists(fname):
                if os.path.isfile(fname):
                    try:
                        z=zipfile.ZipFile(fname,'r')
                        z.extractall(path=opath)
                        msg="'{}' : extracted!".format(fname)
                        print(msg)
                        self.externalTasks(statusBar,msg,noclear=False)
                    except OSError as err:
                        statusBar.showMessage('look at terminal output! zip-file still exists, turn off encryption!')
                        print(err)
                else:
                    msg="'{}' : not a file!".format(fname)
                    print(msg)
                    self.externalTasks(statusBar,msg)    
            else:
                msg="'{}' : does not exist!".format(fname)
                print(msg)
                self.externalTasks(statusBar,msg)

        def setPaths(self,statusBar):
            noUZ=False
            result=self.master.crypto.decryption(statusBar)
            if result == False:
                noUZ=True
            self.externalTasks(statusBar,"unzipping, please wait!")
            path=self.master.editsU.text.text()
            opathObj=self.master.editsU.otext
            opath=opathObj.text()
            if path == '':
                msg="InPath cannot be blank!"
                self.externalTasks(statusBar,msg)
                print(msg)
            else:
                if opath == '':
                    opath=os.path.splitext(path)[0]
                if not os.path.exists(opath):
                    if opath != os.path.splitext(path)[0]:
                        msg="'{}' : output path does not exist!".format(opath)
                        print(msg)
                        self.externalTasks(statusBar,msg)
                        noUZ=True
                if noUZ == False:
                    opathObj.setText(opath)
                    msg="'{}' : unzipping".format(opath)
                    print(msg)
                    if result == True:
                        self.externalTasks(statusBar,msg)
                        self.unzip(statusBar,path,opath)
                    else:
                        noUZ=True
            
            if noUZ == False:
                print("'{}' : Done".format(path))
            else:
                statusBar.showMessage('something failed; so nothing will be unzipped!')

    class crypto:
        master=None
        def __init__(self):
            self.capsule=capsule2.accessMethods()
        def decryption(self,statusBar):
            #decryption goes here
            if self.master.cbU.enableEnc.isChecked():
                try:
                    infile=self.master.editsU.text.text()
                    if os.path.exists(infile):
                        if os.path.exists(os.path.splitext(infile)[0]+".eke"):
                            if os.path.splitext(infile)[1] == '.ap2':
                                infile=os.path.splitext(infile)[0]
                            userKey=self.master.editsU.pwdtext.text()
                            self.capsule.mainLibAccess(infile,userKey,'d')
                            self.master.editsU.text.setText(infile)
                            return True
                        else:
                            msg='"{}: "keyfile is missing from the same folder as the datafile'.format(os.path.splitext(infile)[0]+".eke")
                            self.master.statusBar().showMessage(msg)
                            print(msg)
                            return False
                    else:
                        msg='"{}" : data file does not exist!'.format(infile)
                        self.master.statusBar().showMessage(msg)
                        print(msg)
                        return False
                except:
                    return False
            else:
                return True
        def encryption(self,statusBar):
            if self.master.cbZ.enableEnc.isChecked():
                try:
                    self.master.statusBar().showMessage('Encrypting! : Do not exit!')
                    infile=self.master.editsU.text.text()
                    if os.path.splitext(infile)[1] == '.ap2':
                        infile=os.path.splitext(infile)[0]
                    infile=self.master.editsZ.otext.text()
                    userKey=self.master.editsZ.pwdtext.text()
                    self.capsule.mainLibAccess(infile,userKey,'e')
                    self.master.statusBar().showMessage('Encypting Done!')
                    return True
                except:
                    return False
            else:
                #encryption goes here
                return True

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
            self.master.crypto.encryption(self.master.statusBar)

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
                            path=os.path.join(root,fname)
                            self.master.statusBar().showMessage('working on: '+path)
                            print(path)
                            z.write(os.path.join(root,fname),os.path.join(root.replace(arcpath,''),fname))
                        else:
                            z.write(os.path.join(root,fname),os.path.join(root,fname))
                    else:
                        z.write(os.path.join(root,fname),os.path.join(custom,fname))
                    counter+=1
                    self.master.statusBar().showMessage("{}/{}".format(counter,self.fcount))
            self.master.statusBar().showMessage('Zipping Done!')

        def okay(self,statusBar,msg=None):
            presentDir=['','.']
            if msg == None:
                text=self.master.editsZ.text.text()
                otextObj=self.master.editsZ.otext
                otext=otextObj.text()
                if os.path.exists(text):
                    print(self.okMsg,text)
                    statusBar.showMessage("{}: '{}'".format(self.okMsg,text))
                    if otext in presentDir:
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
        def clear(self,statusBar,tab):
            if tab == 'zip':
                self.master.editsZ.text.setText('')
                self.master.editsZ.otext.setText('')
            elif tab == 'unzip':
                self.master.editsU.text.setText('')
                self.master.editsU.otext.setText('')
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
            quit=self.cm.contextMenuActQuit(cmenu)
            action=cmenu.exec_(self.mapToGlobal(event.pos()))
        
        def initUi(self):
            QToolTip.setFont(QFont('SansSerif',11))
            self.setGeometry(300,300,500,200)
            self.setWindowTitle('Kohmet\'s Tail')
            self.setWindowIcon(QIcon('icon.png'))
            self.show()

    def initUI(self):
        #at this level, the var master found in other classes is self.Example
        #think of this section as the assembler for the rest of the code
        self.Example=self.example()
        self.Example.ext=self.ext

        self.Example.cm=self.cm()
        self.Example.cm.master=self.Example

        self.Example.fm=self.fileMenu()
        self.Example.fm.master=self.Example
        self.Example.fm.mkMenuBar()

        self.Example.dialogs=self.dialogs()
        self.Example.dialogs.master=self.Example

        self.Example.buttons=self.buttons()
        self.Example.buttons.clearType='zip'
        self.Example.buttons.master=self.Example

        self.Example.buttonsU=self.buttons()
        self.Example.buttonsU.clearType='unzip'
        self.Example.buttonsU.master=self.Example

        self.Example.crypto=self.crypto()
        self.Example.crypto.master=self.Example

        self.Example.unzip=self.unzip()
        self.Example.unzip.master=self.Example

        self.Example.editsZ=self.edits()
        self.Example.editsZ.master=self.Example
        
        self.Example.editsU=self.edits()
        self.Example.editsU.master=self.Example

        self.Example.act=self.actions()
        self.Example.act.master=self.Example

        self.Example.cbZ=self.checkboxes()
        self.Example.cbZ.master=self.Example
        self.Example.cbZ.encMode='enc'
        self.Example.cbZ.run()

        self.Example.cbU=self.checkboxes()
        self.Example.cbU.master=self.Example
        self.Example.cbU.encMode='dec'
        self.Example.cbU.run()

        self.Example.layout=self.layout()
        self.Example.layout.master=self.Example
        self.Example.layout.mkTabs()

        self.Example.toolbar=self.toolbar()
        self.Example.toolbar.master=self.Example
        self.Example.toolbar.mkToolBar()
        
        self.Example.initUi()

    class layout(example):
        master=None
        def mkTabs(self):
            tabs=QTabWidget()
            tabs.addTab(self.setLayoutZip(),"Zip")
            tabs.addTab(self.setLayoutUnzip(),"UnZip")
            self.master.setCentralWidget(tabs)

        def setLayoutUnzip(self):
            wid=QWidget(self.master)
            self.master.setCentralWidget(wid)
            grid=QGridLayout()
            grid.setSpacing(10)
            #add widgets
            grid.addWidget(self.master.buttonsU.unzipBtn(),1,0,1,3)
            grid.addWidget(self.master.buttonsU.quitBtn(),1,3,1,1)
            grid.addWidget(self.master.buttonsU.clearBtn(),1,4,1,1)
            grid.addWidget(self.master.editsU.label,2,0,1,4)
            grid.addWidget(self.master.editsU.text,2,1,1,4)
            grid.addWidget(self.master.buttonsU.openFileBtn(),2,6,1,1)
            grid.addWidget(self.master.editsU.olabel,3,0,1,4)
            grid.addWidget(self.master.editsU.otext,3,1,1,4)
            grid.addWidget(self.master.buttonsU.getDirBtnU(),3,6,1,1)
            grid.addWidget(self.master.editsU.pwdlabel,4,1,1,1)
            grid.addWidget(self.master.editsU.pwdtext,4,2,1,3)
            grid.addWidget(self.master.cbU.enableEnc,4,0,1,1)
            wid.setLayout(grid)
            return wid

        def setLayoutZip(self):
            wid=QWidget(self.master)
            self.master.setCentralWidget(wid)
            grid=QGridLayout()
            grid.setSpacing(10)
            grid.addWidget(self.master.buttons.okayBtn(),1,0,1,3)
            grid.addWidget(self.master.buttons.quitBtn(),1,3,1,1)
            grid.addWidget(self.master.buttons.clearBtn(),1,4,1,1)
            grid.addWidget(self.master.editsZ.label,2,0,1,4)
            grid.addWidget(self.master.editsZ.text,2,1,1,4)
            grid.addWidget(self.master.buttons.getDirBtn(),2,6,1,1)
            grid.addWidget(self.master.editsZ.olabel,3,0,1,4)
            grid.addWidget(self.master.editsZ.otext,3,1,1,4)
            grid.addWidget(self.master.buttons.saveFileBtn(),3,6,1,1)
            grid.addWidget(self.master.editsZ.pwdlabel,4,1,1,1)
            grid.addWidget(self.master.editsZ.pwdtext,4,2,1,3)
            grid.addWidget(self.master.cbZ.enableEnc,4,0,1,1)
            wid.setLayout(grid)
            return wid
            
    class edits(example):
        master=None
        def __init__(self):
            super().__init__()
            self.lineText()
            self.lineTextLabel()
            self.lineTextOut()
            self.lineTextOutLabel()
            self.lineTextPwdEdit()
            self.lineTextPwdLabel()

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
        
        def lineTextPwdLabel(self):
            label=QLabel('Password')
            self.pwdlabel=label
        
        def lineTextPwdEdit(self):
            text=QLineEdit()
            text.setEchoMode(QLineEdit.Password)
            self.pwdtext=text

    class buttons(example):
        master=None
        clearType=''
        #gui buttons
        def quitBtn(self):
            button=QPushButton('Quit')
            button.setToolTip('Quit!')
            button.resize(50,50)
            button.setStatusTip('Quit Button')
            button.clicked.connect(lambda: self.master.act.quit(self.master.statusBar(),QApplication.instance()))
            return button
       
        def okayBtn(self):
            button=QPushButton('Zip')
            button.setToolTip('Zip!')
            button.resize(50,50)
            button.setStatusTip('Zip Button')
            button.clicked.connect(lambda: self.master.act.okay(self.master.statusBar()))
            return button
        
        def clearBtn(self):
            button=QPushButton('Clear')
            button.setToolTip("clear inpath")
            button.resize(50,50)
            button.setStatusTip('cleared inpath')
            button.clicked.connect(lambda: self.master.act.clear(self.master.statusBar(),self.clearType))
            return button
        
        def unzipBtn(self):
            button=QPushButton('Un-Zip')
            button.setToolTip('Unzip a Zip-File')
            button.clicked.connect(lambda: self.master.unzip.setPaths(self.master.statusBar()))
            button.setStatusTip('Unzip a Zip-File')
            button.resize(50,50)
            return button

        def getDirBtn(self):
            button=QPushButton('Open')
            button.setToolTip('location')
            button.clicked.connect(lambda: self.master.dialogs.openDir(self.master.statusBar(),"zip"))
            button.setStatusTip('location')
            button.resize(50,50)
            return button
        
        def saveFileBtn(self):
            button=QPushButton('Open')
            button.setToolTip('location')
            button.clicked.connect(lambda: self.master.dialogs.saveFile(self.master.statusBar()))
            button.setStatusTip('location')
            button.resize(50,50)
            return button
        
        def openFileBtn(self):
            button=QPushButton('Open')
            button.setToolTip('location')
            button.clicked.connect(lambda: self.master.dialogs.openFile(self.master.statusBar()))
            button.setStatusTip('location')
            button.resize(50,50)
            return button

        def getDirBtnU(self):
            button=QPushButton('Open')
            button.setToolTip('location')
            button.clicked.connect(lambda: self.master.dialogs.openDir(self.master.statusBar(),"unzip"))
            button.setStatusTip('location')
            button.resize(50,50)
            return button

    class checkboxes(example):
        master=None
        encMode=None
        def run(self):
            self.enableEncArch()
            self.enableEncMode(Qt.Unchecked)
        def enableEncMode(self,state):
            if self.encMode == 'enc':
                if state == Qt.Checked:
                    self.master.editsZ.pwdtext.show()
                    self.master.editsZ.pwdlabel.show()
                else:
                    self.master.editsZ.pwdtext.hide()
                    self.master.editsZ.pwdlabel.hide()
            elif self.encMode == 'dec':
                if state == Qt.Checked:
                    self.master.editsU.pwdtext.show()
                    self.master.editsU.pwdlabel.show()
                else:
                    self.master.editsU.pwdtext.hide()
                    self.master.editsU.pwdlabel.hide()

        def enableEncArch(self):
            checkBox=QCheckBox('Encryption',self)
            checkBox.stateChanged.connect(self.enableEncMode)
            self.enableEnc=checkBox

    class dialogs(example):
        master=None
        userHome=None
        def __init__(self):
            super().__init__()
            self.userHome=os.path.expanduser('~')
        def openDir(self,statusBar,mode):
            if mode == "zip":
                fname = QFileDialog.getExistingDirectory(self, 'Open Folder',self.userHome,QFileDialog.ShowDirsOnly)
                self.master.editsZ.text.setText(fname)
            elif mode == "unzip":
                fname = QFileDialog.getExistingDirectory(self, 'Open Folder',self.userHome,QFileDialog.ShowDirsOnly)
                self.master.editsU.otext.setText(fname)

        def saveFile(self,statusBar):
            fname = QFileDialog.getSaveFileName(self,'Save File',self.userHome)
            if len(fname) > 0:
                self.master.editsZ.otext.setText(fname[0])
        def openFile(self,statusBar):
            fname = QFileDialog.getOpenFileName(self,"Open File",self.userHome)
            if len(fname) > 0:
                self.master.editsU.text.setText(fname[0])
            
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
            #fileMenu.addMenu(self.mkFileMenuSub_Import())
            fileMenu.addAction(self.exitAction())
            fileMenu.addAction(self.mkFileAction_TogStat())
        '''
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
        '''
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
        '''
        def contextMenuActOpen(self,cmenu):
            action=cmenu.addAction("Open")
            self.master.setStatusTip("Open")
            return action
        '''
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
