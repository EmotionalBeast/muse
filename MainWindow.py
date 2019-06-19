# -*- coding: utf-8 -*-
#author: Jhin Yao

import json, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
													QTableWidgetItem, QAbstractItemView, QComboBox)
from PyQt5.QtCore import Qt
from MainWindowUi import Ui_MainWindow
from OperateData import OperateJson
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
		
		with open("./font.json", 'r') as lf:
			jsonStr = lf.read()
			self.dict1 = json.loads(jsonStr, strict = False)
		#反转字典，赋值给新的字典
		self.dict2 = {v:k for k,v in self.dict1.items()}

	#将列表赋给comBox
	def templateList(self,text):
		self.list_3 = []
		with open("./setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		path = dic["directory"] + "/" + text + "/in"
		for root,dirs,files in os.walk(path):
			for file in files:
				if file == "template.json":
					name = file + "-" + root[-4:]
					self.list_3.append(name)
		self.comBox_2.addItems(self.list_3)
		self.comBox_2.setCurrentIndex(-1)

	def itemList(self):
		with open("./font.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr,strict = False)
			self.list_1 = dic.keys()
		return self.list_1

	def dirList(self):
		self.list_2 = []
		with open("./setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		path = dic["directory"]
		for root,dirs,files in os.walk(path):
			for dir in dirs:
				if root == path:
					self.list_2.append(dir)
		return self.list_2

	#打开关联的窗口
	def openFileWindow(self):
		self.myFileWindow = MyFileWindow()
		self.myFileWindow.setWindowModality(Qt.ApplicationModal)
		self.myFileWindow.show()

	def openPaintWindow(self):
		tup = self.getTableValue()
		self.myPaintWindow = MyPaintWindow(tup)
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
		self.statusbar.showMessage("Editable")

	def nonEditable(self):
		self.tableWidget_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.statusbar.showMessage("Non Editable")

	#工具栏图片功能的槽函数
	def openFile(self):
		self.cleanContents()
		fileName, fileType = QFileDialog.getOpenFileName(self,  
			"File System", './', "Text Files (*.json)")

		if len(fileName) == 0 :
			QMessageBox.information(self,"Tips","No file selected!")
		else:
			jsonFile = OperateJson(fileName)
			self.dic = jsonFile.loadJson()
			self.valuedTable(self.dic)
		self.nonEditable()

	def getItemText(self):
		dic = {}
		dic['templateId'] = int(self.lineEdit_1.text())
		dic['elements'] = []


		for i in range(self.tableWidget_2.rowCount()):
			if self.tableWidget_2.item(i,1) != None:
				cell_dic = {}
				cell_dic['id'] = self.tableWidget_2.item(i, 0).text()
				cell_dic['type'] = self.tableWidget_2.item(i, 1).text()
				cell_dic['mediaId'] = self.tableWidget_2.item(i, 2).text()
				item_1 = self.tableWidget_2.item(i,3).text()
				item_2 = self.tableWidget_2.item(i,4).text()
				item_3 = self.tableWidget_2.item(i,5).text()
				item_4 = self.tableWidget_2.item(i,6).text()
				item_5 = self.tableWidget_2.item(i,7).text()
				item_6 = self.tableWidget_2.item(i,8).text()
				item_7 = self.tableWidget_2.item(i,9).text()
				item_8 = self.tableWidget_2.item(i,10).text()
				cell_dic['constraints'] = {"left":{
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

				dic["elements"].append(cell_dic)

		for i in range(self.tableWidget_3.rowCount()):
			if self.tableWidget_3.item(i,1) != None:
				bg_dic = {}
				bg_dic['id'] = self.tableWidget_3.item(i, 0).text()
				bg_dic['type'] = self.tableWidget_3.item(i, 1).text()
				bg_dic['imageName'] = self.tableWidget_3.item(i, 2).text()
				item_1 = self.tableWidget_3.item(i,3).text()
				item_2 = self.tableWidget_3.item(i,4).text()
				item_3 = self.tableWidget_3.item(i,5).text()
				item_4 = self.tableWidget_3.item(i,6).text()
				item_5 = self.tableWidget_3.item(i,7).text()
				item_6 = self.tableWidget_3.item(i,8).text()
				item_7 = self.tableWidget_3.item(i,9).text()
				item_8 = self.tableWidget_3.item(i,10).text()
				bg_dic['constraints'] = {"left":{
												 "percentage": float(item_1),
												 "constant": float(item_2)
												 },
												 "right": {
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
				dic["elements"].append(bg_dic)

		for i in range(self.tableWidget_4.rowCount()):
			if self.tableWidget_4.item(i, 1) != None:
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
				dic["elements"].append(text_dic)
		 	
		return dic

	def cleanContents(self):
		self.tableWidget_1.clearContents()
		self.tableWidget_2.clearContents()
		self.tableWidget_3.clearContents()
		self.comBox_03.clearEditText()
		self.comBox_13.clearEditText()
		self.comBox_23.clearEditText()
		self.comBox_33.clearEditText()
		self.comBox_43.clearEditText()
		self.comBox_53.clearEditText()
		self.comBox_63.clearEditText()
		self.comBox_73.clearEditText()

		for i in range(self.tableWidget_4.columnCount()):
			if i != 3:
				for j in range(self.tableWidget_4.rowCount()):
					self.tableWidget_4.takeItem(j,i)
		
	#传参到paintWindow
	def getTableValue(self):
		cell_list = []
		text_list = []
		for i in range(self.tableWidget_2.columnCount()):
			if self.tableWidget_2.item(i,1) != None:
				cell_dic = {}
				for j in range(self.tableWidget_2.rowCount()-3):
					key = self.tableWidget_2.horizontalHeaderItem(j+3).text()
					value = self.tableWidget_2.item(i, j+3).text()
					cell_dic[key] = value
				cell_list.append(cell_dic)

		for i in range(self.tableWidget_4.columnCount()):
			if self.tableWidget_4.item(i, 1) != None:
				text_dic = {}
				for j in range(self.tableWidget_4.rowCount()-4):
					key = self.tableWidget_4.horizontalHeaderItem(j+4).text()
					value = self.tableWidget_4.item(i, j+4).text()
					text_dic[key] = value
				text_list.append(text_dic)

		return (cell_list, text_list)

	#读入json文件，显示在页面中
	def readJson(self):
		temp_1 = self.comBox_1.currentText()
		temp_2 = self.comBox_2.currentText()
		with open("./setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		path = dic["directory"] + "/" + temp_1 + "/in/" + temp_2[-4:] + "/template.json" 
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
		self.item_list = []
		self.dic = self.readJson()
		if self.dic == 0:
			self.spinBox_1.setValue(0)
			self.spinBox_2.setValue(0)
			self.spinBox_3.setValue(0)
			self.spinBox_4.setValue(0)
		else:
			item = self.dic["elements"]
			for i in range(len(item)):
				if item[i].has_key("refId"):
					self.blur_list.append(item[i])
				if item[i].has_key("mediaId"):
					self.cell_list.append(item[i])
				if item[i].has_key("imageName"):
					self.bg_list.append(item[i])
				if item[i].has_key("textId"):
					self.text_list.append(item[i])
				if item[i].has_key("contentMode"):
					self.rbtn_1.setChecked(True)
			self.spinBox_1.setValue(len(self.blur_list))
			self.spinBox_2.setValue(len(self.cell_list))
			self.spinBox_3.setValue(len(self.bg_list))
			self.spinBox_4.setValue(len(self.text_list))

	def initDate(self):
		self.resolveJson()
		if self.spinBox_1.value() != 0:
			self.tableWidget_1.setRowCount(self.spinBox_1.value())
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
			self.tableWidget_1.setRowCount(self.spinBox_1.value())

		if self.spinBox_2.value() != 0:
			self.tableWidget_2.setRowCount(self.spinBox_2.value())
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
			self.tableWidget_2.setRowCount(self.spinBox_2.value())

		if self.spinBox_3.value() != 0:
			self.tableWidget_3.setRowCount(self.spinBox_3.value())
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
			self.tableWidget_3.setRowCount(self.spinBox_3.value())

		if self.spinBox_4.value() != 0:
			self.tableWidget_4.setRowCount(self.spinBox_4.value())
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
			self.tableWidget_3.setRowCount(self.spinBox_3.value())

	#点击生成按钮的槽函数
	def createTable(self):
		if self.dic == 0 or self.spinBox_1.value() != len(self.blur_list) or self.spinBox_2 != len(self.cell_list) or self.spinBox_3 != len(self.bg_list) or self.spinBox_4 != len(self.text_list):
			count_1 = self.spinBox_1.value()
			count_2 = self.spinBox_2.value()
			count_3 = self.spinBox_3.value()
			count_4 = self.spinBox_4.value()
			#设置table的行数
			self.tableWidget_1.setRowCount(count_1)
			self.tableWidget_2.setRowCount(count_2)
			self.tableWidget_3.setRowCount(count_3)
			self.tableWidget_4.setRowCount(count_4)
			#将comBox放到tablewidget中
			self.tableWidget_4.setCellWidget(0, 3, self.comBox_03)
			self.tableWidget_4.setCellWidget(1, 3, self.comBox_13)
			self.tableWidget_4.setCellWidget(2, 3, self.comBox_23)
			self.tableWidget_4.setCellWidget(3, 3, self.comBox_33)
			self.tableWidget_4.setCellWidget(4, 3, self.comBox_43)
			self.tableWidget_4.setCellWidget(5, 3, self.comBox_53)
			self.tableWidget_4.setCellWidget(6, 3, self.comBox_63)
			self.tableWidget_4.setCellWidget(7, 3, self.comBox_73)
			name = self.comBox_2.currentText()
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
			for i in range(count_2):
				self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(count_1+i)))
				self.tableWidget_2.setItem(i,1,QTableWidgetItem("media"))
				self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(i)))
				self.tableWidget_2.setItem(i,4,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,8,QTableWidgetItem("0"))
				self.tableWidget_2.setItem(i,10,QTableWidgetItem("0"))
			for i in range(count_3):
				self.tableWidget_3.setItem(i,0,QTableWidgetItem(str(count_1+count_2+i)))
				self.tableWidget_3.setItem(i,1,QTableWidgetItem("image"))
				self.tableWidget_3.setItem(i,2,QTableWidgetItem("template_widget_"+name[-4:]+".png"))
				self.tableWidget_3.setItem(i,3,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,4,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,5,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,6,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,7,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,8,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,9,QTableWidgetItem("0"))
				self.tableWidget_3.setItem(i,10,QTableWidgetItem("0"))
			for i in range(count_4):
				self.tableWidget_4.setItem(i,0,QTableWidgetItem(str(count_1+count_2+count_3+i)))
				self.tableWidget_4.setItem(i,1,QTableWidgetItem("text"))
				self.tableWidget_4.setItem(i,2,QTableWidgetItem(str(i)))
				self.tableWidget_4.setItem(i,5,QTableWidgetItem("375"))
				self.tableWidget_4.setItem(i,10,QTableWidgetItem("0"))
				self.tableWidget_4.setItem(i,12,QTableWidgetItem("0"))
				self.tableWidget_4.setItem(i,14,QTableWidgetItem("0"))

	def saveTable(self):
		self.nonEditable()
		QMessageBox.information(self, "提示", "保存成功！")









		










        











