# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lasttools.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_MainWindow(object):
    #在界面中添加控件
    def setupUi(self, MainWindow):
        #设置主窗口，主窗口分为菜单栏，工具栏，状态栏，标题栏
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 640)
        MainWindow.setFixedSize(1000, 640)
        MainWindow.setWindowIcon(QtGui.QIcon('./images/tool.png'))

        

        #主体部分添加控件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #添加tabWidget到centralWidget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 1000, 550))
        self.tabWidget.setObjectName("tabWidget")
      
        #定义type的comBox
        self.comBox_03 = QtWidgets.QComboBox()
        self.comBox_03.addItems(self.itemList())
        self.comBox_03.setEditable(True)
        self.comBox_03.setCurrentIndex(-1)

        self.comBox_13 = QtWidgets.QComboBox()
        self.comBox_13.addItems(self.itemList())
        self.comBox_13.setEditable(True)
        self.comBox_13.setCurrentIndex(-1)

        self.comBox_23 = QtWidgets.QComboBox()
        self.comBox_23.addItems(self.itemList())
        self.comBox_23.setEditable(True)
        self.comBox_23.setCurrentIndex(-1)

        self.comBox_33 = QtWidgets.QComboBox()
        self.comBox_33.addItems(self.itemList())
        self.comBox_33.setEditable(True)
        self.comBox_33.setCurrentIndex(-1)

        self.comBox_43 = QtWidgets.QComboBox()
        self.comBox_43.addItems(self.itemList())
        self.comBox_43.setEditable(True)
        self.comBox_43.setCurrentIndex(-1)


        #虚化背景的json参数表格
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_1.setColumnCount(12)
        self.tableWidget_1.setRowCount(5)
        self.tableWidget_1.setGeometry(QtCore.QRect(0, 0, 1000, 340))
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

        #cell表格的json参数列表
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setColumnCount(11)
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 1000, 340))
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
        self.tabWidget.addTab(self.tab_2, "")

        #背景图片的json参数列表
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setColumnCount(11)
        self.tableWidget_3.setRowCount(5)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 1000, 340))
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

        #文字的json参数列表
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setColumnCount(15)
        self.tableWidget_4.setRowCount(5)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 1000, 340))
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
        self.tabWidget.addTab(self.tab_4, "")

        #设置列宽
        self.tableWidget_1.setColumnWidth(10,120)
        self.tableWidget_1.setColumnWidth(11,120)
        self.tableWidget_2.setColumnWidth(9,120)
        self.tableWidget_2.setColumnWidth(10,120)
        self.tableWidget_3.setColumnWidth(9,120)
        self.tableWidget_3.setColumnWidth(10,120)
        self.tableWidget_4.setColumnWidth(3,230)
        self.tableWidget_4.setColumnWidth(7,600)
        

       

        #将comBox放入相应的table中
        self.tableWidget_4.setCellWidget(0, 3, self.comBox_03)
        self.tableWidget_4.setCellWidget(1, 3, self.comBox_13)
        self.tableWidget_4.setCellWidget(2, 3, self.comBox_23)
        self.tableWidget_4.setCellWidget(3, 3, self.comBox_33)
        self.tableWidget_4.setCellWidget(4, 3, self.comBox_43)



        #设置tablewidget为不可编辑的状态
        self.tableWidget_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        #
        MainWindow.setCentralWidget(self.centralwidget)

        #选择素材组
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(45,10,100,30))
        self.label_1.setText("素材组：")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.comBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comBox_1.setGeometry(QtCore.QRect(155, 10, 300, 30))
        self.comBox_1.setEditable(True)
        self.comBox_1.setCurrentIndex(-1)
        self.comBox_1.setObjectName("comBox_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(545,10,100,30))
        self.label_2.setText("json文件：")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comBox_1.setGeometry(QtCore.QRect(645, 10, 300, 30))
        self.comBox_1.setEditable(True)
        self.comBox_1.setCurrentIndex(-1)
        self.comBox_1.setObjectName("comBox_1")

        #选择素材的组件部分:blur,cell,background,text,picturelevel(控制图层）
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 60, 30))
        self.label_3.setText("Blur:")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.spinBox_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_1.setGeometry(QtCore.QRect(100,50,50,30))

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 50, 60, 30))
        self.label_4.setText("Cell:")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(240, 50, 50, 30))

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 50, 90, 30))
        self.label_5.setText("Background:")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(410, 50, 50, 30))

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 50, 60, 30))
        self.label_6.setText("Text:")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(550, 50, 50, 30))

        #增加RadioButton
        self.rbtn_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_1.setGeometry(QtCore.QRect(620,50,60,30))
        self.rbtn_1.setText("Level")
        self.rbtn_1.setObjectName("rbtn_1")

        #增加button
        self.pbtn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_1.setGeometry(QtCore.QRect(870,50,100,30))
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
        self.open_ = QtWidgets.QAction(QtGui.QIcon('./images/open.png'), '&open', self)
        self.new = QtWidgets.QAction(QtGui.QIcon('./images/new.png'), '&new', self)
        self.edit = QtWidgets.QAction(QtGui.QIcon('./images/edit.png'),'&edit', self)
        self.save = QtWidgets.QAction(QtGui.QIcon('./images/save.png'), '&save', self)
        self.toolBar.addAction(self.open_)
        self.toolBar.addAction(self.new)
        self.toolBar.addAction(self.edit)
        self.toolBar.addAction(self.save)


        #定义动作信息
        self.actionOpen = QtWidgets.QAction(QtGui.QIcon('./images/open.png'), '&Open', self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(QtGui.QIcon('./images/new.png'), '&New', self)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(QtGui.QIcon('./images/save_as.png'), '&Save', self)
        self.actionSave.setObjectName("actionSave")
        self.actionSetting = QtWidgets.QAction(QtGui.QIcon('./images/setting.png'), '&Setting', self)
        self.actionSetting.setObjectName("actionSetting")
        self.actionQuit = QtWidgets.QAction(QtGui.QIcon('./images/quit.png'), '&Quit', self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPaint = QtWidgets.QAction(QtGui.QIcon('./images/paint.png'), '&Paint', self)
        self.actionPaint.setObjectName("actionPaint")

        
        #将动作信息添加到菜单栏
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSetting)
        self.menuFile.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionPaint)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        #动作连接到相应的方法
        self.tabWidget.setCurrentIndex(0)

        #菜单栏的功能定义
        self.actionOpen.triggered.connect(self.openFile)
        self.actionNew.triggered.connect(self.openFileWindow)
        self.actionSave.triggered.connect(self.saveTable)
        self.actionSetting.triggered.connect(self.openDirWindow)
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)
        self.actionPaint.triggered.connect(self.openPaintWindow)

        #工具栏的功能定义
        self.open_.triggered.connect(self.openFile)
        self.new.triggered.connect(self.openFileWindow)
        self.edit.triggered.connect(self.editable)
        self.save.triggered.connect(self.saveTable)




        #调用方法重命名控件
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    

    #设置控件的各种属性
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        #主窗口的属性
        MainWindow.setWindowTitle(_translate("MainWindow", "material_tool"))

        #虚化背景表格的顶栏字段
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

        #tabWidget顶栏字段
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Cell"))

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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Text"))

        #设置菜单栏的属性
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))


        #设置工具栏的属性
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


        #设置动作属性
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionSetting.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPaint.setText(_translate("MainWindow", "Paint"))
        self.actionPaint.setShortcut(_translate("MainWindow", "Ctrl+R"))


    def itemList(self):
        with open("./font.json", "r") as lf:
            jsonStr = lf.read()
            dic = json.loads(jsonStr,strict = False)
            self.Lis = dic.keys()
           
        return self.Lis




