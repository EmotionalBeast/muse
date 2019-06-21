# -*- coding: utf-8 -*-
#author: Jhin Yao

import json, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
													QTableWidgetItem, QAbstractItemView, QComboBox)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
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
		
		with open("./font.json", 'r') as lf:
			jsonStr = lf.read()
			self.dict1 = json.loads(jsonStr, strict = False)
		#反转字典，赋值给新的字典
		self.dict2 = {v:k for k,v in self.dict1.items()}


	#将列表赋给comBox
	def templateList(self,text):
		if self.comBox_2.count() != 0:
			self.comBox_2.clear()
		list_3 = []
		with open("./setting.json", "r") as lf:
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
		with open("./font.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr,strict = False)
			list_1 = dic.keys()
		return list_1

	def dirList(self):
		list_2 = []
		with open("./setting.json", "r") as lf:
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
		self.tableWidget_5.setEditTriggers(QAbstractItemView.CurrentChanged)
		self.statusbar.showMessage("Editable")

	def nonEditable(self):
		self.tableWidget_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.statusbar.showMessage("Non Editable")
		
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

	def readJson(self):
		temp_1 = self.comBox_1.currentText()
		temp_2 = self.comBox_2.currentText()
		with open("./setting.json", "r") as lf:
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
		self.rbtn_1.setChecked(False)
		self.dic = self.readJson()
		if self.dic == 0:
			self.spinBox_1.setValue(0)
			self.spinBox_2.setValue(0)
			self.spinBox_3.setValue(0)
			self.spinBox_4.setValue(0)
		else:
			item = self.dic["elements"]
			for i in range(len(item)):
				if "blur" in item[i].keys():
					self.blur_list.append(item[i])
				if "mediaId" in item[i].keys():
					self.cell_list.append(item[i])
				if "imageName" in item[i].keys():
					self.bg_list.append(item[i])
				if "textId" in item[i].keys():
					self.text_list.append(item[i])
				if "contentMode" in item[i].keys():
					self.level_list.append(item[i])
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
			self.tableWidget_4.setRowCount(self.spinBox_4.value())

		if self.rbtn_1.isChecked() == True:
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


	#点击生成按钮的槽函数
	def createTable(self):
		self.nonEditable()
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
			self.initComBox()
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
				self.tableWidget_3.setItem(i,2,QTableWidgetItem("template_widget_"+name[self.count:]+".png"))
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
			if self.rbtn_1.isChecked() == True:
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

	def saveTable(self):
		self.nonEditable()
		if self.checkValues():
			if self.spinBox_2 != 0:
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

	def checkValues(self):
		if self.spinBox_1.value() != 0:
			for i in range(self.spinBox_1.value()):
				if self.tableWidget_1.item(i,2) == None or self.tableWidget_1.item(i,2).text() == "":

					self.info = "blur表中第 "+str(i+1)+" 行第 3 列未填值！"
					return False

		if self.spinBox_2.value() != 0:
			for i in range(self.spinBox_2.value()):
				for j in range(self.tableWidget_2.columnCount()):
					if self.tableWidget_2.item(i,j) == None or self.tableWidget_2.item(i,j).text() == "":
						self.info = "cell表中第 "+str(i+1)+" 行第 "+str(j+1)+" 列未填值！"
						return False

		if self.spinBox_4.value() != 0:
			print("3")
			for i in range(self.spinBox_4.value()):
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
		if self.spinBox_1.value() != 0:
			for i in range(self.spinBox_1.value()):
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

		if self.spinBox_2.value() != 0:
			for i in range(self.spinBox_2.value()):
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

		if self.spinBox_3.value() != 0:
			for i in range(self.spinBox_3.value()):
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

		if self.spinBox_4.value() != 0:
			for i in range(self.spinBox_4.value()):
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

		if self.rbtn_1.isChecked() == True:
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
			pathJar = "./jar/encrypt.jar" 
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


















		










        











