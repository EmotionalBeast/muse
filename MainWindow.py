# -*- coding: utf-8 -*-
#author: Jhin Yao

import json, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
													QTableWidgetItem, QAbstractItemView, QComboBox)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5 import QtWidgets, QtCore
from MainWindowUi import Ui_MainWindow
from PaintWindow import MyPaintWindow
from DirWindow import MyDirWindow
from FileWindow import MyFileWindow


class MyMainWindow(QMainWindow,Ui_MainWindow):
	#初始化
	def __init__(self):
		super(MyMainWindow,self).__init__()
		self.setupUi(self)
		self.myFileWindow = MyFileWindow()
		self.myDirWindow = MyDirWindow()
		
		with open("./resources/json/font.json", 'r') as lf:
			jsonStr = lf.read()
			self.dict1 = json.loads(jsonStr, strict = False)
		#反转字典，赋值给新的字典
		self.dict2 = {v:k for k,v in self.dict1.items()}


	#将列表赋给comBox
	def templateList(self,text):
		if self.comBox_2.count() != 0:
			self.comBox_2.clear()
		list_3 = []
		with open("./resources/json/setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		self.path = dic["directory"] + "/" + text + "/in"

		for root,dirs,files in os.walk(self.path):
			for dir in dirs:
				if self.path == root:
					self.count = len(dir) * (-1)
			for file in files:
				if file == "template.json":
					name = file + "-" + root[self.count:]
					list_3.append(name)
					list_3.sort()

		self.comBox_2.addItems(list_3)
		self.comBox_2.setCurrentIndex(-1)

	def itemList(self):
		with open("./resources/json/font.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr,strict = False)
			list_1 = dic.keys()
		return list_1

	def dirList(self):
		list_2 = []
		with open("./resources/json/setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		path = dic["directory"]
		for root,dirs,files in os.walk(path):
			for dir in dirs:
				if root == path:
					list_2.append(dir)
		return list_2

	def setRefresh(self):
		bc = self.comBox_1.count()
		text_1 = self.comBox_1.currentText()
		self.comBox_1.clear()
		self.comBox_1.addItems(self.dirList())
		ac = self.comBox_1.count()
		if bc != ac:
			self.comBox_1.setCurrentIndex(-1)
			self.comBox_2.setCurrentIndex(-1)
		else:
			self.comBox_1.setCurrentText(text_1)
		

	#打开关联的窗口
	def openFileWindow(self):
		self.myFileWindow = MyFileWindow()
		self.myFileWindow.setWindowModality(Qt.ApplicationModal)
		self.myFileWindow.show()

	def openPaintWindow(self):
		dic = self.getTableValue()
		self.myPaintWindow = MyPaintWindow(dic)
		self.myPaintWindow.setWindowModality(Qt.ApplicationModal)
		self.myPaintWindow.show()

	def openDirWindow(self):
		self.myDirWindow.setWindowModality(Qt.ApplicationModal)
		self.myDirWindow.show()


	#关闭主窗口提示
	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message', 'You sure to quit?',
									 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	#表格的可编辑性
	def editable(self):
		self.tableWidget_1.setEditTriggers(QAbstractItemView.CurrentChanged)
		self.tableWidget_2.setEditTriggers(QAbstractItemView.CurrentChanged)
		self.tableWidget_3.setEditTriggers(QAbstractItemView.CurrentChanged)
		self.tableWidget_4.setEditTriggers(QAbstractItemView.CurrentChanged)
		self.tableWidget_5.setEditTriggers(QAbstractItemView.CurrentChanged)
		self.statusbar.showMessage("Editable")

	def nonEditable(self):
		self.tableWidget_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.statusbar.showMessage("Non Editable")


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

	def initTable(self):
		#初始化普通模版的table
		if self.cbox_1.isChecked() == False and self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == False:
			if self.spinBox_3.value() != 0:
				self.initNormalCellTable()
				self.initNormalBgTableI()
				self.initNormalTextTable()
			else:
				self.initNormalCellTable()
				self.initNormalBgTableI()
		#初始化背景自动虚化模板的table
		if self.cbox_1.isChecked() == True and self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == False:
			if self.spinBox_3.value() != 0:
				self.initBlurTable()
				self.initNormalCellTable()
				self.initNormalBgTable()
				self.initNormalTextTable()
			else:
				self.initBlurTable()
				self.initNormalCellTable()
				self.initNormalBgTableI()
		#初始化图片有上下层次模板的table
		if self.cbox_1.isChecked() == False and self.cbox_2.isChecked() == True and self.cbox_3.isChecked() == False:
			if self.spinBox_3.value() != 0:
				self.initLevelCellTable()
				self.initNormalBgTable()
				self.initNormalTextTable()
				self.initLevelTable()
			else:
				self.initLevelCellTable()
				self.initNormalBgTable()
				self.initLevelTable()
		#初始化动态模板的table
		if self.cbox_1.isChecked() == False and self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == True:
			if self.spinBox_3.value() != 0:
				self.initDynamicCellTable()
				self.initDynamicBgTable()
				self.initDynamicTextTable()
				self.initDynamicTable()
			else:
				self.initDynamicCellTable()
				self.initDynamicBgTable()
				self.initDynamicTable()

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

	def initNormalCellTable(self):
		#cell表格的json参数列表
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
		self.tableWidget_2.setColumnCount(11)
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
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Cell"))

	def initLevelCellTable(self):
		#cell表格的json参数列表
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
		self.tableWidget_2.setColumnCount(12)
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
		self.tabWidget.addTab(self.tab_2, "")
		#设置列宽
		self.tableWidget_2.setColumnWidth(10,120)
		self.tableWidget_2.setColumnWidth(11,120)
		_translate = QtCore.QCoreApplication.translate
		#cell顶栏字段
		item = self.tableWidget_2.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "id"))
		item = self.tableWidget_2.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "customIconId"))
		item = self.tableWidget_2.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "type"))
		item = self.tableWidget_2.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "mediaId"))
		item = self.tableWidget_2.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "left_percentage"))
		item = self.tableWidget_2.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "left_constant"))
		item = self.tableWidget_2.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "right_percentage"))
		item = self.tableWidget_2.horizontalHeaderItem(7)
		item.setText(_translate("MainWindow", "right_constant"))
		item = self.tableWidget_2.horizontalHeaderItem(8)
		item.setText(_translate("MainWindow", "top_percentage"))
		item = self.tableWidget_2.horizontalHeaderItem(9)
		item.setText(_translate("MainWindow", "top_constant"))
		item = self.tableWidget_2.horizontalHeaderItem(10)
		item.setText(_translate("MainWindow", "height_percentage"))
		item = self.tableWidget_2.horizontalHeaderItem(11)
		item.setText(_translate("MainWindow", "height_constant"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Cell"))

	def initDynamicCellTable(self):
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
		self.tableWidget_2.setColumnWidth(12,120)
		self.tableWidget_2.setColumnWidth(13,120)
		_translate = QtCore.QCoreApplication.translate
		#cell顶栏字段
		item = self.tableWidget_2.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "id"))
		item = self.tableWidget_2.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "type"))
		item = self.tableWidget_2.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "mediaId"))
		item = self.tableWidget_2.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "keyPath"))
		item = self.tableWidget_2.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "contentSize_x"))
		item = self.tableWidget_2.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "contentSize_y"))
		item = self.tableWidget_2.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "lelft_percentage"))
		item = self.tableWidget_2.horizontalHeaderItem(7)
		item.setText(_translate("MainWindow", "left_constant"))
		item = self.tableWidget_2.horizontalHeaderItem(8)
		item.setText(_translate("MainWindow", "right_percentage"))
		item = self.tableWidget_2.horizontalHeaderItem(9)
		item.setText(_translate("MainWindow", "right_constant"))
		item = self.tableWidget_2.horizontalHeaderItem(10)
		item.setText(_translate("MainWindow", "top_percentage"))
		item = self.tableWidget_2.horizontalHeaderItem(11)
		item.setText(_translate("MainWindow", "top_constant"))
		item = self.tableWidget_2.horizontalHeaderItem(12)
		item.setText(_translate("MainWindow", "height_percentage"))
		item = self.tableWidget_2.horizontalHeaderItem(13)
		item.setText(_translate("MainWindow", "height_constant"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Cell"))

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

	def initDynamicBgTable(self):
		#背景图片的json参数列表
		self.tab_3 = QtWidgets.QWidget()
		self.tab_3.setObjectName("tab_3")
		self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
		self.tableWidget_3.setColumnCount(14)
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
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_3.setHorizontalHeaderItem(11, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_3.setHorizontalHeaderItem(12, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_3.setHorizontalHeaderItem(13, item)
		self.tabWidget.addTab(self.tab_3, "")
		#设置列宽
		self.tableWidget_3.setColumnWidth(12,120)
		self.tableWidget_3.setColumnWidth(13,120)
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
		item.setText(_translate("MainWindow", "keyPath"))
		item = self.tableWidget_3.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "contentSize_x"))
		item = self.tableWidget_3.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "contentSize_y"))
		item = self.tableWidget_3.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "left_percentage"))
		item = self.tableWidget_3.horizontalHeaderItem(7)
		item.setText(_translate("MainWindow", "left_constant"))
		item = self.tableWidget_3.horizontalHeaderItem(8)
		item.setText(_translate("MainWindow", "right_percentage"))
		item = self.tableWidget_3.horizontalHeaderItem(9)
		item.setText(_translate("MainWindow", "right_constant"))
		item = self.tableWidget_3.horizontalHeaderItem(10)
		item.setText(_translate("MainWindow", "top_percentage"))
		item = self.tableWidget_3.horizontalHeaderItem(11)
		item.setText(_translate("MainWindow", "top_constant"))
		item = self.tableWidget_3.horizontalHeaderItem(12)
		item.setText(_translate("MainWindow", "bottom_percentage"))
		item = self.tableWidget_3.horizontalHeaderItem(13)
		item.setText(_translate("MainWindow", "bottom_constant"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Background"))

	def initNormalTextTable(self):
		#文字的json参数列表
		self.tab_4 = QtWidgets.QWidget()
		self.tab_4.setObjectName("tab_4")
		self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
		self.tableWidget_4.setColumnCount(15)
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
		self.tabWidget.addTab(self.tab_4, "")
		#设置列宽
		self.tableWidget_4.setColumnWidth(3,230)
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
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Text"))

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
		self.tableWidget_4.setColumnWidth(3,230)
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
		item.setText(_translate("MainWindow", "contentSize_x"))
		item = self.tableWidget_4.horizontalHeaderItem(17)
		item.setText(_translate("MainWindow", "contentSize_y"))
		item = self.tableWidget_4.horizontalHeaderItem(18)
		item.setText(_translate("MainWindow", "animation_name"))
		item = self.tableWidget_4.horizontalHeaderItem(19)
		item.setText(_translate("MainWindow", "animation_type"))
		item = self.tableWidget_4.horizontalHeaderItem(20)
		item.setText(_translate("MainWindow", "animation_resourceDirectory"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Text"))

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

	#读入json文件，显示在页面中
	def readJson(self):
		temp_1 = self.comBox_1.currentText()
		temp_2 = self.comBox_2.currentText()
		with open("./resources/json/setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		path = dic["directory"] + "/" + temp_1 + "/in/" + temp_2[self.count:] + "/template.json" 
		with open(path, "r") as lf:
			size = os.path.getsize(path)
			if size != 0:
				jsonStr = lf.read()
				dic = json.loads(jsonStr, strict = False)
				return dic
			else:
				return 0

	def resolveJson(self):
		self.blur_list = []
		self.cell_list = []
		self.bg_list = []
		self.text_list = []
		self.level_list = []
		self.item = []
		self.cbox_1.setChecked(False)
		self.cbox_2.setChecked(False)
		self.cbox_3.setChecked(False)
		self.dic = self.readJson()
		if self.dic == 0:
			self.spinBox_1.setValue(0)
			self.spinBox_2.setValue(0)
			self.spinBox_3.setValue(0)
		else:
			if "animation" in self.dic.keys():
				self.cbox_3.setChecked(True)
			item = self.dic["elements"]
			for i in range(len(item)):
				if "blur" in item[i].keys():
					self.blur_list.append(item[i])
					self.cbox_1.setChecked(True)
				if "mediaId" in item[i].keys():
					self.cell_list.append(item[i])
				if "imageName" in item[i].keys():
					self.bg_list.append(item[i])
				if "textId" in item[i].keys():
					self.text_list.append(item[i])
				if "contentMode" in item[i].keys():
					self.level_list.append(item[i])
					self.cbox_2.setChecked(True)

			self.spinBox_1.setValue(len(self.cell_list))
			self.spinBox_2.setValue(len(self.bg_list))
			self.spinBox_3.setValue(len(self.text_list))

	def initDate(self):
		self.resolveJson()
		self.initTable()
		if self.cbox_1.isChecked() == True:
			self.tableWidget_1.setRowCount(1)
			for i in range(len(self.blur_list)):
				self.tableWidget_1.setItem(i,0,QTableWidgetItem(self.blur_list[i]['id']))
				self.tableWidget_1.setItem(i,1,QTableWidgetItem(self.blur_list[i]['type']))
				self.tableWidget_1.setItem(i,2,QTableWidgetItem(str(self.blur_list[i]['blur'])))
				self.tableWidget_1.setItem(i,3,QTableWidgetItem(self.blur_list[i]['refId']))
				self.tableWidget_1.setItem(i,4,QTableWidgetItem(str(self.blur_list[i]['constraints']['left']['percentage'])))
				self.tableWidget_1.setItem(i,5,QTableWidgetItem(str(self.blur_list[i]['constraints']['left']['constant'])))
				self.tableWidget_1.setItem(i,6,QTableWidgetItem(str(self.blur_list[i]['constraints']['right']['percentage'])))
				self.tableWidget_1.setItem(i,7,QTableWidgetItem(str(self.blur_list[i]['constraints']['right']['constant'])))
				self.tableWidget_1.setItem(i,8,QTableWidgetItem(str(self.blur_list[i]['constraints']['top']['percentage'])))
				self.tableWidget_1.setItem(i,9,QTableWidgetItem(str(self.blur_list[i]['constraints']['top']['constant'])))
				self.tableWidget_1.setItem(i,10,QTableWidgetItem(str(self.blur_list[i]['constraints']['bottom']['percentage'])))
				self.tableWidget_1.setItem(i,11,QTableWidgetItem(str(self.blur_list[i]['constraints']['bottom']['constant'])))
		else:
			self.tableWidget_1.setRowCount(0)

		if self.spinBox_1.value() != 0:
			if self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == False:
				self.tableWidget_2.setRowCount(self.spinBox_1.value())
				for i in range(len(self.cell_list)):
					self.tableWidget_2.setItem(i,0,QTableWidgetItem(self.cell_list[i]['id']))
					self.tableWidget_2.setItem(i,1,QTableWidgetItem(self.cell_list[i]['type']))
					self.tableWidget_2.setItem(i,2,QTableWidgetItem(self.cell_list[i]['mediaId']))
					self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['percentage'])))
					self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['constant'])))
					self.tableWidget_2.setItem(i,5,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['percentage'])))
					self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['constant'])))
					self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['percentage'])))
					self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['constant'])))
					self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['percentage'])))
					self.tableWidget_2.setItem(i,10,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['constant'])))
			elif self.cbox_2.isChecked() == True and self.cbox_3.isChecked() == False: 
				self.tableWidget_2.setRowCount(self.spinBox_1.value())
				for i in range(len(self.cell_list)):
					self.tableWidget_2.setItem(i,0,QTableWidgetItem(self.cell_list[i]['id']))
					self.tableWidget_2.setItem(i,1,QTableWidgetItem(self.cell_list[i]['customIconId']))
					self.tableWidget_2.setItem(i,2,QTableWidgetItem(self.cell_list[i]['type']))
					self.tableWidget_2.setItem(i,3,QTableWidgetItem(self.cell_list[i]['mediaId']))
					self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['percentage'])))
					self.tableWidget_2.setItem(i,5,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['constant'])))
					self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['percentage'])))
					self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['constant'])))
					self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['percentage'])))
					self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['constant'])))
					self.tableWidget_2.setItem(i,10,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['percentage'])))
					self.tableWidget_2.setItem(i,11,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['constant'])))
			elif self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == True:
				self.tableWidget_2.setRowCount(self.spinBox_1.value())
				for i in range(len(self.cell_list)):
					self.tableWidget_2.setItem(i,0,QTableWidgetItem(self.cell_list[i]['id']))
					self.tableWidget_2.setItem(i,1,QTableWidgetItem(self.cell_list[i]['type']))
					self.tableWidget_2.setItem(i,2,QTableWidgetItem(self.cell_list[i]['mediaId']))
					self.tableWidget_2.setItem(i,3,QTableWidgetItem(self.cell_list[i]['keyPath']))
					self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(self.cell_list[i]['contentSize'][0])))
					self.tableWidget_2.setItem(i,5,QTableWidgetItem(str(self.cell_list[i]['contentSize'][1])))
					self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['percentage'])))
					self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['constant'])))
					self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['percentage'])))
					self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['constant'])))
					self.tableWidget_2.setItem(i,10,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['percentage'])))
					self.tableWidget_2.setItem(i,11,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['constant'])))
					self.tableWidget_2.setItem(i,12,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['percentage'])))
					self.tableWidget_2.setItem(i,13,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['constant'])))
			else:
				QMessageBox.information(self,"提示","只能选择一个！")
		else:
			self.tableWidget_2.setRowCount(self.spinBox_1.value())

		if self.spinBox_2.value() != 0:
			if self.cbox_3.isChecked() == False:
				self.tableWidget_3.setRowCount(self.spinBox_2.value())
				for i in range(len(self.bg_list)):
					self.tableWidget_3.setItem(i,0,QTableWidgetItem(self.bg_list[i]['id']))
					self.tableWidget_3.setItem(i,1,QTableWidgetItem(self.bg_list[i]['type']))
					self.tableWidget_3.setItem(i,2,QTableWidgetItem(self.bg_list[i]['imageName']))
					self.tableWidget_3.setItem(i,3,QTableWidgetItem(str(self.bg_list[i]['constraints']['left']['percentage'])))
					self.tableWidget_3.setItem(i,4,QTableWidgetItem(str(self.bg_list[i]['constraints']['left']['constant'])))
					self.tableWidget_3.setItem(i,5,QTableWidgetItem(str(self.bg_list[i]['constraints']['right']['percentage'])))
					self.tableWidget_3.setItem(i,6,QTableWidgetItem(str(self.bg_list[i]['constraints']['right']['constant'])))
					self.tableWidget_3.setItem(i,7,QTableWidgetItem(str(self.bg_list[i]['constraints']['top']['percentage'])))
					self.tableWidget_3.setItem(i,8,QTableWidgetItem(str(self.bg_list[i]['constraints']['top']['constant'])))
					self.tableWidget_3.setItem(i,9,QTableWidgetItem(str(self.bg_list[i]['constraints']['bottom']['percentage'])))
					self.tableWidget_3.setItem(i,10,QTableWidgetItem(str(self.bg_list[i]['constraints']['bottom']['constant'])))
			else:
				self.tableWidget_3.setRowCount(self.spinBox_2.value())
				for i in range(len(self.bg_list)):
					self.tableWidget_3.setItem(i,0,QTableWidgetItem(self.bg_list[i]['id']))
					self.tableWidget_3.setItem(i,1,QTableWidgetItem(self.bg_list[i]['type']))
					self.tableWidget_3.setItem(i,2,QTableWidgetItem(self.bg_list[i]['imageName']))
					self.tableWidget_3.setItem(i,3,QTableWidgetItem(self.bg_list[i]['keyPath']))
					self.tableWidget_3.setItem(i,4,QTableWidgetItem(str(self.bg_list[i]['contentSize'][0])))
					self.tableWidget_3.setItem(i,5,QTableWidgetItem(str(self.bg_list[i]['imageName'][0])))
					self.tableWidget_3.setItem(i,6,QTableWidgetItem(str(self.bg_list[i]['constraints']['left']['percentage'])))
					self.tableWidget_3.setItem(i,7,QTableWidgetItem(str(self.bg_list[i]['constraints']['left']['constant'])))
					self.tableWidget_3.setItem(i,8,QTableWidgetItem(str(self.bg_list[i]['constraints']['right']['percentage'])))
					self.tableWidget_3.setItem(i,9,QTableWidgetItem(str(self.bg_list[i]['constraints']['right']['constant'])))
					self.tableWidget_3.setItem(i,10,QTableWidgetItem(str(self.bg_list[i]['constraints']['top']['percentage'])))
					self.tableWidget_3.setItem(i,11,QTableWidgetItem(str(self.bg_list[i]['constraints']['top']['constant'])))
					self.tableWidget_3.setItem(i,12,QTableWidgetItem(str(self.bg_list[i]['constraints']['bottom']['percentage'])))
					self.tableWidget_3.setItem(i,13,QTableWidgetItem(str(self.bg_list[i]['constraints']['bottom']['constant'])))
		else:
			self.tableWidget_3.setRowCount(self.spinBox_2.value())

		if self.spinBox_3.value() != 0:
			if self.cbox_3.isChecked() == False:
				self.tableWidget_4.setRowCount(self.spinBox_3.value())
				self.initComBox()
				for i in range(len(self.text_list)):
					self.tableWidget_4.setItem(i,0,QTableWidgetItem(self.text_list[i]['id']))
					self.tableWidget_4.setItem(i,1,QTableWidgetItem(self.text_list[i]['type']))
					self.tableWidget_4.setItem(i,2,QTableWidgetItem(self.text_list[i]['textId']))
					self.tableWidget_4.cellWidget(i,3).setCurrentText(self.dict2[self.text_list[i]["fontName"]])
					self.tableWidget_4.setItem(i,4,QTableWidgetItem(str(self.text_list[i]['fontSize'])))
					self.tableWidget_4.setItem(i,5,QTableWidgetItem(str(self.text_list[i]['canvasWidth'])))
					self.tableWidget_4.setItem(i,6,QTableWidgetItem(self.text_list[i]['textColor']))
					self.tableWidget_4.setItem(i,7,QTableWidgetItem(self.text_list[i]['placeHolder']))
					self.tableWidget_4.setItem(i,8,QTableWidgetItem(self.text_list[i]['textAlignment']))
					self.tableWidget_4.setItem(i,9,QTableWidgetItem(str(self.text_list[i]['constraints']['left']['percentage'])))
					self.tableWidget_4.setItem(i,10,QTableWidgetItem(str(self.text_list[i]['constraints']['left']['constant'])))
					self.tableWidget_4.setItem(i,11,QTableWidgetItem(str(self.text_list[i]['constraints']['right']['percentage'])))
					self.tableWidget_4.setItem(i,12,QTableWidgetItem(str(self.text_list[i]['constraints']['right']['constant'])))
					self.tableWidget_4.setItem(i,13,QTableWidgetItem(str(self.text_list[i]['constraints']['top']['percentage'])))
					self.tableWidget_4.setItem(i,14,QTableWidgetItem(str(self.text_list[i]['constraints']['top']['constant'])))
			else:
				self.tableWidget_4.setRowCount(self.spinBox_3.value())
				self.initComBox()
				for i in range(len(self.text_list)):
					self.tableWidget_4.setItem(i,0,QTableWidgetItem(self.text_list[i]['id']))
					self.tableWidget_4.setItem(i,1,QTableWidgetItem(self.text_list[i]['type']))
					self.tableWidget_4.setItem(i,2,QTableWidgetItem(self.text_list[i]['textId']))
					self.tableWidget_4.cellWidget(i,3).setCurrentText(self.dict2[self.text_list[i]["fontName"]])
					self.tableWidget_4.setItem(i,4,QTableWidgetItem(str(self.text_list[i]['fontSize'])))
					self.tableWidget_4.setItem(i,5,QTableWidgetItem(str(self.text_list[i]['canvasWidth'])))
					self.tableWidget_4.setItem(i,6,QTableWidgetItem(self.text_list[i]['textColor']))
					self.tableWidget_4.setItem(i,7,QTableWidgetItem(self.text_list[i]['placeHolder']))
					self.tableWidget_4.setItem(i,8,QTableWidgetItem(self.text_list[i]['textAlignment']))
					self.tableWidget_4.setItem(i,9,QTableWidgetItem(str(self.text_list[i]['constraints']['left']['percentage'])))
					self.tableWidget_4.setItem(i,10,QTableWidgetItem(str(self.text_list[i]['constraints']['left']['constant'])))
					self.tableWidget_4.setItem(i,11,QTableWidgetItem(str(self.text_list[i]['constraints']['right']['percentage'])))
					self.tableWidget_4.setItem(i,12,QTableWidgetItem(str(self.text_list[i]['constraints']['right']['constant'])))
					self.tableWidget_4.setItem(i,13,QTableWidgetItem(str(self.text_list[i]['constraints']['top']['percentage'])))
					self.tableWidget_4.setItem(i,14,QTableWidgetItem(str(self.text_list[i]['constraints']['top']['constant'])))
					self.tableWidget_4.setItem(i,15,QTableWidgetItem(self.text_list[i]['keyPath']))
					self.tableWidget_4.setItem(i,16,QTableWidgetItem(str(self.text_list[i]['contentSize'][0])))
					self.tableWidget_4.setItem(i,17,QTableWidgetItem(str(self.text_list[i]['contentSize'][1])))
					self.tableWidget_4.setItem(i,18,QTableWidgetItem(self.text_list[i]['animation']['name']))
					self.tableWidget_4.setItem(i,19,QTableWidgetItem(str(self.text_list[i]['animation']['type'])))
					self.tableWidget_4.setItem(i,20,QTableWidgetItem(self.text_list[i]['animation']['resourceDirectory']))
		else:
			self.tableWidget_4.setRowCount(self.spinBox_3.value())

		if self.cbox_2.isChecked() == True:
			self.tableWidget_5.setRowCount(1)
			for i in range(1):
				self.tableWidget_5.setItem(i,0,QTableWidgetItem(self.level_list[i]['id']))
				self.tableWidget_5.setItem(i,1,QTableWidgetItem(self.level_list[i]['type']))
				self.tableWidget_5.setItem(i,2,QTableWidgetItem(self.level_list[i]['contentMode']))
				self.tableWidget_5.setItem(i,3,QTableWidgetItem(str(self.level_list[i]['constraints']['right']['percentage'])))
				self.tableWidget_5.setItem(i,4,QTableWidgetItem(str(self.level_list[i]['constraints']['right']['constant'])))
				self.tableWidget_5.setItem(i,5,QTableWidgetItem(str(self.level_list[i]['constraints']['top']['percentage'])))
				self.tableWidget_5.setItem(i,6,QTableWidgetItem(str(self.level_list[i]['constraints']['top']['constant'])))
				self.tableWidget_5.setItem(i,7,QTableWidgetItem(str(self.level_list[i]['constraints']['height']['percentage'])))
				self.tableWidget_5.setItem(i,8,QTableWidgetItem(str(self.level_list[i]['constraints']['height']['constant'])))
				self.tableWidget_5.setItem(i,9,QTableWidgetItem(str(self.level_list[i]['constraints']['width']['percentage'])))
				self.tableWidget_5.setItem(i,10,QTableWidgetItem(str(self.level_list[i]['constraints']['width']['constant'])))
		else:
			self.tableWidget_5.setRowCount(0)

		if self.cbox_3.isChecked() == True:
			self.tableWidget_6.setRowCount(1)
			self.tableWidget_6.setItem(i,0,QTableWidgetItem(self.dic['animation']['name']))
			self.tableWidget_6.setItem(i,1,QTableWidgetItem(str(self.dic['animation']['type'])))
			self.tableWidget_6.setItem(i,2,QTableWidgetItem(self.dic['animation']['resourceDirectory']))
		else:
			self.tableWidget_6.setRowCount(0)


	#点击生成按钮的槽函数
	def createTable(self):
		self.nonEditable()
		self.initTable()
		count_1 = 0
		count_2 = self.spinBox_1.value()
		count_3 = self.spinBox_2.value()
		count_4 = self.spinBox_3.value()
		count_5 = 0
		count_6 = 0
		#设置table的行数
		self.tableWidget_2.setRowCount(count_1)
		self.tableWidget_3.setRowCount(count_2)
		if count_4 != 0:
			self.tableWidget_4.setRowCount(count_4)	
		#将comBox放到tablewidget中	
		self.initComBox()
		name = self.comBox_2.currentText()
		if self.cbox_1.isChecked() == True:
			count_1 = 1
			self.tableWidget_1.setRowCount(count_1)
			for i in range(count_1):
				self.tableWidget_1.setItem(i,0,QTableWidgetItem(str(i)))
				self.tableWidget_1.setItem(i,1,QTableWidgetItem("image"))
				self.tableWidget_1.setItem(i,3,QTableWidgetItem(str(i+1)))
				self.tableWidget_1.setItem(i,4,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,5,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,7,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,8,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,9,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,10,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,11,QTableWidgetItem("0"))
		if self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == False:
			for i in range(count_2):
				self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(count_1+i)))
				self.tableWidget_2.setItem(i,1,QTableWidgetItem("media"))
				self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(i)))
				self.tableWidget_2.setItem(i,4,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,8,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,10,QTableWidgetItem("0"))
		elif self.cbox_2.isChecked() == True and self.cbox_3.isChecked() == False:
			for i in range(count_2):
				self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(count_1+i)))
				self.tableWidget_2.setItem(i,2,QTableWidgetItem("media"))
				self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(i)))
				self.tableWidget_2.setItem(i,5,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,7,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,9,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,11,QTableWidgetItem("0"))
		elif self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == True:
			for i in range(count_2):
				self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(count_1+i)))
				self.tableWidget_2.setItem(i,1,QTableWidgetItem("media"))
				self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(i)))
				self.tableWidget_2.setItem(i,7,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,9,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,11,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,13,QTableWidgetItem("0"))
		else:
			QMessageBox.information(self, "提示", "不能多选")


		if self.cbox_3.isChecked() == False:
			for i in range(count_3):
				self.tableWidget_3.setItem(i,0,QTableWidgetItem(str(count_1+count_2+i)))
				self.tableWidget_3.setItem(i,1,QTableWidgetItem("image"))
				self.tableWidget_3.setItem(i,2,QTableWidgetItem("template_widget_"+name[self.count:]+".png"))
				self.tableWidget_3.setItem(i,3,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,4,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,5,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,7,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,8,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,9,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,10,QTableWidgetItem("0"))
		else:
			for i in range(count_3):
				self.tableWidget_3.setItem(i,0,QTableWidgetItem(str(count_1+count_2+i)))
				self.tableWidget_3.setItem(i,1,QTableWidgetItem("image"))
				self.tableWidget_3.setItem(i,2,QTableWidgetItem("template_widget_"+name[self.count:]+".png"))
				self.tableWidget_3.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,7,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,8,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,9,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,10,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,11,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,12,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,13,QTableWidgetItem("0"))
		if self.cbox_3.isChecked() == False:
			for i in range(count_4):
				self.tableWidget_4.setItem(i,0,QTableWidgetItem(str(count_1+count_2+count_3+i)))
				self.tableWidget_4.setItem(i,1,QTableWidgetItem("text"))
				self.tableWidget_4.setItem(i,2,QTableWidgetItem(str(i)))
				self.tableWidget_4.setItem(i,5,QTableWidgetItem("375"))
				self.tableWidget_4.setItem(i,10,QTableWidgetItem("0"))
				self.tableWidget_4.setItem(i,12,QTableWidgetItem("0"))
				self.tableWidget_4.setItem(i,14,QTableWidgetItem("0"))
		else:
			for i in range(count_4):
				self.tableWidget_4.setItem(i,0,QTableWidgetItem(str(count_1+count_2+count_3+i)))
				self.tableWidget_4.setItem(i,1,QTableWidgetItem("text"))
				self.tableWidget_4.setItem(i,2,QTableWidgetItem(str(i)))
				self.tableWidget_4.setItem(i,5,QTableWidgetItem("375"))
				self.tableWidget_4.setItem(i,10,QTableWidgetItem("0"))
				self.tableWidget_4.setItem(i,12,QTableWidgetItem("0"))
				self.tableWidget_4.setItem(i,14,QTableWidgetItem("0"))
				self.tableWidget_5.setItem(i,15,QTableWidgetItem("字 " + str(i+1)))
				self.tableWidget_5.setItem(i,18,QTableWidgetItem("data.json"))
				self.tableWidget_5.setItem(i,19,QTableWidgetItem("1"))
				self.tableWidget_5.setItem(i,20,QTableWidgetItem("/字" + str(i+1)))				
		if self.cbox_2.isChecked() == True:
			count_5 = 1
			self.tableWidget_5.setRowCount(count_5)
			for i in range(count_5):
				self.tableWidget_5.setItem(i,0,QTableWidgetItem(str(count_1+count_2+count_3+count_4+i)))
				self.tableWidget_2.setItem(i,1,QTableWidgetItem(str(count_1+count_2+count_3+count_4+i)))
				self.tableWidget_5.setItem(i,1,QTableWidgetItem("mediaIcon"))
				self.tableWidget_5.setItem(i,2,QTableWidgetItem("aspectFit"))
				self.tableWidget_5.setItem(i,3,QTableWidgetItem("0"))
				self.tableWidget_5.setItem(i,4,QTableWidgetItem("0"))
				self.tableWidget_5.setItem(i,5,QTableWidgetItem("0"))
				self.tableWidget_5.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_5.setItem(i,7,QTableWidgetItem("0"))
				self.tableWidget_5.setItem(i,8,QTableWidgetItem("0"))
				self.tableWidget_5.setItem(i,9,QTableWidgetItem("0"))
				self.tableWidget_5.setItem(i,10,QTableWidgetItem("0"))
		if self.cbox_3.isChecked() == True:
			count_6 = 1
			self.tableWidget_6.setRowCount(count_6)
			for in range(count_6):
				self.tableWidget_6.setItem(i,0,QTableWidgetItem("data.json"))
				self.tableWidget_6.setItem(i,1,QTableWidgetItem("1"))
				self.tableWidget_6.setItem(i,2,QTableWidgetItem("/"))

	def saveTable(self):
		self.nonEditable()
		if self.comBox_2.currentText() != "":
			if self.checkValues():
				if self.spinBox_1 != 0:
					self.tableValues()
					dic = {}
					temp = self.comBox_2.currentText()
					dic["templateId"] = int(temp[self.count:])
					dic["elements"] = []
					for i in range(len(self.item)):
						dic["elements"].append(self.item[i])
					name = self.comBox_2.currentText()
					path = self.path + "/" + name[self.count:] + "/" + name[:13]			
					with open(path, "w") as df:
						jsonStr = json.dumps(dic, sort_keys=True, indent=2)
						df.write(jsonStr)

					self.item = []
					QMessageBox.information(self, "提示", "保存成功！")
			else:
				QMessageBox.information(self,"提示",self.info)
		else:
			QMessageBox.information(self,"提示","请选择json文件！")

	def checkValues(self):
		if self.cbox_1.isChecked() == True:
			for i in range(1):
				if self.tableWidget_1.item(i,2) == None or self.tableWidget_1.item(i,2).text() == "":
					self.info = "blur表中第 "+str(i+1)+" 行第 3 列未填值！"
					return False

		if self.spinBox_1.value() != 0:
			for i in range(self.spinBox_1.value()):
				for j in range(self.tableWidget_2.columnCount()):
					if self.tableWidget_2.item(i,j) == None or self.tableWidget_2.item(i,j).text() == "":
						self.info = "cell表中第 "+str(i+1)+" 行第 "+str(j+1)+" 列未填值！"
						return False
			
		if self.spinBox_2.value() != 0:
			for i in range(self.spinBox_1.value()):
				for j in range(self.tableWidget_2.columnCount()):
					if self.tableWidget_3.item(i,j) == None or self.tableWidget_3.item(i,j).text() == "":
						self.info = "background表中第 "+str(i+1)+" 行第 "+str(j+1)+" 列未填值！"
						return False

		if self.spinBox_3.value() != 0:
			for i in range(self.spinBox_3.value()):
				for j in range(self.tableWidget_4.columnCount()-4):
					if self.tableWidget_4.item(i,j+4) == None or self.tableWidget_4.item(i,j+4).text() == "":
						self.info = "text表中第 "+str(i+1)+" 行第 "+str(j+1)+" 列未填值！"
						return False
				if self.tableWidget_4.cellWidget(i,3).currentText() == "":
					print("1")
					self.info = "text表中第 "+str(i+1)+" 行第 4 列未填值！"
					return False
	
		
		return True

	def tableValues(self):
		if self.cbox_1.isChecked() == True:
			for i in range(1):
				blur_dic = {}
				blur_dic["id"] = self.tableWidget_1.item(i, 0).text()
				blur_dic["type"] = self.tableWidget_1.item(i, 1).text()
				blur_dic["blur"] = int(self.tableWidget_1.item(i, 2).text())
				blur_dic["refId"] = self.tableWidget_1.item(i,3).text()
				item_1 = self.tableWidget_1.item(i,4).text()
				item_2 = self.tableWidget_1.item(i,5).text()
				item_3 = self.tableWidget_1.item(i,6).text()
				item_4 = self.tableWidget_1.item(i,7).text()
				item_5 = self.tableWidget_1.item(i,8).text()
				item_6 = self.tableWidget_1.item(i,9).text()
				item_7 = self.tableWidget_1.item(i,10).text()
				item_8 = self.tableWidget_1.item(i,11).text()
				blur_dic["constraints"] = {"left":{
															"percentage": float(item_1),
															"constant": float(item_2)
															},
													"right":{
															"percentage": float(item_3),
															"constant": float(item_4)
															},
													"top":{
															"percentage": float(item_5),
															"constant": float(item_6)
															},
													"bottom":{
															"percentage": float(item_7),
															"constant": float(item_8)
															}
													}
				self.item.append(blur_dic)

		if self.spinBox_1.value() != 0:
			if self.cbox_2.isChecked == False and self.cbox_3.isChecked() == False:
				for i in range(self.spinBox_1.value()):
					cell_dic = {}
					cell_dic["id"] = self.tableWidget_2.item(i, 0).text()
					cell_dic["type"] = self.tableWidget_2.item(i, 1).text()
					cell_dic["mediaId"] = self.tableWidget_2.item(i, 2).text()
					item_1 = self.tableWidget_2.item(i,3).text()
					item_2 = self.tableWidget_2.item(i,4).text()
					item_3 = self.tableWidget_2.item(i,5).text()
					item_4 = self.tableWidget_2.item(i,6).text()
					item_5 = self.tableWidget_2.item(i,7).text()
					item_6 = self.tableWidget_2.item(i,8).text()
					item_7 = self.tableWidget_2.item(i,9).text()
					item_8 = self.tableWidget_2.item(i,10).text()
					cell_dic["constraints"] = {"left":{
																"percentage": float(item_1),
																"constant": float(item_2)
																},
														"right":{
																"percentage": float(item_3),
																"constant": float(item_4)
																},
														"top":{
																"percentage": float(item_5),
																"constant": float(item_6)
																},
														"height":{
																"percentage": float(item_7),
																"constant": float(item_8)
																}
														}
					self.item.append(cell_dic)
			elif self.cbox_2.isChecked == True and self.cbox_3.isChecked() == False:
				for i in range(self.spinBox_1.value()):
					cell_dic = {}
					cell_dic["id"] = self.tableWidget_2.item(i, 0).text()
					cell_dic["customIconId"] = self.tableWidget_2.item(i,1).text()
					cell_dic["type"] = self.tableWidget_2.item(i, 2).text()
					cell_dic["mediaId"] = self.tableWidget_2.item(i, 3).text()
					item_1 = self.tableWidget_2.item(i,4).text()
					item_2 = self.tableWidget_2.item(i,5).text()
					item_3 = self.tableWidget_2.item(i,6).text()
					item_4 = self.tableWidget_2.item(i,7).text()
					item_5 = self.tableWidget_2.item(i,8).text()
					item_6 = self.tableWidget_2.item(i,9).text()
					item_7 = self.tableWidget_2.item(i,10).text()
					item_8 = self.tableWidget_2.item(i,11).text()
					cell_dic["constraints"] = {"left":{
																"percentage": float(item_1),
																"constant": float(item_2)
																},
														"right":{
																"percentage": float(item_3),
																"constant": float(item_4)
																},
														"top":{
																"percentage": float(item_5),
																"constant": float(item_6)
																},
														"height":{
																"percentage": float(item_7),
																"constant": float(item_8)
																}
														}
					self.item.append(cell_dic)
			elif self.cbox_2.isChecked == False and self.cbox_3.isChecked() == True:
				for i in range(self.spinBox_1.value()):
					cell_dic = {}
					cell_dic["id"] = self.tableWidget_2.item(i, 0).text()
					cell_dic["type"] = self.tableWidget_2.item(i, 1).text()
					cell_dic["mediaId"] = self.tableWidget_2.item(i, 2).text()
					cell_dic["keyPath"] = self.tableWidget_2.item(i,2).text()
					cell_dic["cen"]
					item_1 = self.tableWidget_2.item(i,3).text()
					item_2 = self.tableWidget_2.item(i,4).text()
					item_3 = self.tableWidget_2.item(i,5).text()
					item_4 = self.tableWidget_2.item(i,6).text()
					item_5 = self.tableWidget_2.item(i,7).text()
					item_6 = self.tableWidget_2.item(i,8).text()
					item_7 = self.tableWidget_2.item(i,9).text()
					item_8 = self.tableWidget_2.item(i,10).text()
					cell_dic["constraints"] = {"left":{
																"percentage": float(item_1),
																"constant": float(item_2)
																},
														"right":{
																"percentage": float(item_3),
																"constant": float(item_4)
																},
														"top":{
																"percentage": float(item_5),
																"constant": float(item_6)
																},
														"height":{
																"percentage": float(item_7),
																"constant": float(item_8)
																}
														}
					self.item.append(cell_dic)


		if self.spinBox_2.value() != 0:
			for i in range(self.spinBox_2.value()):
				bg_dic = {}
				bg_dic["id"] = self.tableWidget_3.item(i, 0).text()
				bg_dic["type"] = self.tableWidget_3.item(i, 1).text()
				bg_dic["imageName"] = self.tableWidget_3.item(i, 2).text()
				item_1 = self.tableWidget_3.item(i,3).text()
				item_2 = self.tableWidget_3.item(i,4).text()
				item_3 = self.tableWidget_3.item(i,5).text()
				item_4 = self.tableWidget_3.item(i,6).text()
				item_5 = self.tableWidget_3.item(i,7).text()
				item_6 = self.tableWidget_3.item(i,8).text()
				item_7 = self.tableWidget_3.item(i,9).text()
				item_8 = self.tableWidget_3.item(i,10).text()
				bg_dic["constraints"] = {"left":{
															"percentage": float(item_1),
															"constant": float(item_2)
															},
													"right":{
															"percentage": float(item_3),
															"constant": float(item_4)
															},
													"top":{
															"percentage": float(item_5),
															"constant": float(item_6)
															},
													"bottom":{
															"percentage": float(item_7),
															"constant": float(item_8)
															}
													}
				self.item.append(bg_dic)

		if self.spinBox_3.value() != 0:
			for i in range(self.spinBox_3.value()):
				text_dic = {}
				text_dic['id'] = self.tableWidget_4.item(i, 0).text()
				text_dic['type'] = self.tableWidget_4.item(i, 1).text()
				text_dic['textId'] = self.tableWidget_4.item(i, 2).text()
				text_dic['fontName'] = self.dict1[self.tableWidget_4.cellWidget(i, 3).currentText()]
				text_dic['fontSize'] = int(self.tableWidget_4.item(i, 4).text())
				text_dic['canvasWidth'] = int(self.tableWidget_4.item(i, 5).text())
				text_dic['textColor'] = self.tableWidget_4.item(i, 6).text()
				text_dic['placeHolder'] = self.tableWidget_4.item(i, 7).text()
				text_dic['textAlignment'] = self.tableWidget_4.item(i, 8).text()
				item_1 = self.tableWidget_4.item(i,9).text()
				item_2 = self.tableWidget_4.item(i,10).text()
				item_3 = self.tableWidget_4.item(i,11).text()
				item_4 = self.tableWidget_4.item(i,12).text()
				item_5 = self.tableWidget_4.item(i,13).text()
				item_6 = self.tableWidget_4.item(i,14).text()
				text_dic['constraints'] = {"left":{
												 "percentage": float(item_1),
												 "constant": float(item_2)
												 },
												 "right":{
												  "percentage": float(item_3),
												  "constant": float(item_4)
												  },
												  "top":{
												   "percentage": float(item_5),
												   "constant": float(item_6)
												  }
												 }
				self.item.append(text_dic)

		if self.cbox_2.isChecked() == True:
			for i in range(1):
				level_dic = {}
				level_dic["id"] = self.tableWidget_5.item(i, 0).text()
				level_dic["type"] = self.tableWidget_5.item(i, 1).text()
				level_dic["contentMode"] = self.tableWidget_5.item(i, 2).text()
				item_1 = self.tableWidget_5.item(i,3).text()
				item_2 = self.tableWidget_5.item(i,4).text()
				item_3 = self.tableWidget_5.item(i,5).text()
				item_4 = self.tableWidget_5.item(i,6).text()
				item_5 = self.tableWidget_5.item(i,7).text()
				item_6 = self.tableWidget_5.item(i,8).text()
				item_7 = self.tableWidget_5.item(i,9).text()
				item_8 = self.tableWidget_4.item(i,10).text()
				level_dic["constraints"] = {"right":{
															"percentage": float(item_1),
															"constant": float(item_2)
															},
													"top":{
															"percentage": float(item_3),
															"constant": float(item_4)
															},
													"height":{
															"percentage": float(item_5),
															"constant": float(item_6)
															},
													"width":{
															"percentage": float(item_7),
															"constant": float(item_8)
															}
													}
				self.item.append(level_dic)
			if self.spinBox_1.value() == 0:
				self.item[0]["customIconId"] = level_dic["id"]

	def encryption(self):
		if self.comBox_1.currentText() != "":
			pathIn = self.path
			pathOut = self.path[:-2] + "out"
			pathJar = "./resources/jar/encrypt.jar" 
			command = "java -jar " + pathJar + " " + pathIn + " " + pathOut
			os.system(command)
			QMessageBox.information(self,"提示","加密到out文件夹成功！")
		else:
			QMessageBox.information(self, "提示", "请选择素材组！")

	def compressing(self):
		self.encryption()
		pathOut = self.path[:-2] + "out"
		pathOrigin = self.path[:-2] + "origin"
		for root,dirs,files in os.walk(pathOut):
			for dir in dirs:
				pathNeed = pathOut + "/" + dir + "/"
				targetFile = pathOrigin + "/" + dir + ".7z"
				command = "7z a " + targetFile + " " + pathNeed
				os.system(command)
		QMessageBox.information(self, "提示", "已压缩到origin文件夹！")

	def openOrigin(self):
		if self.comBox_1.currentText() != "":
			pathOrigin ="file:///" + self.path[:-2] + "origin/"
			QDesktopServices.openUrl(QUrl(pathOrigin))
		else:
			QMessageBox.information(self, "提示", "请选择素材组！")





















		










        











