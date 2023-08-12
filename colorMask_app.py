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

    def capture_image(self):
        img = self.img
        ret, frame = self.camera.read()
        cam_off_img = self.cam_off_img

        # label3: Hsv renk spektrum fotografi
        image3 = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888).rgbSwapped()
        pixmap3 = QPixmap.fromImage(image3).scaled(self.ui.hsv.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.hsv.setPixmap(pixmap3)

        if self.ui.cbcam.isChecked():
            if ret:
                # label1: Orjinal görüntü
                frame = cv.flip(frame,1)
                image1 = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()
                pixmap1 = QPixmap.fromImage(image1).scaled(self.ui.webcam.size(), Qt.AspectRatioMode.KeepAspectRatio)
                self.ui.webcam.setPixmap(pixmap1)

        elif not(self.ui.cbcam.isChecked()):
            # webcam off
            image1 = QImage(cam_off_img.data, cam_off_img.shape[1], cam_off_img.shape[0], QImage.Format_RGB888).rgbSwapped()
            pixmap1 = QPixmap.fromImage(image1).scaled(self.ui.webcam.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.webcam.setPixmap(pixmap1)
            # mask off
            image2 = QImage(cam_off_img.data, cam_off_img.shape[1], cam_off_img.shape[0], QImage.Format_RGB888).rgbSwapped()
            pixmap2 = QPixmap.fromImage(image2).scaled(self.ui.mask.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.mask.setPixmap(pixmap2)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()