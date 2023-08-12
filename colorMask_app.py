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

        self.ui.cbdetect.stateChanged.connect(self.show_state)
        self.ui.cbcam.stateChanged.connect(self.show_state)
        self.ui.cbhsv.stateChanged.connect(self.show_state)

        self.timer = QTimer()
        self.timer.timeout.connect(self.capture_image)
        self.timer.start(33)  # 30 FPS (30 kare/saniye) için 33 ms gecikme

    def show_state(self):
        print("\nDetect:",self.ui.cbdetect.isChecked())
        print("Cam:",self.ui.cbcam.isChecked())
        print("Hsv:",self.ui.cbhsv.isChecked())

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()