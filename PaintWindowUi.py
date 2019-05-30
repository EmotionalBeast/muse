# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'painting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QWidget

class Ui_PaintWindow(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setFixedSize(800, 600)
        Form.setWindowIcon(QtGui.QIcon("./images/tool.png"))
        #定义界面控件
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 100, 30))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 10, 480, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(670,10,100,30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 250, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 310, 100, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 370, 100, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(160, 50, 610, 540))
        self.graphicsView.setObjectName("graphicsView")

        #定义button的点击操作
        self.pushButton.clicked.connect(self.ratio_4_3)
        # self.pushButton_2.clicked.connect(self.ratio_16_9)
        # self.pushButton_3.clicked.connect(self.ratio_18:9)
        self.pushButton_4.clicked.connect(self.chooseImage)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Painting"))
        self.label.setText(_translate("Form", "Image"))
        self.pushButton.setText(_translate("Form", "4:3"))
        self.pushButton_2.setText(_translate("Form", "16:9"))
        self.pushButton_3.setText(_translate("Form", "18:9"))
        self.pushButton_4.setText(_translate("Form", "Browse"))




