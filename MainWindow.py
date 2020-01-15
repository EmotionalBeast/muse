# -*- coding: utf-8 -*-
#author: Jhin Yao
"""
重要的是saveTable和resolveJson方法
"""

import json, os, sys, shutil
from PIL import Image
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
		self.index = 0

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
		if self.comBox_2.currentText() != "":
			self.myPaintWindow = MyPaintWindow(self.comBox_1.currentText(),self.comBox_2.currentText())
			self.myPaintWindow.setWindowModality(Qt.ApplicationModal)
			self.myPaintWindow.show()
		else:
			QMessageBox.information(self,"提示","请选择json文件!")
			
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
		if self.comBox_2.currentText() != "":
			if self.cbox_1.isChecked():
				self.tableWidget_1.setEditTriggers(QAbstractItemView.CurrentChanged)
			if self.spinBox_1.value() != 0:
				self.tableWidget_2.setEditTriggers(QAbstractItemView.CurrentChanged)
			if self.spinBox_2.value() != 0:
				self.tableWidget_3.setEditTriggers(QAbstractItemView.CurrentChanged)
			if self.spinBox_3.value() != 0:
				self.tableWidget_4.setEditTriggers(QAbstractItemView.CurrentChanged)
			if self.cbox_2.isChecked():
				self.tableWidget_5.setEditTriggers(QAbstractItemView.CurrentChanged)
			if self.cbox_3.isChecked():
				self.tableWidget_6.setEditTriggers(QAbstractItemView.CurrentChanged)
			self.statusbar.showMessage("Editable")
		else:
			QMessageBox.information(self, "提示", "请选择json文件")

	def nonEditable(self):
		if self.comBox_2.currentText() != "":
			if self.cbox_1.isChecked():
				self.tableWidget_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
			if self.spinBox_1.value() != 0:
				self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
			if self.spinBox_2.value() != 0:
				self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
			if self.spinBox_3.value() != 0:
				self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
			if self.cbox_2.isChecked():
				self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
			if self.cbox_3.isChecked():
				self.tableWidget_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
			self.statusbar.showMessage("Non Editable")
		else:
			QMessageBox.information(self, "提示", "请选择json文件")

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
		self.tabWidget.setGeometry(QtCore.QRect(0, 90, 1000, 550))
		self.tabWidget.setObjectName("tabWidget")
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
				

		#初始化动态模板的table
		if self.cbox_1.isChecked() == False and self.cbox_2.isChecked() == False and self.cbox_3.isChecked() == True:
			if self.spinBox_1.value() != 0:
				self.initDynamicCellTable()
				self.initNormalBgTable()
				self.initDynamicTable()
				if self.spinBox_3.value() != 0:
					self.initDynamicTextTable()
				

		#初始化图片有上下层次的动态模版
		if self.cbox_1.isChecked() == False and self.cbox_2.isChecked() == True and self.cbox_3.isChecked() == True:
			if self.spinBox_1.value() != 0:
				self.initDynamicCellTable()
				self.initNormalBgTable()
				self.initDynamicTable()
				self.initLevelTable()
				if self.spinBox_3.value() != 0:
					self.initDynamicTextTable()

		self.tabWidget.show()
		self.index +=1

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
		#赋值blur表
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
		#赋值cell表
		if self.spinBox_1.value() != 0:
			if self.cbox_3.isChecked() == False:
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
			else:
				self.tableWidget_2.setRowCount(self.spinBox_1.value())
				for i in range(len(self.cell_list)):
					self.tableWidget_2.setItem(i,0,QTableWidgetItem(self.cell_list[i]['id']))
					self.tableWidget_2.setItem(i,1,QTableWidgetItem(self.cell_list[i]['type']))
					self.tableWidget_2.setItem(i,2,QTableWidgetItem(self.cell_list[i]['imageId']))
					self.tableWidget_2.setItem(i,3,QTableWidgetItem(self.cell_list[i]['mediaId']))
					self.tableWidget_2.setItem(i,4,QTableWidgetItem(self.cell_list[i]['keyPath']))
					self.tableWidget_2.setItem(i,5,QTableWidgetItem(str(self.cell_list[i]['contentSize'][0])))
					self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(self.cell_list[i]['contentSize'][1])))
					self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['percentage'])))
					self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['constant'])))
					self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['percentage'])))
					self.tableWidget_2.setItem(i,10,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['constant'])))
					self.tableWidget_2.setItem(i,11,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['percentage'])))
					self.tableWidget_2.setItem(i,12,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['constant'])))
					self.tableWidget_2.setItem(i,13,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['percentage'])))
					self.tableWidget_2.setItem(i,14,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['constant'])))

		#赋值bg表
		if self.spinBox_2.value() != 0:
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
		#赋值text表
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

		#赋值level表
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

		#赋值animation表
		if self.cbox_3.isChecked() == True:
			self.tableWidget_6.setRowCount(1)
			for i in range(1):
				self.tableWidget_6.setItem(i,0,QTableWidgetItem(self.dic['animation']['name']))
				self.tableWidget_6.setItem(i,1,QTableWidgetItem(str(self.dic['animation']['type'])))
				self.tableWidget_6.setItem(i,2,QTableWidgetItem(self.dic['animation']['resourceDirectory']))

	#点击生成按钮的槽函数
	def createTable(self):
		self.initTable()
		self.nonEditable()
		count_1 = 0
		count_2 = self.spinBox_1.value()
		count_3 = self.spinBox_2.value()
		count_4 = self.spinBox_3.value()
		count_5 = 0
		count_6 = 0
		#设置table的行数
		self.tableWidget_2.setRowCount(count_2)
		self.tableWidget_3.setRowCount(count_3)
		if count_4 != 0:
			self.tableWidget_4.setRowCount(count_4)	
		#将comBox放到tablewidget中	
			self.initComBox()
		name = self.comBox_2.currentText()
		#初始化blur表
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
		#初始化cell表
		if  self.cbox_3.isChecked() == False:
			self.tableWidget_2.setRowCount(count_2)
			for i in range(count_2):
				self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(count_1+i)))
				self.tableWidget_2.setItem(i,1,QTableWidgetItem("media"))
				self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(i)))
				self.tableWidget_2.setItem(i,4,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,8,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,10,QTableWidgetItem("0"))			
		else:
			self.tableWidget_2.setRowCount(count_2)
			for i in range(count_2):
				self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(count_1+i)))
				self.tableWidget_2.setItem(i,1,QTableWidgetItem("media"))
				self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(i)))
				self.tableWidget_2.setItem(i,8,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,10,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,12,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,14,QTableWidgetItem("0"))
		#初始化bg表
		if count_3 != 0:
			self.tableWidget_3.setRowCount(count_3)
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

		#初始化text表
		if self.spinBox_3.value() != 0:
			if self.cbox_3.isChecked() == False:
				self.tableWidget_4.setRowCount(count_4)
				for i in range(count_4):
					self.tableWidget_4.setItem(i,0,QTableWidgetItem(str(count_1+count_2+count_3+i)))
					self.tableWidget_4.setItem(i,1,QTableWidgetItem("text"))
					self.tableWidget_4.setItem(i,2,QTableWidgetItem(str(i)))
					self.tableWidget_4.setItem(i,5,QTableWidgetItem("375"))
					self.tableWidget_4.setItem(i,10,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,12,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,14,QTableWidgetItem("0"))
			else:
				self.tableWidget_4.setRowCount(count_4)
				for i in range(count_4):
					self.tableWidget_4.setItem(i,0,QTableWidgetItem(str(count_1+count_2+count_3+i)))
					self.tableWidget_4.setItem(i,1,QTableWidgetItem("text"))
					self.tableWidget_4.setItem(i,2,QTableWidgetItem(str(i)))
					self.tableWidget_4.setItem(i,5,QTableWidgetItem("375"))
					self.tableWidget_4.setItem(i,10,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,12,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,14,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,15,QTableWidgetItem("text" + str(i+1)))
					self.tableWidget_4.setItem(i,18,QTableWidgetItem("data.json"))
					self.tableWidget_4.setItem(i,19,QTableWidgetItem("1"))
					self.tableWidget_4.setItem(i,20,QTableWidgetItem("/text" + str(i+1)))
		#初始化level表
		if self.cbox_2.isChecked() == True:
			count_5 = 1
			self.tableWidget_5.setRowCount(count_5)
			for i in range(count_5):
				self.tableWidget_5.setItem(i,0,QTableWidgetItem(str(count_1+count_2+count_3+count_4+i)))
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
		#初始化animotion表
		if self.cbox_3.isChecked() == True:
			count_6 = 1
			self.tableWidget_6.setRowCount(count_6)
			for i in range(count_6):
				self.tableWidget_6.setItem(i,0,QTableWidgetItem("data.json"))
				self.tableWidget_6.setItem(i,1,QTableWidgetItem("1"))
				self.tableWidget_6.setItem(i,2,QTableWidgetItem("/"))

	def saveTable(self):
		if self.comBox_2.currentText() != "":
			self.nonEditable()
			if self.checkValues():
				if self.spinBox_1 != 0:
					self.tableValues()
					dic = {} #开始封装Json数据
					temp = self.comBox_2.currentText()
					dic["templateId"] = int(temp[self.count:])
					dic["elements"] = []
					if self.cbox_3.isChecked():
						dic['animation'] = self.ani_dic
					for i in range(len(self.item)):
						dic["elements"].append(self.item[i])
					name = self.comBox_2.currentText()
					path = self.path + "/" + name[self.count:] + "/" + name[:13]			
					with open(path, "w") as df:
						jsonStr = json.dumps(dic, sort_keys=True, indent=2, ensure_ascii=False)
						df.write(jsonStr)
					self.item = []
					QMessageBox.information(self, "提示", "保存成功！")
			else:
				QMessageBox.information(self,"提示",self.info)
		else:
			QMessageBox.information(self,"提示","请选择json文件！")

		if self.cbox_3.isChecked() == True:
			self.convertFormat()
			QMessageBox.information(self, "提示", "jpg转化完成！")

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
			for i in range(self.spinBox_2.value()):
				for j in range(self.tableWidget_3.columnCount()):
					if self.tableWidget_3.item(i,j) == None or self.tableWidget_3.item(i,j).text() == "":
						self.info = "background表中第 " + str(i+1)+" 行第 "+str(j+1)+" 列未填值！"
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

		if self.cbox_2.isChecked() == True:
			for i in range(1):
				for j in range(self.tableWidget_5.columnCount()):
					if self.tableWidget_5.item(i,j) == None or self.tableWidget_5.item(i,j).text() == "":
						self.info = "level表中第 " + str(i+1) + " 行第 " + str(j+1) + " 列未填值！"
						return False

		if self.cbox_3.isChecked() == True:
			for i in range(1):
				for j in range(self.tableWidget_6.columnCount()):
					if self.tableWidget_6.item(i,j) == None or self.tableWidget_6.item(i,j).text() == "":
						self.info = "Dynamic表中第 " + str(i+1) + " 行第 " + str(j+1) + " 列未填值！"
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
			if self.cbox_3.isChecked() == False:
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
			else:
				for i in range(self.spinBox_1.value()):
					cell_dic = {}
					cell_dic["contentSize"] = []
					cell_dic["id"] = self.tableWidget_2.item(i, 0).text()
					cell_dic["type"] = self.tableWidget_2.item(i, 1).text()
					cell_dic["imageId"] = self.tableWidget_2.item(i, 2).text()
					cell_dic["mediaId"] = self.tableWidget_2.item(i, 3).text()
					cell_dic["keyPath"] = self.tableWidget_2.item(i,4).text()
					cell_dic["contentSize"].append(int(self.tableWidget_2.item(i,5).text()))
					cell_dic["contentSize"].append(int(self.tableWidget_2.item(i,6).text()))
					item_1 = self.tableWidget_2.item(i,7).text()
					item_2 = self.tableWidget_2.item(i,8).text()
					item_3 = self.tableWidget_2.item(i,9).text()
					item_4 = self.tableWidget_2.item(i,10).text()
					item_5 = self.tableWidget_2.item(i,11).text()
					item_6 = self.tableWidget_2.item(i,12).text()
					item_7 = self.tableWidget_2.item(i,13).text()
					item_8 = self.tableWidget_2.item(i,14).text()
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
			if self.cbox_3.isChecked() == False:
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

			else:
				for i in range(self.spinBox_3.value()):
					text_dic = {}
					text_dic['contentSize'] = []
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
					text_dic["keyPath"] = self.tableWidget_4.item(i,15).text()
					text_dic["contentSize"].append(int(self.tableWidget_4.item(i,16).text()))
					text_dic["contentSize"].append(int(self.tableWidget_4.item(i,17).text()))
					item_7 = self.tableWidget_4.item(i,18).text()
					item_8 = self.tableWidget_4.item(i,19).text()
					item_9 = self.tableWidget_4.item(i,20).text()
					text_dic['animation'] = {'name': item_7, 'type': int(item_8), 'resourceDirectory': item_9}
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
				item_8 = self.tableWidget_5.item(i,10).text()
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
			self.item[0]["customIconId"] = self.tableWidget_5.item(0,0).text()
			
		if self.cbox_3.isChecked() == True:
			for i in range(1):
				self.ani_dic = {}
				self.ani_dic['name'] = self.tableWidget_6.item(i,0).text()
				self.ani_dic['type'] = int(self.tableWidget_6.item(i,1).text())
				self.ani_dic['resourceDirectory'] = self.tableWidget_6.item(i,2).text()

	#加密压缩功能
	def encryption(self):
		pathIn = self.path
		pathOut = self.path[:-2] + "out"
		pathJar = "./resources/jar/encrypt.jar" 
		command = "java -jar " + pathJar + " " + pathIn + " " + pathOut
		os.system(command)
		QMessageBox.information(self,"提示","加密到out文件夹成功！")

	def compressing(self):
		pathOut = self.path[:-2] + "out"
		pathOrigin = self.path[:-2] + "origin"
		for root,dirs,files in os.walk(pathOut):
			for dir in dirs:
				if root == pathOut:
					pathNeed = pathOut + "/" + dir + "/"
					targetFile = pathOrigin + "/" + dir + ".7z"
					command = "7z a " + targetFile + " " + pathNeed
					os.system(command)
		QMessageBox.information(self, "提示", "已压缩到origin文件夹！")
		self.cleanFile(pathOut)
		os.mkdir(pathOut)

	def EnCom(self):
		if self.comBox_1.currentText() != "":
			self.encryption()
			self.compressing()
		else:
			QMessageBox.information(self, "提示", "请选择素材组！")

	def openOrigin(self):
		if self.comBox_1.currentText() != "":
			pathOrigin ="file:///" + self.path[:-2] + "origin/"
			QDesktopServices.openUrl(QUrl(pathOrigin))
		else:
			QMessageBox.information(self, "提示", "请选择素材组！")

	#转化指定图片的格式
	def convertFormat(self):
		imgPath = []
		img = []
		tempPath = self.comBox_2.currentText().rsplit("-",1)
		for i in range(self.spinBox_1.value()):
			tempStr = self.tableWidget_2.item(i, 2).text()
			img.append("img_" + tempStr[-1:] + ".png")

		for root,dirs,files in os.walk(self.path + "/" + tempPath[1]):
			for dir in dirs:
				if root[-5:-1] != 'text' and dir == "images":
					imgPath.append(root + "/" + dir)

		if len(imgPath) != 0:
			for path in imgPath:
				for root,dirs,files in os.walk(path):
					for file in files:
						if file[-3:] == "png" and (file in img):
							tempPathIn = root + "/" + file
							str1 = file.rsplit(".",1)
							tempPathOut = root + "/" + str1[0] + ".jpg"
							im = Image.open(tempPathIn)
							im = im.convert("RGB")
							im.save(tempPathOut)
							os.remove(tempPathIn)

	def createMV(self):
		pathMaterial = self.path[:-2] + "material"
		if os.path.exists(pathMaterial):			
			if self.comBox_1.currentText() != "":
				self.cleanFile(self.path)
				shutil.copytree(pathMaterial, self.path)
				generate = "./resources/jar/generate.jar"
				command = "java -jar " + generate + " -an " + self.path
				os.system(command)
				QMessageBox.information(self, "提示", "MV素材输出成功！")
				self.encryption()
				self.compressing()
			else:
				QMessageBox.information(self, "提示", "请选择MV素材组！")
		else:
			QMessageBox.information(self, "提示", "请选择MV素材组！")




	def cleanFile(self, path):
		files = os.listdir(path)
		for file in files:
			filepath = os.path.join(path, file)
			if os.path.isfile(filepath):
				os.remove(filepath)
			elif os.path.isdir(filepath):
				self.cleanFile(filepath)
			else:
				continue
		os.rmdir(path)


	def copyFile(self):
		pathMaterial = self.path[:-2] + "material"
		shutil.copytree(self.path, pathMaterial)











				
		



		


























		










        











