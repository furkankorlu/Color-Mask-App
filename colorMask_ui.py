# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorMask.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColorMaskApp(object):
    def setupUi(self, ColorMaskApp):
        ColorMaskApp.setObjectName("ColorMaskApp")
        ColorMaskApp.resize(1463, 900)
        self.centralwidget = QtWidgets.QWidget(ColorMaskApp)
        self.centralwidget.setObjectName("centralwidget")
        self.lower_slide = QtWidgets.QSlider(self.centralwidget)
        self.lower_slide.setGeometry(QtCore.QRect(40, 530, 30, 250))
        self.lower_slide.setMaximum(180)
        self.lower_slide.setSingleStep(1)
        self.lower_slide.setProperty("value", 90)
        self.lower_slide.setOrientation(QtCore.Qt.Vertical)
        self.lower_slide.setObjectName("lower_slide")
        self.webcam = QtWidgets.QLabel(self.centralwidget)
        self.webcam.setGeometry(QtCore.QRect(80, 10, 640, 480))
        self.webcam.setText("")
        self.webcam.setObjectName("webcam")
        self.upper_slide = QtWidgets.QSlider(self.centralwidget)
        self.upper_slide.setGeometry(QtCore.QRect(1100, 530, 30, 250))
        self.upper_slide.setMaximum(180)
        self.upper_slide.setSingleStep(1)
        self.upper_slide.setProperty("value", 130)
        self.upper_slide.setOrientation(QtCore.Qt.Vertical)
        self.upper_slide.setObjectName("upper_slide")
        self.mask = QtWidgets.QLabel(self.centralwidget)
        self.mask.setGeometry(QtCore.QRect(760, 10, 640, 480))
        self.mask.setText("")
        self.mask.setObjectName("mask")
        self.lower_label = QtWidgets.QLabel(self.centralwidget)
        self.lower_label.setGeometry(QtCore.QRect(190, 760, 150, 20))
        self.lower_label.setObjectName("lower_label")
        self.upper_label = QtWidgets.QLabel(self.centralwidget)
        self.upper_label.setGeometry(QtCore.QRect(1250, 760, 150, 20))
        self.upper_label.setObjectName("upper_label")
        self.hsv = QtWidgets.QLabel(self.centralwidget)
        self.hsv.setGeometry(QtCore.QRect(400, 510, 600, 300))
        self.hsv.setText("")
        self.hsv.setObjectName("hsv")
        self.lower_slides = QtWidgets.QSlider(self.centralwidget)
        self.lower_slides.setGeometry(QtCore.QRect(90, 530, 30, 250))
        self.lower_slides.setMaximum(255)
        self.lower_slides.setProperty("value", 140)
        self.lower_slides.setOrientation(QtCore.Qt.Vertical)
        self.lower_slides.setObjectName("lower_slides")
        self.lower_slidev = QtWidgets.QSlider(self.centralwidget)
        self.lower_slidev.setGeometry(QtCore.QRect(140, 530, 30, 250))
        self.lower_slidev.setMaximum(255)
        self.lower_slidev.setProperty("value", 140)
        self.lower_slidev.setOrientation(QtCore.Qt.Vertical)
        self.lower_slidev.setObjectName("lower_slidev")
        self.upper_slides = QtWidgets.QSlider(self.centralwidget)
        self.upper_slides.setGeometry(QtCore.QRect(1150, 530, 30, 250))
        self.upper_slides.setMaximum(255)
        self.upper_slides.setProperty("value", 255)
        self.upper_slides.setOrientation(QtCore.Qt.Vertical)
        self.upper_slides.setObjectName("upper_slides")
        self.upper_slidev = QtWidgets.QSlider(self.centralwidget)
        self.upper_slidev.setGeometry(QtCore.QRect(1200, 530, 30, 250))
        self.upper_slidev.setMaximum(255)
        self.upper_slidev.setProperty("value", 255)
        self.upper_slidev.setOrientation(QtCore.Qt.Vertical)
        self.upper_slidev.setObjectName("upper_slidev")
        self.cbdetect = QtWidgets.QCheckBox(self.centralwidget)
        self.cbdetect.setGeometry(QtCore.QRect(40, 820, 151, 20))
        self.cbdetect.setObjectName("cbdetect")
        self.cbcam = QtWidgets.QCheckBox(self.centralwidget)
        self.cbcam.setEnabled(True)
        self.cbcam.setGeometry(QtCore.QRect(220, 820, 81, 20))
        self.cbcam.setChecked(True)
        self.cbcam.setObjectName("cbcam")
        self.cbhsv = QtWidgets.QCheckBox(self.centralwidget)
        self.cbhsv.setGeometry(QtCore.QRect(300, 820, 131, 20))
        self.cbhsv.setObjectName("cbhsv")
        self.hsvlabel = QtWidgets.QLabel(self.centralwidget)
        self.hsvlabel.setGeometry(QtCore.QRect(640, 820, 150, 20))
        self.hsvlabel.setObjectName("hsvlabel")
        self.lower_slide.raise_()
        self.upper_slide.raise_()
        self.mask.raise_()
        self.lower_label.raise_()
        self.upper_label.raise_()
        self.lower_slides.raise_()
        self.lower_slidev.raise_()
        self.upper_slides.raise_()
        self.upper_slidev.raise_()
        self.cbdetect.raise_()
        self.webcam.raise_()
        self.hsv.raise_()
        self.cbcam.raise_()
        self.cbhsv.raise_()
        self.hsvlabel.raise_()
        ColorMaskApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ColorMaskApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1463, 26))
        self.menubar.setObjectName("menubar")
        ColorMaskApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ColorMaskApp)
        self.statusbar.setObjectName("statusbar")
        ColorMaskApp.setStatusBar(self.statusbar)
        self.actionresim = QtWidgets.QAction(ColorMaskApp)
        self.actionresim.setObjectName("actionresim")
        self.actionrr = QtWidgets.QAction(ColorMaskApp)
        self.actionrr.setObjectName("actionrr")

        self.retranslateUi(ColorMaskApp)
        QtCore.QMetaObject.connectSlotsByName(ColorMaskApp)

    def retranslateUi(self, ColorMaskApp):
        _translate = QtCore.QCoreApplication.translate
        ColorMaskApp.setWindowTitle(_translate("ColorMaskApp", "Color Mask App"))
        self.lower_label.setText(_translate("ColorMaskApp", "Lower:"))
        self.upper_label.setText(_translate("ColorMaskApp", "Upper:"))
        self.cbdetect.setText(_translate("ColorMaskApp", "Nesne Tespit Yapılsın"))
        self.cbcam.setText(_translate("ColorMaskApp", "Cam"))
        self.cbhsv.setText(_translate("ColorMaskApp", "HSV Renk Tespit"))
        self.hsvlabel.setText(_translate("ColorMaskApp", "HSV:"))
        self.actionresim.setText(_translate("ColorMaskApp", "resim"))
        self.actionrr.setText(_translate("ColorMaskApp", "rr"))
