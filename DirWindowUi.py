# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'painting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_DirWindow(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(680, 90)
        Form.setFixedSize(680, 90)

        with open("./resources/json/setting.json", "r") as lf:
            jsonStr = lf.read()
            dic = json.loads(jsonStr,strict = False)

        #定义界面控件UI
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 100, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 10, 400, 30))
        self.lineEdit.setText(dic["directory"])
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(550, 10, 100, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230,50,100,30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(350,50,100,30))
        self.pushButton_3.setObjectName("pushButton_3")

        #按钮信号槽链接
        self.pushButton_1.clicked.connect(self.chooseDir)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.comfirmDir)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "设置"))
        self.label.setText(_translate("Form", "工作目录："))
        self.pushButton_1.setText(_translate("Form", "选择"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton_3.setText(_translate("Form", "确认"))




 

