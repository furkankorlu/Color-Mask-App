import sys
import cv2 as cv
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from colorMask_ui import Ui_ColorMaskApp

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_ColorMaskApp()
        self.ui.setupUi(self)

        self.camera = cv.VideoCapture(0)
        self.img = cv.imread("gyuw4.png")
        self.cam_off_img = cv.imread("camoff.png")

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()