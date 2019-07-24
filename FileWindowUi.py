# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'painting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileWindow(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 170)
        Form.setFixedSize(500, 170)
        
        #定义界面控件UI
        #第一行
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(30, 10, 100, 30))
        self.label_1.setObjectName("label_1")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setGeometry(QtCore.QRect(150, 10, 320, 30))
        self.lineEdit_1.setObjectName("lineEdit_1")

        #第二行
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 100, 30))
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 50, 150, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 50, 150, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")

        #第三行
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 100, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 90, 200, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(370, 90, 100, 30))
        self.pushButton_1.setObjectName("pushButton_1")

        #第四行
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 130, 100, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 130, 100, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        #定义button的点击操作
        self.pushButton_1.clicked.connect(self.chooseDir)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.makeDir)
        



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "创建素材组"))
        self.label_1.setText(_translate("Form", "素材组名："))
        self.label_2.setText(_translate("Form", "素材序号："))
        self.label_3.setText(_translate("Form", "素材位置："))
        self.pushButton_1.setText(_translate("Form", "选择"))
        self.pushButton_2.setText(_translate("Form", "返回"))
        self.pushButton_3.setText(_translate("Form", "创建"))



