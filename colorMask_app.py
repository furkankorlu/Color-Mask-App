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

        self.ui.lower_slide.valueChanged.connect(self.update_color_mask)
        self.ui.lower_slides.valueChanged.connect(self.update_color_mask)
        self.ui.lower_slidev.valueChanged.connect(self.update_color_mask)

        self.ui.upper_slide.valueChanged.connect(self.update_color_mask)
        self.ui.upper_slides.valueChanged.connect(self.update_color_mask)
        self.ui.upper_slidev.valueChanged.connect(self.update_color_mask)

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

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        def tiklama(click, x, y, flags, param):
            if click == cv.EVENT_LBUTTONDOWN:
                h = hsv[y, x, 0]
                s = hsv[y, x, 1]
                v = hsv[y, x, 2]
                # print(f"H:{h} S:{s} V:{v}")
                self.ui.hsvlabel.setText(f"HSV:[{h},{s},{v}]")

            elif not(self.ui.cbhsv.isChecked()):
                cv.destroyAllWindows()
                
        if self.ui.cbhsv.isChecked():
            frameflip = cv.flip(frame,1)
            cv.imshow("Frame", frameflip)
            cv.setMouseCallback('Frame',tiklama)

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

                # label2: Belirli renk aralığında maskeleme
                masked_frame = self.color_mask(frame)  # Belirli renk aralığında maskeleme işlemi
                image2 = QImage(masked_frame.data, masked_frame.shape[1], masked_frame.shape[0], QImage.Format_RGB888).rgbSwapped()
                pixmap2 = QPixmap.fromImage(image2).scaled(self.ui.mask.size(), Qt.AspectRatioMode.KeepAspectRatio)
                self.ui.mask.setPixmap(pixmap2)

        elif not(self.ui.cbcam.isChecked()):
            # webcam off
            image1 = QImage(cam_off_img.data, cam_off_img.shape[1], cam_off_img.shape[0], QImage.Format_RGB888).rgbSwapped()
            pixmap1 = QPixmap.fromImage(image1).scaled(self.ui.webcam.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.webcam.setPixmap(pixmap1)
            # mask off
            image2 = QImage(cam_off_img.data, cam_off_img.shape[1], cam_off_img.shape[0], QImage.Format_RGB888).rgbSwapped()
            pixmap2 = QPixmap.fromImage(image2).scaled(self.ui.mask.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.mask.setPixmap(pixmap2)

    def color_mask(self, frame):
        # Belirli renk aralığında maskeleme işlemi gerçekleştirilir
        # İşlem sonucu maskeleme yapılmış görüntü döndürülür
        
        lower_color = np.array([self.ui.lower_slide.value(),self.ui.lower_slides.value(),self.ui.lower_slidev.value()])
        upper_color = np.array([self.ui.upper_slide.value(),self.ui.upper_slides.value(),self.ui.upper_slidev.value()])

        blur = cv.GaussianBlur(frame,(3,3),0)
        hsv = cv.cvtColor(blur,cv.COLOR_BGR2HSV)

        # Belirli renk aralığındaki pikselleri maskele
        mask = cv.inRange(hsv, lower_color, upper_color)

        # Maskelenmiş görüntüyü orijinal görüntüyle birleştirerek renkli maskeleme yap
        masked_frame = cv.bitwise_and(frame, frame, mask=mask)

        if self.ui.cbdetect.isChecked():

            canny = cv.Canny(mask,100,200)
            
            contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) 

            for cont in contours:

                if cv.contourArea(cont) > 50:
                    # print(cont)
                    cv.drawContours(masked_frame,cont,-1,(0,0,255),2,8)

                    x,y,w,h = cv.boundingRect(cont)

                    cv.rectangle(masked_frame,(x,y),(x+w,y+h),(0,0,255),2)

                    # rect = cv.minAreaRect(cont)
                    # box = cv.boxPoints(rect)
                    # box = np.int0(box)
                    # cv.drawContours(masked_frame,[box],0,(255,0,0),2)

        return masked_frame
    
    def update_color_mask(self):
        self.capture_image()
        
        # Kaydırıcı değerlerini göster
        self.ui.lower_label.setText(f"Lower: {[self.ui.lower_slide.value(),self.ui.lower_slides.value(),self.ui.lower_slidev.value()]}")
        self.ui.upper_label.setText(f"Upper: {[self.ui.upper_slide.value(),self.ui.upper_slides.value(),self.ui.upper_slidev.value()]}")

    def closeEvent(self, event):
        self.camera.release()
        self.timer.stop()
        super().closeEvent(event)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()