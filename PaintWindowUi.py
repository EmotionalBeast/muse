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
        Form.resize(600, 800)
        Form.setFixedSize(600, 800)
        
        #定义界面控件
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 600, 800))
        self.graphicsView.setObjectName("graphicsView")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "效果显示"))
        




