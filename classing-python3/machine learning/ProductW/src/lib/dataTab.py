#! /usr/bin/env python3

from PIL import Image
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy,cv2

class dataTab:
    master=None
    lbls={}
    edits={}
    def labels(self,data):
        for key in data.keys():
            self.lbls[key]=QLabel()
            self.lbls[key].setText(key)    
        for key in data.keys():
            if key == "thumbnailImage":
                self.edits[key]=QLabel()
                h,w, chan = data[key].shape
                bpl=3*w
                self.edits[key].setPixmap(QPixmap(QImage(data[key],w,h,bpl,QImage.Format_RGB888)))
            else:
                self.edits[key]=QTextEdit()
                self.edits[key].setText(str(data[key]))
                self.edits[key].setReadOnly(True)

    def labelsUpdate(self,data):
        for key in data.keys():
            self.lbls[key].setText(key)    
        for key in data.keys():
            if key == "thumbnailImage":
                nparr = numpy.fromstring(data[key], numpy.uint8)
                data[key] = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
                h,w, chan = data[key].shape
                bpl=3*w
                self.edits[key].setPixmap(QPixmap(QImage(data[key],w,h,bpl,QImage.Format_RGB888)))
            else:
                self.edits[key].setText(str(data[key]))
                self.edits[key].setReadOnly(True)
