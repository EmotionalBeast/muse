# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'painting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PaintWindow(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(270, 480)
        Form.setFixedSize(270, 480)
        
        # 定义界面控件
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 270, 480))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("padding: 0px; border: 0px;")
        
        # 定义一个空场景
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0,0,270,480)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "效果展示"))
        




