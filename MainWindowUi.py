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
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 640))
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





        #tabWidget的属性
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setColumnCount(11)
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 1000, 340))
        self.tableWidget_2.setObjectName("tableWidget_2")

       
        # self.tableWidget_2.setTextAlignment(Qt.AlignHCenter)
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
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_3.setColumnCount(13)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(12, item)
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1000, 340))
        self.tableWidget.setObjectName("tableWidget")


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14,item)
        self.tabWidget.addTab(self.tab_3, "")

        #设置列宽
        self.tableWidget.setColumnWidth(3,230)
        self.tableWidget.setColumnWidth(7,600)
        self.tableWidget_3.setColumnWidth(4,200)
       

        #将comBox放入相应的table中

        self.tableWidget.setCellWidget(0, 3, self.comBox_03)
        self.tableWidget.setCellWidget(1, 3, self.comBox_13)
        self.tableWidget.setCellWidget(2, 3, self.comBox_23)
        self.tableWidget.setCellWidget(3, 3, self.comBox_33)
        self.tableWidget.setCellWidget(4, 3, self.comBox_43)



        #设置tablewidget为不可编辑的状态
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        #
        MainWindow.setCentralWidget(self.centralwidget)

        #菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))

        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(460,390,80,20))
        self.label_1.setText("templatedId:")
        self.label_1.setObjectName("label_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(400,420,200,20))
        self.lineEdit_1.setObjectName("lineEdit_1")

        #状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Non Editable")

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
        self.actionQuit = QtWidgets.QAction(QtGui.QIcon('./images/quit.png'), '&Quit', self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPaint = QtWidgets.QAction(QtGui.QIcon('./images/paint.png'), '&Paint', self)
        self.actionPaint.setObjectName("actionPaint")

        #将动作信息添加到菜单栏
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionPaint)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        #动作连接到相应的方法
        self.tabWidget.setCurrentIndex(0)

        #菜单栏的功能定义
        self.actionOpen.triggered.connect(self.openFile)
        self.actionNew.triggered.connect(self.createNewTable)
        self.actionSave.triggered.connect(self.saveTable)
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)
        self.actionPaint.triggered.connect(self.openPaintWindow)

        #工具栏的功能定义
        self.open_.triggered.connect(self.openFile)
        self.new.triggered.connect(self.createNewTable)
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Cell"))

        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "blur"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "refId"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "imageName"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "left_percentage"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_3.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "bottom_percentage"))
        item = self.tableWidget_3.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "bottom_constant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Background"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "textId"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "fontName"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "fontSize"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "canvasWidth"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "textColor"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "placeHolder"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "textAlignment"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "left_percentage"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "top_constant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Text"))

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
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPaint.setText(_translate("MainWindow", "Paint"))
        self.actionPaint.setShortcut(_translate("MainWindow", "Ctrl+P"))


    def itemList(self):
        with open("./font.json", "r") as lf:
            jsonStr = lf.read()
            dic = json.loads(jsonStr,strict = False)
            self.Lis = dic.keys()
           
        return self.Lis




