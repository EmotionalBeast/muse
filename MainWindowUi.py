# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lasttools.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
													QTableWidgetItem, QAbstractItemView, QComboBox)
# import json, os


class Ui_MainWindow(object):
    #在界面中添加控件
    def setupUi(self, MainWindow):
        #设置主窗口，主窗口分为菜单栏，工具栏，状态栏，标题栏
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 680)
        MainWindow.setFixedSize(1000, 680)
        MainWindow.setWindowIcon(QtGui.QIcon('./resources/images/tool.png'))

        #主体部分添加控件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #添加tabWidget到centralWidget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 130, 1000, 550))
        self.tabWidget.setObjectName("tabWidget")


        
        MainWindow.setCentralWidget(self.centralwidget)

        #选择素材组
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(45,10,100,30))
        self.label_1.setText("素材组：")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.comBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comBox_1.setGeometry(QtCore.QRect(155, 10, 300, 30))
        self.comBox_1.addItems(self.dirList())
        self.comBox_1.activated.connect(lambda: self.templateList(self.comBox_1.currentText()))
        self.comBox_1.setCurrentIndex(-1)
        self.comBox_1.setObjectName("comBox_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(545,10,100,30))
        self.label_2.setText("json文件：")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comBox_2.setGeometry(QtCore.QRect(645, 10, 300, 30))
        self.comBox_2.activated.connect(lambda: self.initData(self.comBox_2.currentText()))
        self.comBox_2.setObjectName("comBox_2")

        #选择素材的组件部分:blur,cell,background,text,picturelevel(控制图层）
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 60, 30))
        self.label_3.setText("Cell:")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.spinBox_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_1.setGeometry(QtCore.QRect(100,70,50,30))

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 70, 90, 30))
        self.label_4.setText("Background:")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(280, 70, 50, 30))

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 70, 50, 30))
        self.label_5.setText("Text:")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(420, 70, 50, 30))


        #增加RadioButton
        #第一行
        self.cbox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.cbox_1.setGeometry(QtCore.QRect(490,50,80,30))
        self.cbox_1.setText("Blur")
        self.cbox_1.setObjectName("cbox_1")

        self.cbox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.cbox_2.setGeometry(QtCore.QRect(580,50,80,30))
        self.cbox_2.setText("Level")
        self.cbox_2.setObjectName("cbox_2")

        self.cbox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.cbox_4.setGeometry(QtCore.QRect(670,50,80,30))
        self.cbox_4.setText("bgColor")
        self.cbox_4.setObjectName("cbox_4")

        #第二行
        self.cbox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.cbox_3.setGeometry(QtCore.QRect(490,90,100,30))
        self.cbox_3.setText("animation")
        self.cbox_3.setObjectName("cbox_3")


        self.cbox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.cbox_5.setGeometry(QtCore.QRect(600,90,110,30))
        self.cbox_5.setText("animation_text")
        self.cbox_5.setObjectName("cbox_5")

        self.cbox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.cbox_6.setGeometry(QtCore.QRect(730,90,100,30))
        self.cbox_6.setText("ignore")
        self.cbox_6.setObjectName("cbox_6")


        #增加button
        self.pbtn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_1.setGeometry(QtCore.QRect(890,70,100,30))
        self.pbtn_1.setText("生成")
        self.pbtn_1.setObjectName("pbtn_1")

        #状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Non Editable")

        #菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)

        #工具栏
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.new = QtWidgets.QAction(QtGui.QIcon('./resources/images/new.png'), '&new', self)
        self.edit = QtWidgets.QAction(QtGui.QIcon('./resources/images/edit.png'),'&edit', self)
        self.save = QtWidgets.QAction(QtGui.QIcon('./resources/images/save.png'), '&save', self)
        self.refresh = QtWidgets.QAction(QtGui.QIcon('./resources/images/refresh.png'), '&refresh', self)
        self.open = QtWidgets.QAction(QtGui.QIcon('./resources/images/open.png'), '&open', self)
        self.toolBar.addAction(self.new)
        self.toolBar.addAction(self.edit)
        self.toolBar.addAction(self.save)
        self.toolBar.addAction(self.refresh)
        self.toolBar.addAction(self.open)


        #定义动作信息
        self.actionNew = QtWidgets.QAction(QtGui.QIcon('./resources/images/new.png'), '&New', self)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(QtGui.QIcon('./resources/images/save_as.png'), '&Save', self)
        self.actionSave.setObjectName("actionSave")
        self.actionSetting = QtWidgets.QAction(QtGui.QIcon('./resources/images/setting.png'), '&Setting', self)
        self.actionSetting.setObjectName("actionSetting")
        self.actionQuit = QtWidgets.QAction(QtGui.QIcon('./resources/images/quit.png'), '&Quit', self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPaint = QtWidgets.QAction(QtGui.QIcon('./resources/images/paint.png'), '&Paint', self)
        self.actionPaint.setObjectName("actionPaint")
        self.actionEnCom = QtWidgets.QAction(QtGui.QIcon('./resources/images/EnCom.png'), '&EnCom', self)
        self.actionEnCom.setObjectName("actionEnCom")
        self.actionMV = QtWidgets.QAction(QtGui.QIcon('./resources/images/MV.png'), '&MV', self)
        self.actionMV.setObjectName("actionMV")
        self.actionBeatMV = QtWidgets.QAction(QtGui.QIcon("./resources/images/MV.png"), '&BeatMV', self)
        self.actionMV.setObjectName("actionBeatMV")
        

        
        #将动作信息添加到菜单栏
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSetting)
        self.menuFile.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionPaint)
        self.menuTools.addAction(self.actionEnCom)
        self.menuTools.addAction(self.actionMV)
        self.menuTools.addAction(self.actionBeatMV)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        #动作连接到相应的方法
        self.tabWidget.setCurrentIndex(0)

        # 菜单栏的功能定义
        self.actionNew.triggered.connect(self.openFileWindow)
        self.actionSave.triggered.connect(self.saveTable)
        self.actionSetting.triggered.connect(self.openDirWindow)
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)
        self.actionPaint.triggered.connect(self.openPaintWindow)
        self.actionEnCom.triggered.connect(self.EnCom)
        self.actionMV.triggered.connect(self.createMV)
        self.actionBeatMV.triggered.connect(self.createBeatMV)

        #工具栏的功能定义
        self.new.triggered.connect(self.openFileWindow)
        self.edit.triggered.connect(self.editable)
        self.save.triggered.connect(self.saveTable)
        self.refresh.triggered.connect(self.setRefresh)
        self.open.triggered.connect(self.openOrigin)


        #按钮点击操作
        self.pbtn_1.clicked.connect(self.createTable)


        #调用方法重命名控件
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    
    #设置控件的各种属性
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #主窗口的属性
        MainWindow.setWindowTitle(_translate("MainWindow", "material_tool"))

        #设置菜单栏的属性
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))

        #设置工具栏的属性
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

        #设置动作属性
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSetting.setText(_translate("MainWindow", "设置"))
        self.actionSetting.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionMV.setText(_translate("MainWindow", "MV素材"))
        self.actionMV.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionBeatMV.setText(_translate("MainWindow", "BeatMV素材"))
        self.actionBeatMV.setShortcut(_translate("MianWindow", "Ctrl+V"))
        self.actionPaint.setText(_translate("MainWindow", "展示"))
        self.actionPaint.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionEnCom.setText(_translate("MainWindow", "加密压缩"))
        self.actionEnCom.setShortcut(_translate("MainWindow", "Ctrl+K"))
    
    #动态初始化界面的一些控件	
    def initComBox(self):
		#定义type的comBox
        self.comBox_03 = QComboBox()
        self.comBox_03.addItems(self.itemList())
        self.comBox_03.setEditable(True)
        self.comBox_03.setCurrentIndex(-1)

        self.comBox_13 = QComboBox()
        self.comBox_13.addItems(self.itemList())
        self.comBox_13.setEditable(True)
        self.comBox_13.setCurrentIndex(-1)

        self.comBox_23 = QComboBox()
        self.comBox_23.addItems(self.itemList())
        self.comBox_23.setEditable(True)
        self.comBox_23.setCurrentIndex(-1)

        self.comBox_33 = QComboBox()
        self.comBox_33.addItems(self.itemList())
        self.comBox_33.setEditable(True)
        self.comBox_33.setCurrentIndex(-1)

        self.comBox_43 = QComboBox()
        self.comBox_43.addItems(self.itemList())
        self.comBox_43.setEditable(True)
        self.comBox_43.setCurrentIndex(-1)

        self.comBox_53 = QComboBox()
        self.comBox_53.addItems(self.itemList())
        self.comBox_53.setEditable(True)
        self.comBox_53.setCurrentIndex(-1)

        self.comBox_63 = QComboBox()
        self.comBox_63.addItems(self.itemList())
        self.comBox_63.setEditable(True)
        self.comBox_63.setCurrentIndex(-1)

        self.comBox_73 = QComboBox()
        self.comBox_73.addItems(self.itemList())
        self.comBox_73.setEditable(True)
        self.comBox_73.setCurrentIndex(-1)

        #在table中添加comBox
        self.tableWidget_4.setCellWidget(0, 3, self.comBox_03)
        self.tableWidget_4.setCellWidget(1, 3, self.comBox_13)
        self.tableWidget_4.setCellWidget(2, 3, self.comBox_23)
        self.tableWidget_4.setCellWidget(3, 3, self.comBox_33)
        self.tableWidget_4.setCellWidget(4, 3, self.comBox_43)
        self.tableWidget_4.setCellWidget(5, 3, self.comBox_53)
        self.tableWidget_4.setCellWidget(6, 3, self.comBox_63)
        self.tableWidget_4.setCellWidget(7, 3, self.comBox_73)

    def initBlurTable(self):
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_1.setColumnCount(12)
        self.tableWidget_1.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_1.setObjectName("tableWidget_1")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(11, item)
        self.tabWidget.addTab(self.tab_1, "")
        #设置列宽
        self.tableWidget_1.setColumnWidth(10,120)
        self.tableWidget_1.setColumnWidth(11,120)
        #虚化背景表格的顶栏字段
        _translate = QtCore.QCoreApplication.translate

        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "blur"))
        item = self.tableWidget_1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "refId"))
        item = self.tableWidget_1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "lelft_percentage"))
        item = self.tableWidget_1.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_1.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_1.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_1.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_1.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_1.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "bottom_percentage"))
        item = self.tableWidget_1.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "bottom_constant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Blur"))

        self.tableWidget_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def initNormalCellTable(self):
        #cell表格的json参数列表
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setColumnCount(14)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_2.setObjectName("tableWidget_2")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(13, item)
        self.tabWidget.addTab(self.tab_2, "")
        #设置列宽
        self.tableWidget_2.setColumnWidth(9,120)
        self.tableWidget_2.setColumnWidth(10,120)
        _translate = QtCore.QCoreApplication.translate
        #cell顶栏字段
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "mediaId"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "lelft_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "height_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "height_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "filter"))
        item = self.tableWidget_2.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "filterStrength"))
        item = self.tableWidget_2.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "rotation"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Cell"))

        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def initDynamicCellTable(self):
        #cell表格的json参数列表
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setColumnCount(15)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_2.setObjectName("tableWidget_2")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(14, item)
        self.tabWidget.addTab(self.tab_2, "")
        #设置列宽
        self.tableWidget_2.setColumnWidth(12,120)
        self.tableWidget_2.setColumnWidth(13,120)
        _translate = QtCore.QCoreApplication.translate
        #cell顶栏字段
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "imageId"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "mediaId"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "keyPath"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "contentSize_w"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "contentSize_h"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "lelft_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "height_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "height_constant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Cell"))

        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    
    def initIgnoreCellTable(self):
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setColumnCount(16)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_2.setObjectName("tableWidget_2")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(15, item)
        self.tabWidget.addTab(self.tab_2, "")
        #设置列宽
        self.tableWidget_2.setColumnWidth(12,120)
        self.tableWidget_2.setColumnWidth(13,120)
        _translate = QtCore.QCoreApplication.translate
        #cell顶栏字段
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "imageId"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "mediaId"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "keyPath"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "contentSize_w"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "contentSize_h"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "lelft_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "height_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "height_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "ignore"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Cell"))

        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


    def initNormalBgTable(self):
        #背景图片的json参数列表
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setColumnCount(11)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_3.setObjectName("tableWidget_3")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        self.tabWidget.addTab(self.tab_3, "")
        #设置列宽
        self.tableWidget_3.setColumnWidth(9,120)
        self.tableWidget_3.setColumnWidth(10,120)
        self.tableWidget_3.setColumnWidth(2,200)
        _translate = QtCore.QCoreApplication.translate
        #背景图片的顶栏字段
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "imageName"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "left_percentage"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "bottom_percentage"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "bottom_constant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Background"))

        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def initNormalTextTable(self):
        #文字的json参数列表
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setColumnCount(18)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_4.setObjectName("tableWidget_4")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(14,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(15,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(16,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(17,item)
        self.tabWidget.addTab(self.tab_4, "")
        #设置列宽
        self.tableWidget_4.setColumnWidth(3,300)
        self.tableWidget_4.setColumnWidth(7,600)
        _translate = QtCore.QCoreApplication.translate
        #文字表格的顶栏字段
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "textId"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "fontName"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "fontSize"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "canvasWidth"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "textColor"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "placeHolder"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "textAlignment"))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "left_percentage"))
        item = self.tableWidget_4.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_4.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_4.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_4.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_4.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_4.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "textSpacing"))
        item = self.tableWidget_4.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "lineSpacing"))
        item = self.tableWidget_4.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "angle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Text"))

        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def initDynamicTextTable(self):
        #文字的json参数列表
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setColumnCount(21)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_4.setObjectName("tableWidget_4")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(14,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(15,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(16,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(17,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(18,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(19,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(20,item)
        self.tabWidget.addTab(self.tab_4, "")
        #设置列宽
        self.tableWidget_4.setColumnWidth(3,300)
        self.tableWidget_4.setColumnWidth(7,600)
        self.tableWidget_4.setColumnWidth(20,150)
        _translate = QtCore.QCoreApplication.translate
        #文字表格的顶栏字段
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "textId"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "fontName"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "fontSize"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "canvasWidth"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "textColor"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "placeHolder"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "textAlignment"))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "left_percentage"))
        item = self.tableWidget_4.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_4.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_4.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_4.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_4.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_4.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "keyPath"))
        item = self.tableWidget_4.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "contentSize_w"))
        item = self.tableWidget_4.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "contentSize_h"))
        item = self.tableWidget_4.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "animation_name"))
        item = self.tableWidget_4.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "animation_type"))
        item = self.tableWidget_4.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "animation_resourceDirectory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Text"))

        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
	
    def initCustomDynamicTextTable(self):
    	#文字的json参数列表
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setColumnCount(20)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_4.setObjectName("tableWidget_4")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(14,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(15,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(16,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(17,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(18,item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(19,item)
        self.tabWidget.addTab(self.tab_4, "")
        #设置列宽
        self.tableWidget_4.setColumnWidth(3,300)
        self.tableWidget_4.setColumnWidth(7,600)
        self.tableWidget_4.setColumnWidth(15,120)
        _translate = QtCore.QCoreApplication.translate
        #文字表格的顶栏字段
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "textId"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "fontName"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "fontSize"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "canvasWidth"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "textColor"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "placeHolder"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "textAlignment"))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "left_percentage"))
        item = self.tableWidget_4.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_4.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_4.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_4.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_4.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_4.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "sourcePath"))
        item = self.tableWidget_4.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "textSpacing"))
        item = self.tableWidget_4.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "lineSpacing"))
        item = self.tableWidget_4.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "angle"))
        item = self.tableWidget_4.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "startFrame"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Text"))

        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def initLevelTable(self):
        #分层图片的参数列表
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_5.setColumnCount(11)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_5.setObjectName("tableWidget_5")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(10, item)
        self.tabWidget.addTab(self.tab_5, "")
        #设置列宽
        self.tableWidget_5.setColumnWidth(7,120)
        self.tableWidget_5.setColumnWidth(8,120)
        _translate = QtCore.QCoreApplication.translate
        #分层图片表格的顶栏字段
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "contentMode"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_5.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "height_percentage"))
        item = self.tableWidget_5.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "height_constant"))
        item = self.tableWidget_5.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "width_percentage"))
        item = self.tableWidget_5.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "width_constant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "level"))

        self.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def initDynamicTable(self):
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_6.setColumnCount(3)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 0, 1000, 450))
        self.tableWidget_6.setObjectName("tableWidget_6")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.tab_6, "")
        #设置列宽
        self.tableWidget_6.setColumnWidth(2,150)
        _translate = QtCore.QCoreApplication.translate
        #分层图片表格的顶栏字段
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "animation_type"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "animation_name"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "animation_resourceDirectory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Dynamic"))

        self.tableWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def initTable(self):
        if self.index > 0:
        	self.tabWidget.close()
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 130, 1000, 550))
        self.tabWidget.setObjectName("tabWidget")
        #静态模版
        #初始化普通模版的table
        if self.cbox_1.isChecked() == False and self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == False:
            if self.spinBox_1.value() != 0:
                self.initNormalCellTable()
                self.initNormalBgTable()
                if self.spinBox_3.value() != 0:
                    self.initNormalTextTable()

		#初始化背景自动虚化模板的table
        if self.cbox_1.isChecked() == True and self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == False:
            if self.spinBox_1.value() != 0:
                self.initBlurTable()
                self.initNormalCellTable()
                self.initNormalBgTable()
                if self.spinBox_3.value() != 0:
                    self.initNormalTextTable()

		#初始化图片有上下层次模板的table
        if self.cbox_1.isChecked() == False and self.cbox_2.isChecked() == True and self.cbox_3.isChecked() == False:
            if self.spinBox_1.value() != 0:
                self.initNormalCellTable()
                self.initNormalBgTable()
                self.initLevelTable()
                if self.spinBox_3.value() != 0:
                    self.initNormalTextTable()
				
        #动态模版
		#初始化动态模板的table
        if self.cbox_1.isChecked() == False and self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == True:
            if self.spinBox_1.value() != 0:
                #选择不同类型的media
                if self.cbox_6.isChecked() == False:
                    self.initDynamicCellTable()
                if self.cbox_6.isChecked() == True:
                    self.initIgnoreCellTable()

                self.initNormalBgTable()
                self.initDynamicTable()
                #选择不同类型的text， text or animation_text
                if self.spinBox_3.value() != 0:
                    if self.cbox_5.isChecked() == False:
                        self.initDynamicTextTable()
                    if self.cbox_5.isChecked() == True:
                        self.initCustomDynamicTextTable()
				

		#初始化图片有上下层次的动态模版
        if self.cbox_1.isChecked() == False and self.cbox_2.isChecked() == True and self.cbox_3.isChecked() == True:
            if self.spinBox_1.value() != 0:
                if self.cbox_6.isChecked() == False:
                    self.initDynamicCellTable()
                if self.cbox_6.isChecked() == True:
                    self.initIgnoreCellTable()
                
                self.initNormalBgTable()
                self.initDynamicTable()
                self.initLevelTable()

                if self.spinBox_3.value() != 0:
                    if self.cbox_5.isChecked() == False:
                        self.initDynamicTextTable()
                    if self.cbox_5.isChecked() == True:
                        self.initCustomDynamicTextTable()

        self.tabWidget.show()
        self.index +=1










                



        






