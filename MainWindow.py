# -*- coding: utf-8 -*-
#author: Jhin Yao
"""
重要的是saveTable和resolveJson方法
"""

import json, os, sys, shutil, subprocess
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
from pathlib import Path
from animation import AnimationData

FONT_JSON_PATH = os.path.join(os.getcwd(), "resources", "json", "font.json")
SETTING_JSON_PATH = os.path.join(os.getcwd(), "resources", "json", "setting.json")
ENCRYPT_JAR_PATH = os.path.join(os.getcwd(), "resources", "jar", "encrypt.jar")
GENERATE_JAR_PATH = os.path.join(os.getcwd(), "resources", "jar", "generate.jar")

class MyMainWindow(QMainWindow,Ui_MainWindow):
	#初始化
	def __init__(self):
		super(MyMainWindow,self).__init__()
		self.setupUi(self)
		self.myFileWindow = MyFileWindow()
		self.myDirWindow = MyDirWindow()
		self.index = 0

		with open(FONT_JSON_PATH, 'r') as lf:
			jsonStr = lf.read()
			self.dict1 = json.loads(jsonStr, strict = False)
		#反转字典，赋值给新的字典
		self.dict2 = {v:k for k,v in self.dict1.items()}


	#将列表赋给comBox
	def templateList(self,text):
		if self.comBox_2.count() != 0:
			self.comBox_2.clear()
		list_3 = []
		with open(SETTING_JSON_PATH, "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		self.path = os.path.join(Path(dic["directory"]), text, "in")

		for root,dirs,files in os.walk(self.path):
			for dir in dirs:
				if self.path == root:
					self.count = len(dir) * (-1)
			for file in files:
				if file == "template.json" or file == "template_1_1.json":
					name = file + "-" + root[self.count:]
					list_3.append(name)
					list_3.sort()

		self.comBox_2.addItems(list_3)
		self.comBox_2.setCurrentIndex(-1)

	def itemList(self):
		with open(FONT_JSON_PATH, "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr,strict = False)
			list_1 = list(dic.keys())
			list_1.sort()
		return list_1

	def dirList(self):
		list_2 = []
		with open(SETTING_JSON_PATH, "r") as lf:
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

	#读入json文件，显示在页面中
	def readJson(self):
		temp_1 = self.comBox_1.currentText()
		temp_2 = self.comBox_2.currentText()
		with open(SETTING_JSON_PATH, "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		if temp_2[:13] == "template.json":
			fileName = temp_2[:13]
		else:
			fileName = temp_2[:17] #template_1_1.json
		path = os.path.join(dic["directory"], temp_1, "in", temp_2[self.count:], fileName)
		with open(path, "r") as lf:
			size = os.path.getsize(path)
			if size != 0:
				jsonStr = lf.read()
				dic = json.loads(jsonStr, strict = False)
				return dic
			else:
				return 0

	def resolveJson(self):
		#reset
		self.blur_list = []
		self.cell_list = []
		self.bg_list = []
		self.text_list = []
		self.level_list = []
		self.item = []
		self.cbox_1.setChecked(False)
		self.cbox_2.setChecked(False)
		self.cbox_3.setChecked(False)
		self.cbox_4.setChecked(False)
		self.cbox_5.setChecked(False)
		self.cbox_6.setChecked(False)

		#value
		self.dic = self.readJson()
		if self.dic == 0:
			self.spinBox_1.setValue(0)
			self.spinBox_2.setValue(0)
			self.spinBox_3.setValue(0)
		else:
			if "animation" in self.dic.keys():
				self.cbox_3.setChecked(True)
			if "background" in self.dic.keys():
				self.cbox_4.setChecked(True)
				self.lineEdit_1.setText(self.dic["background"])
			item = self.dic["elements"]
			for i in range(len(item)):
				if "blur" in item[i].keys():
					self.blur_list.append(item[i])
					self.cbox_1.setChecked(True)
				if "mediaId" in item[i].keys():
					self.cell_list.append(item[i])
					if "ignore" in item[i].keys() and self.cbox_6.isChecked() == False:
    						self.cbox_6.setChecked(True)
				if "imageName" in item[i].keys():
					self.bg_list.append(item[i])
				if "textId" in item[i].keys():
					self.text_list.append(item[i])
					if item[i]["type"] == "animation_text" and self.cbox_5.isChecked() == False:
						self.cbox_5.setChecked(True)
				if "contentMode" in item[i].keys():
					self.level_list.append(item[i])
					self.cbox_2.setChecked(True)

			self.spinBox_1.setValue(len(self.cell_list))
			self.spinBox_2.setValue(len(self.bg_list))
			self.spinBox_3.setValue(len(self.text_list))
			self.spinBox_4.setValue(len(self.blur_list))

	def initData(self):
		self.handleData()
		self.resolveJson()
		self.initTable()
		#赋值blur表
		if self.cbox_1.isChecked() == True:
			self.tableWidget_1.setRowCount(self.spinBox_4.value())
			for i in range(len(self.blur_list)):
				self.tableWidget_1.setItem(i,7,QTableWidgetItem(self.blur_list[i]['id']))
				self.tableWidget_1.setItem(i,8,QTableWidgetItem(self.blur_list[i]['type']))
				self.tableWidget_1.setItem(i,4,QTableWidgetItem(str(self.blur_list[i]['blur'])))
				self.tableWidget_1.setItem(i,5,QTableWidgetItem(self.blur_list[i]['refId']))
				if "rotation" in self.blur_list[i].keys():
					self.tableWidget_1.setItem(i,6,QTableWidgetItem(str(self.blur_list[i]['rotation'])))
				else:
					self.tableWidget_1.setItem(i, 6, QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,0,QTableWidgetItem(str(self.blur_list[i]['constraints']['left']['percentage'])))
				self.tableWidget_1.setItem(i,9,QTableWidgetItem(str(self.blur_list[i]['constraints']['left']['constant'])))
				self.tableWidget_1.setItem(i,1,QTableWidgetItem(str(self.blur_list[i]['constraints']['right']['percentage'])))
				self.tableWidget_1.setItem(i,10,QTableWidgetItem(str(self.blur_list[i]['constraints']['right']['constant'])))
				self.tableWidget_1.setItem(i,2,QTableWidgetItem(str(self.blur_list[i]['constraints']['top']['percentage'])))
				self.tableWidget_1.setItem(i,11,QTableWidgetItem(str(self.blur_list[i]['constraints']['top']['constant'])))
				self.tableWidget_1.setItem(i,3,QTableWidgetItem(str(self.blur_list[i]['constraints']['bottom']['percentage'])))
				self.tableWidget_1.setItem(i,12,QTableWidgetItem(str(self.blur_list[i]['constraints']['bottom']['constant'])))
		#赋值cell表
		if self.spinBox_1.value() != 0:
			if self.cbox_3.isChecked() == False:
				self.tableWidget_2.setRowCount(self.spinBox_1.value())
				for i in range(len(self.cell_list)):
					self.tableWidget_2.setItem(i,7,QTableWidgetItem(self.cell_list[i]['id']))
					self.tableWidget_2.setItem(i,8,QTableWidgetItem(self.cell_list[i]['type']))
					self.tableWidget_2.setItem(i,9,QTableWidgetItem(self.cell_list[i]['mediaId']))
					self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(round(self.cell_list[i]['constraints']['left']['percentage']*100,2))))
					self.tableWidget_2.setItem(i,10,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['constant'])))
					self.tableWidget_2.setItem(i,1,QTableWidgetItem(str(round(self.cell_list[i]['constraints']['right']['percentage']*100, 2))))
					self.tableWidget_2.setItem(i,11,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['constant'])))
					self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(round(self.cell_list[i]['constraints']['top']['percentage']*100, 2))))
					self.tableWidget_2.setItem(i,12,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['constant'])))
					bottom = 1.0 - self.cell_list[i]['constraints']['top']['percentage'] - self.cell_list[i]['constraints']['height']['percentage']
					self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(round(bottom*100, 2))))
					self.tableWidget_2.setItem(i,13,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['constant'])))
					if "filter" in self.cell_list[i].keys():
						self.tableWidget_2.setItem(i,5,QTableWidgetItem(self.cell_list[i]['filter']))
					else:
						self.tableWidget_2.setItem(i,5,QTableWidgetItem("0"))
					if "filterStrength" in self.cell_list[i].keys():
						self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(self.cell_list[i]['filterStrength'])))
					else:
						self.tableWidget_2.setItem(i,6,QTableWidgetItem("0"))
					if "rotation" in self.cell_list[i].keys():
						self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(self.cell_list[i]['rotation'])))
					else:
						self.tableWidget_2.setItem(i, 4, QTableWidgetItem("0"))
			elif self.cbox_3.isChecked() == True and self.cbox_6.isChecked() == False: 
				self.tableWidget_2.setRowCount(self.spinBox_1.value())
				for i in range(len(self.cell_list)):
					self.tableWidget_2.setItem(i,8,QTableWidgetItem(self.cell_list[i]['id']))
					self.tableWidget_2.setItem(i,10,QTableWidgetItem(self.cell_list[i]['type']))
					self.tableWidget_2.setItem(i,4,QTableWidgetItem(self.cell_list[i]['imageId']))
					self.tableWidget_2.setItem(i,9,QTableWidgetItem(self.cell_list[i]['mediaId']))
					self.tableWidget_2.setItem(i,5,QTableWidgetItem(self.cell_list[i]['keyPath']))
					self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(self.cell_list[i]['contentSize'][0])))
					self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(self.cell_list[i]['contentSize'][1])))
					self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(round(self.cell_list[i]['constraints']['left']['percentage']*100,2))))
					self.tableWidget_2.setItem(i,11,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['constant'])))
					self.tableWidget_2.setItem(i,1,QTableWidgetItem(str(round(self.cell_list[i]['constraints']['right']['percentage']*100,2))))
					self.tableWidget_2.setItem(i,12,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['constant'])))
					self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(round(self.cell_list[i]['constraints']['top']['percentage']*100,2))))
					self.tableWidget_2.setItem(i,13,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['constant'])))
					bottom = 1.0 - self.cell_list[i]['constraints']['height']['percentage'] - self.cell_list[i]['constraints']['top']['percentage']
					self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(round(bottom*100, 2))))
					self.tableWidget_2.setItem(i,14,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['constant'])))
			elif self.cbox_3.isChecked() == True and self.cbox_6.isChecked() == True:
				self.tableWidget_2.setRowCount(self.spinBox_1.value())
				for i in range(len(self.cell_list)):
					if self.cell_list[i]['ignore'] == 0:
						self.tableWidget_2.setItem(i,8,QTableWidgetItem(self.cell_list[i]['id']))
						self.tableWidget_2.setItem(i,10,QTableWidgetItem(self.cell_list[i]['type']))
						self.tableWidget_2.setItem(i,4,QTableWidgetItem(self.cell_list[i]['imageId']))
						self.tableWidget_2.setItem(i,9,QTableWidgetItem(self.cell_list[i]['mediaId']))
						self.tableWidget_2.setItem(i,5,QTableWidgetItem(self.cell_list[i]['keyPath']))
						self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(self.cell_list[i]['contentSize'][0])))
						self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(self.cell_list[i]['contentSize'][1])))
						self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(round(self.cell_list[i]['constraints']['left']['percentage']*100,2))))
						self.tableWidget_2.setItem(i,11,QTableWidgetItem(str(self.cell_list[i]['constraints']['left']['constant'])))
						self.tableWidget_2.setItem(i,1,QTableWidgetItem(str(round(self.cell_list[i]['constraints']['right']['percentage']*100,2))))
						self.tableWidget_2.setItem(i,12,QTableWidgetItem(str(self.cell_list[i]['constraints']['right']['constant'])))
						self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(round(self.cell_list[i]['constraints']['top']['percentage']*100,2))))
						self.tableWidget_2.setItem(i,13,QTableWidgetItem(str(self.cell_list[i]['constraints']['top']['constant'])))
						bottom = 1.0 - self.cell_list[i]['constraints']['height']['percentage'] - self.cell_list[i]['constraints']['top']['percentage']
						self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(round(bottom*100,2))))
						self.tableWidget_2.setItem(i,14,QTableWidgetItem(str(self.cell_list[i]['constraints']['height']['constant'])))
						self.tableWidget_2.setItem(i,15,QTableWidgetItem(str(self.cell_list[i]['ignore'])))
    				

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
			if self.cbox_3.isChecked() == False and self.cbox_5.isChecked() == False:
				self.tableWidget_4.setRowCount(self.spinBox_3.value())
				self.initComBox()
				for i in range(len(self.text_list)):
					self.tableWidget_4.setItem(i,11,QTableWidgetItem(self.text_list[i]['id']))
					self.tableWidget_4.setItem(i,12,QTableWidgetItem(self.text_list[i]['type']))
					self.tableWidget_4.setItem(i,13,QTableWidgetItem(self.text_list[i]['textId']))
					if self.text_list[i]["fontName"] in self.dict2.keys():
						self.tableWidget_4.cellWidget(i,0).setCurrentText(self.dict2[self.text_list[i]["fontName"]])
					else:
						self.tableWidget_4.cellWidget(i, 0).setCurrentText(self.dict2["Perpetua"])
					self.tableWidget_4.setItem(i,3,QTableWidgetItem(str(self.text_list[i]['fontSize'])))
					if "canvasWidth" in self.text_list[i].keys():
						self.tableWidget_4.setItem(i,14,QTableWidgetItem(str(self.text_list[i]['canvasWidth'])))
					else:
						self.tableWidget_4.setItem(i,14,QTableWidgetItem("375"))
					self.tableWidget_4.setItem(i,2,QTableWidgetItem(self.text_list[i]['textColor']))
					self.tableWidget_4.setItem(i,6,QTableWidgetItem(self.text_list[i]['placeHolder']))
					if "textAlignment" in self.text_list[i].keys():
						self.tableWidget_4.cellWidget(i,1).setCurrentText(self.text_list[i]['textAlignment'])
					else:
						self.tableWidget_4.cellWidget(i,1).setCurrentText("center")
					self.tableWidget_4.setItem(i,7,QTableWidgetItem(str(round(self.text_list[i]['constraints']['left']['percentage']*100,2))))
					self.tableWidget_4.setItem(i,15,QTableWidgetItem(str(self.text_list[i]['constraints']['left']['constant'])))
					self.tableWidget_4.setItem(i,8,QTableWidgetItem(str(round(self.text_list[i]['constraints']['right']['percentage']*100,2))))
					self.tableWidget_4.setItem(i,16,QTableWidgetItem(str(self.text_list[i]['constraints']['right']['constant'])))
					top = self.text_list[i]['constraints']['top']['percentage'] + self.text_list[i]['fontSize']/24*0.007
					self.tableWidget_4.setItem(i,9,QTableWidgetItem(str(round(top*100,2))))
					self.tableWidget_4.setItem(i,17,QTableWidgetItem(str(self.text_list[i]['constraints']['top']['constant'])))
					if "textSpacing" in self.text_list[i].keys():
						self.tableWidget_4.setItem(i,4,QTableWidgetItem(str(self.text_list[i]['textSpacing'])))
					else:
						self.tableWidget_4.setItem(i,4,QTableWidgetItem("0"))
					if "lineSpacing" in self.text_list[i].keys():					
						self.tableWidget_4.setItem(i,5,QTableWidgetItem(str(self.text_list[i]['lineSpacing'])))
					else:
						self.tableWidget_4.setItem(i, 5, QTableWidgetItem("1"))
					if "angle" in self.text_list[i].keys():
						self.tableWidget_4.setItem(i,10,QTableWidgetItem(str(self.text_list[i]['angle'])))
					else:
						self.tableWidget_4.setItem(i, 10, QTableWidgetItem("0"))
			elif self.cbox_3.isChecked() == True and self.cbox_5.isChecked() == False:
				self.tableWidget_4.setRowCount(self.spinBox_3.value())
				self.initComBox()
				for i in range(len(self.text_list)):
					self.tableWidget_4.setItem(i,3,QTableWidgetItem(self.text_list[i]['id']))
					self.tableWidget_4.setItem(i,8,QTableWidgetItem(self.text_list[i]['type']))
					self.tableWidget_4.setItem(i,2,QTableWidgetItem(self.text_list[i]['textId']))
					self.tableWidget_4.cellWidget(i,0).setCurrentText(self.dict2[self.text_list[i]["fontName"]])
					self.tableWidget_4.setItem(i,4,QTableWidgetItem(str(self.text_list[i]['fontSize'])))
					self.tableWidget_4.setItem(i,5,QTableWidgetItem(str(self.text_list[i]['canvasWidth'])))
					self.tableWidget_4.setItem(i,6,QTableWidgetItem(self.text_list[i]['textColor']))
					self.tableWidget_4.setItem(i,7,QTableWidgetItem(self.text_list[i]['placeHolder']))
					self.tableWidget_4.cellWidget(i,1).setCurrentText(self.text_list[i]['textAlignment'])
					self.tableWidget_4.setItem(i,9,QTableWidgetItem(str(round(self.text_list[i]['constraints']['left']['percentage']*100,2))))
					self.tableWidget_4.setItem(i,10,QTableWidgetItem(str(self.text_list[i]['constraints']['left']['constant'])))
					self.tableWidget_4.setItem(i,11,QTableWidgetItem(str(round(self.text_list[i]['constraints']['right']['percentage']*100,2))))
					self.tableWidget_4.setItem(i,12,QTableWidgetItem(str(self.text_list[i]['constraints']['right']['constant'])))
					top  = self.text_list[i]['constraints']['top']['percentage'] + self.text_list[i]['fontSize']/24*0.007
					self.tableWidget_4.setItem(i,13,QTableWidgetItem(str(round(top*100,2))))
					self.tableWidget_4.setItem(i,14,QTableWidgetItem(str(self.text_list[i]['constraints']['top']['constant'])))
					self.tableWidget_4.setItem(i,15,QTableWidgetItem(self.text_list[i]['keyPath']))
					self.tableWidget_4.setItem(i,16,QTableWidgetItem(str(self.text_list[i]['contentSize'][0])))
					self.tableWidget_4.setItem(i,17,QTableWidgetItem(str(self.text_list[i]['contentSize'][1])))
					self.tableWidget_4.setItem(i,18,QTableWidgetItem(self.text_list[i]['animation']['name']))
					self.tableWidget_4.setItem(i,19,QTableWidgetItem(str(self.text_list[i]['animation']['type'])))
					self.tableWidget_4.setItem(i,20,QTableWidgetItem(self.text_list[i]['animation']['resourceDirectory']))
			elif self.cbox_3.isChecked() == True and self.cbox_5.isChecked() == True:
				self.tableWidget_4.setRowCount(self.spinBox_3.value())
				self.initComBox()
				for i in range(len(self.text_list)):
					self.tableWidget_4.setItem(i,12,QTableWidgetItem(self.text_list[i]['id']))
					self.tableWidget_4.setItem(i,14,QTableWidgetItem(self.text_list[i]['type']))
					self.tableWidget_4.setItem(i,13,QTableWidgetItem(self.text_list[i]['textId']))
					self.tableWidget_4.cellWidget(i,0).setCurrentText(self.dict2[self.text_list[i]["fontName"]])
					self.tableWidget_4.setItem(i,2,QTableWidgetItem(str(self.text_list[i]['fontSize'])))
					self.tableWidget_4.setItem(i,15,QTableWidgetItem(str(self.text_list[i]['canvasWidth'])))
					self.tableWidget_4.setItem(i,3,QTableWidgetItem(self.text_list[i]['textColor']))
					self.tableWidget_4.setItem(i,4,QTableWidgetItem(self.text_list[i]['placeHolder']))
					self.tableWidget_4.cellWidget(i,1).setCurrentText(self.text_list[i]['textAlignment'])
					self.tableWidget_4.setItem(i,5,QTableWidgetItem(str(round(self.text_list[i]['constraints']['left']['percentage']*100,2))))
					self.tableWidget_4.setItem(i,16,QTableWidgetItem(str(self.text_list[i]['constraints']['left']['constant'])))
					self.tableWidget_4.setItem(i,6,QTableWidgetItem(str(round(self.text_list[i]['constraints']['right']['percentage']*100,2))))
					self.tableWidget_4.setItem(i,17,QTableWidgetItem(str(self.text_list[i]['constraints']['right']['constant'])))
					top  = self.text_list[i]['constraints']['top']['percentage'] + self.text_list[i]['fontSize']/24*0.007
					self.tableWidget_4.setItem(i,7,QTableWidgetItem(str(round(top*100,2))))
					self.tableWidget_4.setItem(i,18,QTableWidgetItem(str(self.text_list[i]['constraints']['top']['constant'])))
					self.tableWidget_4.setItem(i,19,QTableWidgetItem(self.text_list[i]['sourcePath']))
					self.tableWidget_4.setItem(i,9,QTableWidgetItem(str(self.text_list[i]['textSpacing'])))
					self.tableWidget_4.setItem(i,10,QTableWidgetItem(str(self.text_list[i]['lineSpacing'])))
					self.tableWidget_4.setItem(i,11,QTableWidgetItem(str(self.text_list[i]['angle'])))
					self.tableWidget_4.setItem(i,8,QTableWidgetItem(str(self.text_list[i]['startFrame']))) 					

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

	def handleData(self):
		num = self.comBox_2.currentText().split("-")[1]
		path1 = os.path.join(self.path, num, "ignore.txt")
		path2 = os.path.join(self.path, num, "data.json")
		an = AnimationData(path1, path2)
		an.replaceNM()
		self.pictureName = an.getPictureName()
		self.NMDic = an.getJsonDic()
		self.contentSizeDic = an.getImageContentSize()

	#点击生成按钮的槽函数
	def createTable(self):
		self.initTable()
		self.nonEditable()
		count_1 = self.spinBox_4.value()
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
			self.tableWidget_1.setRowCount(count_1)
			for i in range(count_1):
				self.tableWidget_1.setItem(i,7,QTableWidgetItem(str(i)))
				self.tableWidget_1.setItem(i,8,QTableWidgetItem("image"))
				# self.tableWidget_1.setItem(i,5,QTableWidgetItem(str(count_1)))
				self.tableWidget_1.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,9,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,10,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,11,QTableWidgetItem("0"))
				self.tableWidget_1.setItem(i,12,QTableWidgetItem("0"))
		#初始化cell表
		if  self.cbox_3.isChecked() == False:
			self.tableWidget_2.setRowCount(count_2)
			for i in range(count_2):
				self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(count_1+i)))
				self.tableWidget_2.setItem(i,8,QTableWidgetItem("media"))
				self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(i)))
				self.tableWidget_2.setItem(i,10,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,11,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,12,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,13,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,5,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,4,QTableWidgetItem("0"))

		elif self.cbox_3.isChecked() == True and self.cbox_6.isChecked() == False:
			self.tableWidget_2.setRowCount(count_2)
			for i in range(count_2):
				self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(count_1+i)))
				self.tableWidget_2.setItem(i,10,QTableWidgetItem("media"))
				self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(i)))
				self.tableWidget_2.setItem(i,11,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,12,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,13,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,14,QTableWidgetItem("0"))
				if count_2 == len(self.pictureName):
					name = self.pictureName[i]
					refName = name.replace("_", "") + "a"
					self.tableWidget_2.setItem(i,4,QTableWidgetItem(name))   #图片名称
					self.tableWidget_2.setItem(i,5,QTableWidgetItem(refName))	#关联名称
					self.tableWidget_2.setItem(i,6,QTableWidgetItem(self.contentSizeDic[name][0]))	#图片高度
					self.tableWidget_2.setItem(i,7,QTableWidgetItem(self.contentSizeDic[name][1]))	#图片宽度
		elif self.cbox_3.isChecked() == True and self.cbox_6.isChecked() == True:
			self.tableWidget_2.setRowCount(count_2)
			for i in range(count_2):
				self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(count_1+i)))
				self.tableWidget_2.setItem(i,10,QTableWidgetItem("media"))
				self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(i)))
				self.tableWidget_2.setItem(i,11,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,12,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,13,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,14,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,15,QTableWidgetItem("0"))
				if count_2 == len(self.pictureName):
					name = self.pictureName[i]
					refName = name.replace("_", "") + "a"
					self.tableWidget_2.setItem(i,4,QTableWidgetItem(name))   #图片名称
					self.tableWidget_2.setItem(i,5,QTableWidgetItem(refName))	#关联名称
					self.tableWidget_2.setItem(i,6,QTableWidgetItem(self.contentSizeDic[name][0]))	#图片高度
					self.tableWidget_2.setItem(i,7,QTableWidgetItem(self.contentSizeDic[name][1]))	#图片宽度

		#初始化bg表
		if count_3 != 0:
			self.tableWidget_3.setRowCount(count_3)
			for i in range(count_3):
				self.tableWidget_3.setItem(i,0,QTableWidgetItem(str(count_1+count_2+i)))
				self.tableWidget_3.setItem(i,1,QTableWidgetItem("image"))
				if self.comBox_2.currentText()[:13] == "template.json":
					self.tableWidget_3.setItem(i,2,QTableWidgetItem("template_widget_"+name[self.count:]+".png"))
				else:
					self.tableWidget_3.setItem(i,2,QTableWidgetItem("template_widget_"+name[self.count:]+"_1_1.png"))
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
			if self.cbox_3.isChecked() == False and self.cbox_5.isChecked() == False:
				self.tableWidget_4.setRowCount(count_4)
				for i in range(count_4):
					self.tableWidget_4.setItem(i,11,QTableWidgetItem(str(count_1+count_2+count_3+i)))
					self.tableWidget_4.setItem(i,12,QTableWidgetItem("text"))
					self.tableWidget_4.setItem(i,13,QTableWidgetItem(str(i)))
					self.tableWidget_4.setItem(i,14,QTableWidgetItem("375"))
					self.tableWidget_4.setItem(i,15,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,16,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,17,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,4,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,5,QTableWidgetItem("1"))
					self.tableWidget_4.setItem(i,10,QTableWidgetItem("0"))

			elif self.cbox_3.isChecked() == True and self.cbox_5.isChecked() == False:
				self.tableWidget_4.setRowCount(count_4)
				for i in range(count_4):
					self.tableWidget_4.setItem(i,3,QTableWidgetItem(str(count_1+count_2+count_3+i)))
					self.tableWidget_4.setItem(i,8,QTableWidgetItem("text"))
					self.tableWidget_4.setItem(i,2,QTableWidgetItem(str(i)))
					self.tableWidget_4.setItem(i,5,QTableWidgetItem("375"))
					self.tableWidget_4.setItem(i,10,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,12,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,14,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,15,QTableWidgetItem("text" + str(i+1)))
					self.tableWidget_4.setItem(i,18,QTableWidgetItem("data.json"))
					self.tableWidget_4.setItem(i,19,QTableWidgetItem("1"))
					self.tableWidget_4.setItem(i,20,QTableWidgetItem("/text" + str(i+1)))
			elif self.cbox_3.isChecked() == True and self.cbox_5.isChecked() == True:
				self.tableWidget_4.setRowCount(count_4)
				for i in range(count_4):
					self.tableWidget_4.setItem(i,12,QTableWidgetItem(str(count_1+count_2+count_3+i)))
					self.tableWidget_4.setItem(i,14,QTableWidgetItem("animation_text"))
					self.tableWidget_4.setItem(i,13,QTableWidgetItem(str(i)))
					self.tableWidget_4.setItem(i,15,QTableWidgetItem("375"))
					self.tableWidget_4.setItem(i,16,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,17,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,18,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,19,QTableWidgetItem("text" + str(i+1) + "/data.json"))
					self.tableWidget_4.setItem(i,9,QTableWidgetItem("0"))
					self.tableWidget_4.setItem(i,10,QTableWidgetItem("1"))
					self.tableWidget_4.setItem(i,11,QTableWidgetItem("0"))

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
					dic["version"] = "1.1"
					dic["elements"] = []
					if self.cbox_4.isChecked():
						dic["background"] = self.lineEdit_1.text()
					if self.cbox_3.isChecked():
						dic['animation'] = self.ani_dic
					for i in range(len(self.item)):
						dic["elements"].append(self.item[i])
					name = self.comBox_2.currentText()
					if name[:13] == "template.json":
						path = os.path.join(self.path, name[self.count:], name[:13])
					else:
						path = os.path.join(self.path, name[self.count:], name[:17])	
					with open(path, "w") as df:
						jsonStr = json.dumps(dic, sort_keys=True, indent=2, ensure_ascii=False)
						df.write(jsonStr)
					self.item = []
					QMessageBox.information(self, "提示", "保存成功！")
			else:
				QMessageBox.information(self,"提示",self.info)
		else:
			QMessageBox.information(self,"提示","请选择json文件！")

		# if self.cbox_3.isChecked() == True:
		# 	self.convertFormat()
		# 	QMessageBox.information(self, "提示", "jpg转化完成！")

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
				for j in range(self.tableWidget_4.columnCount()-2):
					if self.tableWidget_4.item(i,j+2) == None or self.tableWidget_4.item(i,j+2).text() == "":
						self.info = "text表中第 "+str(i+1)+" 行第 "+str(j+1)+" 列未填值！"
						return False
				if self.tableWidget_4.cellWidget(i,0).currentText() == "":
					print("1")
					self.info = "text表中第 "+str(i+1)+" 行第 1 列未填值！"
					return False
				if self.tableWidget_4.cellWidget(i,1).currentText() == "":
					print("1")
					self.info = "text表中第 "+str(i+1)+" 行第 2 列未填值！"
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
			for i in range(self.spinBox_4.value()):
				blur_dic = {}
				blur_dic["id"] = self.tableWidget_1.item(i, 7).text()
				blur_dic["type"] = self.tableWidget_1.item(i, 8).text()
				blur_dic["blur"] = int(self.tableWidget_1.item(i, 4).text())
				blur_dic["refId"] = self.tableWidget_1.item(i,5).text()
				if self.tableWidget_1.item(i, 8).text() != "clone_image":
					blur_dic["rotation"] = float(self.tableWidget_1.item(i, 6).text())
				item_1 = self.tableWidget_1.item(i,0).text()
				item_2 = self.tableWidget_1.item(i,9).text()
				item_3 = self.tableWidget_1.item(i,1).text()
				item_4 = self.tableWidget_1.item(i,10).text()
				item_5 = self.tableWidget_1.item(i,2).text()
				item_6 = self.tableWidget_1.item(i,11).text()
				item_7 = self.tableWidget_1.item(i,3).text()
				item_8 = self.tableWidget_1.item(i,12).text()
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
					cell_dic["id"] = self.tableWidget_2.item(i, 7).text()
					cell_dic["type"] = self.tableWidget_2.item(i, 8).text()
					cell_dic["mediaId"] = self.tableWidget_2.item(i, 9).text()
					if self.tableWidget_2.item(i, 5).text() != "0":
						cell_dic["filter"] = self.tableWidget_2.item(i, 5).text()
						cell_dic["filterStrength"] = float(self.tableWidget_2.item(i, 6).text())
					cell_dic["rotation"] = float(self.tableWidget_2.item(i, 4).text())
					item_1 = self.tableWidget_2.item(i,0).text()
					item_2 = self.tableWidget_2.item(i,10).text()
					item_3 = self.tableWidget_2.item(i,1).text()
					item_4 = self.tableWidget_2.item(i,11).text()
					item_5 = self.tableWidget_2.item(i,2).text()
					item_6 = self.tableWidget_2.item(i,12).text()
					item_7 = 100-float(self.tableWidget_2.item(i,3).text())-float(item_5)
					item_8 = self.tableWidget_2.item(i,13).text()
					cell_dic["constraints"] = {"left":{
																"percentage": round(float(item_1)/100, 4),
																"constant": float(item_2)
																},
														"right":{
																"percentage": round(float(item_3)/100, 4),
																"constant": float(item_4)
																},
														"top":{
																"percentage": round(float(item_5)/100, 4),
																"constant": float(item_6)
																},
														"height":{
																"percentage": round(item_7/100, 4),
																"constant": float(item_8)
																}
														}
					self.item.append(cell_dic)

			elif self.cbox_3.isChecked() == True and self.cbox_6.isChecked() == False:
				for i in range(self.spinBox_1.value()):
					cell_dic = {}
					cell_dic["contentSize"] = []
					cell_dic["id"] = self.tableWidget_2.item(i, 8).text()
					cell_dic["type"] = self.tableWidget_2.item(i, 10).text()
					cell_dic["imageId"] = self.tableWidget_2.item(i, 4).text()
					cell_dic["mediaId"] = self.tableWidget_2.item(i, 9).text()
					cell_dic["keyPath"] = self.tableWidget_2.item(i,5).text()
					cell_dic["contentSize"].append(int(self.tableWidget_2.item(i,6).text()))
					cell_dic["contentSize"].append(int(self.tableWidget_2.item(i,7).text()))
					item_1 = self.tableWidget_2.item(i,0).text()
					item_2 = self.tableWidget_2.item(i,11).text()
					item_3 = self.tableWidget_2.item(i,1).text()
					item_4 = self.tableWidget_2.item(i,12).text()
					item_5 = self.tableWidget_2.item(i,2).text()
					item_6 = self.tableWidget_2.item(i,13).text()
					item_7 = 100 - float(self.tableWidget_2.item(i,3).text()) - float(item_5)
					item_8 = self.tableWidget_2.item(i,14).text()
					cell_dic["constraints"] = {"left":{
																"percentage": round(float(item_1)/100, 4),
																"constant": float(item_2)
																},
														"right":{
																"percentage": round(float(item_3)/100, 4),
																"constant": float(item_4)
																},
														"top":{
																"percentage": round(float(item_5)/100, 4),
																"constant": float(item_6)
																},
														"height":{
																"percentage": round(float(item_7)/100, 4),
																"constant": float(item_8)
																}
														}
					self.item.append(cell_dic)
			
			elif self.cbox_3.isChecked() == True and self.cbox_6.isChecked() == True:
				for i in range(self.spinBox_1.value()):
					cell_dic = {}
					cell_dic["contentSize"] = []
					cell_dic["id"] = self.tableWidget_2.item(i, 8).text()
					cell_dic["type"] = self.tableWidget_2.item(i, 10).text()
					cell_dic["imageId"] = self.tableWidget_2.item(i, 4).text()
					cell_dic["mediaId"] = self.tableWidget_2.item(i, 9).text()
					cell_dic["keyPath"] = self.tableWidget_2.item(i,5).text()
					cell_dic["contentSize"].append(int(self.tableWidget_2.item(i,6).text()))
					cell_dic["contentSize"].append(int(self.tableWidget_2.item(i,7).text()))
					item_1 = self.tableWidget_2.item(i,0).text()
					item_2 = self.tableWidget_2.item(i,11).text()
					item_3 = self.tableWidget_2.item(i,1).text()
					item_4 = self.tableWidget_2.item(i,12).text()
					item_5 = self.tableWidget_2.item(i,2).text()
					item_6 = self.tableWidget_2.item(i,13).text()
					item_7 = 100 - float(self.tableWidget_2.item(i,3).text()) - float(item_5)
					item_8 = self.tableWidget_2.item(i,14).text()
					cell_dic["constraints"] = {"left":{
																"percentage": round(float(item_1)/100, 4),
																"constant": float(item_2)
																},
														"right":{
																"percentage": round(float(item_3)/100,4),
																"constant": float(item_4)
																},
														"top":{
																"percentage": round(float(item_5)/100,4),
																"constant": float(item_6)
																},
														"height":{
																"percentage": round(float(item_7)/100,4),
																"constant": float(item_8)
																}
														}
					cell_dic["ignore"] = int(self.tableWidget_2.item(i, 15).text())
					self.item.append(cell_dic)
					for name in self.NMDic[cell_dic["imageid"]]:
						if name != cell_dic["keyPath"]:
							cell_dic["keyPath"] = name
							cell_dic["ignore"] = 1
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
					text_dic['id'] = self.tableWidget_4.item(i, 11).text()
					text_dic['type'] = self.tableWidget_4.item(i, 12).text()
					text_dic['textId'] = self.tableWidget_4.item(i, 13).text()
					text_dic['fontName'] = self.dict1[self.tableWidget_4.cellWidget(i, 0).currentText()]
					fontSize = float(self.tableWidget_4.item(i, 3).text())
					text_dic['fontSize'] = fontSize
					text_dic['canvasWidth'] = int(self.tableWidget_4.item(i, 14).text())
					text_dic['textColor'] = self.tableWidget_4.item(i, 2).text()
					text_dic['placeHolder'] = self.tableWidget_4.item(i, 6).text()
					text_dic['textAlignment'] = self.tableWidget_4.cellWidget(i, 1).currentText()
					text_dic['textSpacing'] = float(self.tableWidget_4.item(i, 4).text())
					text_dic['lineSpacing'] = float(self.tableWidget_4.item(i, 5).text())
					text_dic['angle'] = float(self.tableWidget_4.item(i, 10).text())
					item_1 = self.tableWidget_4.item(i,7).text()
					item_2 = self.tableWidget_4.item(i,15).text()
					item_3 = self.tableWidget_4.item(i,8).text()
					item_4 = self.tableWidget_4.item(i,16).text()
					item_5 = self.tableWidget_4.item(i,9).text()
					item_6 = self.tableWidget_4.item(i,17).text()
					text_dic['constraints'] = {"left":{
													 "percentage": round(float(item_1)/100,4),
													 "constant": float(item_2)
													 },
													 "right":{
													  "percentage": round(float(item_3)/100,4),
													  "constant": float(item_4)
													  },
													  "top":{
													   "percentage": round(float(item_5)/100 - fontSize/24*0.007,4),
													   "constant": float(item_6)
													  }
													 }
					self.item.append(text_dic)

			elif self.cbox_3.isChecked() == True and self.cbox_5.isChecked() == False:
				for i in range(self.spinBox_3.value()):
					text_dic = {}
					text_dic['contentSize'] = []
					text_dic['id'] = self.tableWidget_4.item(i, 3).text()
					text_dic['type'] = self.tableWidget_4.item(i, 8).text()
					text_dic['textId'] = self.tableWidget_4.item(i, 2).text()
					text_dic['fontName'] = self.dict1[self.tableWidget_4.cellWidget(i, 0).currentText()]
					fontSize = float(self.tableWidget_4.item(i, 4).text())
					text_dic['fontSize'] = fontSize
					text_dic['canvasWidth'] = int(self.tableWidget_4.item(i, 5).text())
					text_dic['textColor'] = self.tableWidget_4.item(i, 6).text()
					text_dic['placeHolder'] = self.tableWidget_4.item(i, 7).text()
					text_dic['textAlignment'] = self.tableWidget_4.cellWidget(i, 1).currentText()
					item_1 = self.tableWidget_4.item(i,9).text()
					item_2 = self.tableWidget_4.item(i,10).text()
					item_3 = self.tableWidget_4.item(i,11).text()
					item_4 = self.tableWidget_4.item(i,12).text()
					item_5 = self.tableWidget_4.item(i,13).text()
					item_6 = self.tableWidget_4.item(i,14).text()
					text_dic['constraints'] = {"left":{
													 "percentage": round(float(item_1)/100,4),
													 "constant": float(item_2)
													 },
													 "right":{
													  "percentage": round(float(item_3)/100,4),
													  "constant": float(item_4)
													  },
													  "top":{
													   "percentage": round(float(item_5)/100 - fontSize/24*0.007,4),
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
			
			elif self.cbox_3.isChecked() == True and self.cbox_5.isChecked() == True:
				for i in range(self.spinBox_3.value()):
					text_dic = {}
					text_dic['id'] = self.tableWidget_4.item(i, 12).text()
					text_dic['type'] = self.tableWidget_4.item(i, 14).text()
					text_dic['textId'] = self.tableWidget_4.item(i, 13).text()
					text_dic['fontName'] = self.dict1[self.tableWidget_4.cellWidget(i, 0).currentText()]
					fontSize = float(self.tableWidget_4.item(i, 2).text())
					text_dic['fontSize'] = fontSize
					text_dic['canvasWidth'] = int(self.tableWidget_4.item(i, 15).text())
					text_dic['textColor'] = self.tableWidget_4.item(i, 3).text()
					text_dic['placeHolder'] = self.tableWidget_4.item(i, 4).text()
					text_dic['textAlignment'] = self.tableWidget_4.cellWidget(i, 1).currentText()
					item_1 = self.tableWidget_4.item(i,5).text()
					item_2 = self.tableWidget_4.item(i,16).text()
					item_3 = self.tableWidget_4.item(i,6).text()
					item_4 = self.tableWidget_4.item(i,17).text()
					item_5 = self.tableWidget_4.item(i,7).text()
					item_6 = self.tableWidget_4.item(i,18).text()
					text_dic['constraints'] = {"left":{
													 "percentage": round(float(item_1)/100,4),
													 "constant": float(item_2)
													 },
													 "right":{
													  "percentage": round(float(item_3)/100,4),
													  "constant": float(item_4)
													  },
													  "top":{
													   "percentage": round(float(item_5)/100 - fontSize/24*0.007,4),
													   "constant": float(item_6)
													  }
													 }
					text_dic["sourcePath"] = self.tableWidget_4.item(i,19).text()
					text_dic["textSpacing"] = float(self.tableWidget_4.item(i,9).text())
					text_dic["lineSpacing"]= float(self.tableWidget_4.item(i,10).text())
					text_dic["angle"] = float(self.tableWidget_4.item(i,11).text())
					text_dic["startFrame"] = float(self.tableWidget_4.item(i,8).text())
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
		pathJar = ENCRYPT_JAR_PATH
		command = "java -jar " + pathJar + " " + pathIn + " " + pathOut
		info = subprocess.check_call(command, shell=True)
		if info == 0:
			QMessageBox.information(self,"提示","加密到out文件夹成功！")
		else:
			QMessageBox.information(self,"提示",info)

	def compressing(self):
		pathOut = self.path[:-2] + "out"
		pathOrigin = self.path[:-2] + "origin"
		for root,dirs,files in os.walk(pathOut):
			for dir in dirs:
				if root == pathOut:
					pathNeed = os.path.join(pathOut, dir)
					tmp = dir + ".7z"
					targetFile = os.path.join(pathOrigin, tmp)
					print("pathNeed:", pathNeed)
					print("targetFile:", targetFile)
					command = "7z a " + targetFile + " " + pathNeed
					subprocess.call(command, shell=True)
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
			pathOrigin ="file:///" + self.path[:-2] + "origin"
			QDesktopServices.openUrl(QUrl(pathOrigin))
		else:
			QMessageBox.information(self, "提示", "请选择素材组！")

	#转化指定图片的格式
	def convertFormat(self):
		imgPath = []
		img = []
		tempPath = self.comBox_2.currentText().rsplit("-",1)
		for i in range(self.spinBox_1.value()):
			tempStr = self.tableWidget_2.item(i, 4).text()
			img.append("img_" + tempStr[-1:] + ".png")

		for root,dirs,files in os.walk(os.path.join(self.path, tempPath[1])):
			for dir in dirs:
				if root[-5:-1] != 'text' and dir == "images":
					imgPath.append(os.path.join(root, dir))

		if len(imgPath) != 0:
			for path in imgPath:
				for root,dirs,files in os.walk(path):
					for file in files:
						if file[-3:] == "png" and (file in img):
							tempPathIn = os.path.join(root, file)
							str1 = file.rsplit(".",1)
							str2 = str1[0] + ".jpg"
							tempPathOut = os.path.join(root, str2)
							im = Image.open(tempPathIn)
							im = im.convert("RGB")
							im.save(tempPathOut)
							os.remove(tempPathIn)

	def createChicMV(self):
		pathMaterial = self.path[:-2] + "material"
		if os.path.exists(pathMaterial):			
			if self.comBox_1.currentText() != "":
				self.cleanFile(self.path)
				shutil.copytree(pathMaterial, self.path)
				generate =os.path.join(os.getcwd(),"resources", "jar", "generate.jar")
				command = "java -jar " + generate + " -an " + self.path
				info = subprocess.check_call(command, shell=True)
				if info == 0:
					QMessageBox.information(self, "提示", "MV素材输出成功！")
				else:
					QMessageBox.information(self, "提示", info)
				self.encryption()
				self.compressing()
			else:
				QMessageBox.information(self, "提示", "请选择MV素材组！")
		else:
			QMessageBox.information(self, "提示", "请选择MV素材组！")
	
	def createBeatMV(self):
		# pathMaterial = self.path[:-2] + "material"
		# if os.path.exists(pathMaterial):
		# 	if self.comBox_1.currentText() != "":
		# 		self.cleanFile(self.path)
		# 		shutil.copytree(pathMaterial, self.path)
		# 		generate = os.path.join(os.getcwd(),"resources", "jar", "generate.jar")
		# 		command = "java -jar " + generate + " -an -vex " + self.path
		# 		info = subprocess.check_call(command, shell=True)
		# 		if info == 0:
		# 			QMessageBox.information(self, "提示", "MV素材输出成功！")
		# 		else:
		# 			QMessageBox.information(self, "提示", info)
		# 		self.encryption()
		# 		self.compressing()
		# 	else:
		# 		QMessageBox.information(self, "提示", "请选择BeatMV素材组！")
		# else:
		# 	QMessageBox.information(self, "提示", "请选择BeatMV素材")
		pass 

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
	
	def moveTableRow(self):
		pass













				
		



		


























		










        











