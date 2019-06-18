# -*- coding: utf-8 -*-
#author: Jhin Yao

import json
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
													QTableWidgetItem, QAbstractItemView, QComboBox)
from PyQt5.QtCore import Qt
from MainWindowUi import Ui_MainWindow
from OperateData import OperateJson
from PaintWindow import MyPaintWindow
from DirWindow import MyDirWindow
from FileWindow import MyFileWindow


class MyMainWindow(QMainWindow,Ui_MainWindow):

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


	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message', 'You sure to quit?',
									 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

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

	def valuedTable(self, dic):
		self.lineEdit_1.setText(str(dic['templateId']))
		list_ = dic['elements']
		blur_list = []
		cell_list = []
		bg_list = []
		text_list = []

		for i in range(len(list_)):
			if list_[i]['type'] == "media":
				cell_list.append(list_[i])
			elif list_[i]['type'] == "image":
				bg_list.append(list_[i])
			else:
				text_list.append(list_[i])

		for i in range(len(cell_list)):
			# self.tableWidget_2.setItem(i,0,QTableWidgetItem(cell_list[i]['id']))
			# self.tableWidget_2.setItem(i,1,QTableWidgetItem(cell_list[i]['type']))
			# self.tableWidget_2.setItem(i,2,QTableWidgetItem(cell_list[i]['mediaId']))
			self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(cell_list[i]['constraints']['left']['percentage'])))
			# self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(cell_list[i]['constraints']['left']['constant'])))
			self.tableWidget_2.setItem(i,5,QTableWidgetItem(str(cell_list[i]['constraints']['right']['percentage'])))
			# self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(cell_list[i]['constraints']['right']['constant'])))
			self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(cell_list[i]['constraints']['top']['percentage'])))
			# self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(cell_list[i]['constraints']['top']['constant'])))
			self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(cell_list[i]['constraints']['height']['percentage'])))
			# self.tableWidget_2.setItem(i,10,QTableWidgetItem(str(cell_list[i]['constraints']['height']['constant'])))

		
		for i in range(len(bg_list)):
			# self.tableWidget_3.setItem(i,0,QTableWidgetItem(bg_list[i]['id']))
			# self.tableWidget_3.setItem(i,1,QTableWidgetItem(bg_list[i]['type']))
			self.tableWidget_3.setItem(i,2,QTableWidgetItem(bg_list[i]['imageName']))
			self.tableWidget_3.setItem(i,3,QTableWidgetItem(str(bg_list[i]['constraints']['left']['percentage'])))
			# self.tableWidget_3.setItem(i,4,QTableWidgetItem(str(bg_list[i]['constraints']['left']['constant'])))
			self.tableWidget_3.setItem(i,5,QTableWidgetItem(str(bg_list[i]['constraints']['right']['percentage'])))
			# self.tableWidget_3.setItem(i,6,QTableWidgetItem(str(bg_list[i]['constraints']['right']['constant'])))
			self.tableWidget_3.setItem(i,7,QTableWidgetItem(str(bg_list[i]['constraints']['top']['percentage'])))
			# self.tableWidget_3.setItem(i,8,QTableWidgetItem(str(bg_list[i]['constraints']['top']['constant'])))
			self.tableWidget_3.setItem(i,9,QTableWidgetItem(str(bg_list[i]['constraints']['bottom']['percentage'])))
			# self.tableWidget_3.setItem(i,10,QTableWidgetItem(str(bg_list[i]['constraints']['bottom']['constant'])))

		for i in range(len(text_list)):
			# self.tableWidget_4.setItem(i,0,QTableWidgetItem(text_list[i]['id']))
			# self.tableWidget_4.setItem(i,1,QTableWidgetItem(text_list[i]['type']))
			# self.tableWidget_4.setItem(i,2,QTableWidgetItem(text_list[i]['textId']))
			self.tableWidget_4.cellWidget(i,3).setCurrentText(self.dict2[text_list[i]["fontName"]])
			self.tableWidget_4.setItem(i,4,QTableWidgetItem(str(text_list[i]['fontSize'])))
			# self.tableWidget_4.setItem(i,5,QTableWidgetItem(str(text_list[i]['canvasWidth'])))
			self.tableWidget_4.setItem(i,6,QTableWidgetItem(text_list[i]['textColor']))
			self.tableWidget_4.setItem(i,7,QTableWidgetItem(text_list[i]['placeHolder']))
			self.tableWidget_4.setItem(i,8,QTableWidgetItem(text_list[i]['textAlignment']))
			self.tableWidget_4.setItem(i,9,QTableWidgetItem(str(text_list[i]['constraints']['left']['percentage'])))
			# self.tableWidget_4.setItem(i,10,QTableWidgetItem(str(text_list[i]['constraints']['left']['constant'])))
			self.tableWidget_4.setItem(i,11,QTableWidgetItem(str(text_list[i]['constraints']['right']['percentage'])))
			# self.tableWidget_4.setItem(i,12,QTableWidgetItem(str(text_list[i]['constraints']['right']['constant'])))
			self.tableWidget_4.setItem(i,13,QTableWidgetItem(str(text_list[i]['constraints']['top']['percentage'])))
			# self.tableWidget_4.setItem(i,14,QTableWidgetItem(str(text_list[i]['constraints']['top']['constant'])))



	def saveTable(self):
		# self.nonEditable()
		# fileName, fileType = QFileDialog.getSaveFileName(self, 'Save File', './', "Text Files(*.json)")

		# if len(fileName) == 0:
		# 	QMessageBox.information(self, "Tips", "No file selected!")
		# else:	
		# 	dic = self.getItemText()
		# 	jsonFile = OperateJson(fileName)
		# 	jsonFile.dumpJson(dic)
		QMessageBox.information(self, "提示", "保存成功！")



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


	def openFileWindow(self):
		self.myFileWindow = MyFileWindow()
		self.myFileWindow.setWindowModality(Qt.ApplicationModal)
		self.myFileWindow.show()

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

	def cleanContents(self):
		self.tableWidget_2.clearContents()
		self.tableWidget_3.clearContents()
		self.comBox_03.clearEditText()
		self.comBox_13.clearEditText()
		self.comBox_23.clearEditText()
		self.comBox_33.clearEditText()
		self.comBox_43.clearEditText()
		for i in range(self.tableWidget_4.columnCount()):
			if i != 3:
				for j in range(self.tableWidget_4.rowCount()):
					self.tableWidget_4.takeItem(j,i)

	
	def openPaintWindow(self):
		tup = self.getTableValue()
		self.myPaintWindow = MyPaintWindow(tup)
		self.myPaintWindow.setWindowModality(Qt.ApplicationModal)
		self.myPaintWindow.show()


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

	def openDirWindow(self):
		self.myDirWindow.setWindowModality(Qt.ApplicationModal)
		self.myDirWindow.show()

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

	# def readJson(self):
	# 	with open("./setting.json", "r") as lf:
	# 		jsonStr = lf.read()
	# 		dic = json.loads(jsonStr, strict = False)
	# 	path = dicp["directory"] + "/" + self.comBox_1.currentText() + "/in"

	# 	for root,dirs,files in os.walk(path):
	# 		for file in files:
	# 			if file == "template.json":
	# 				temp = os.path.join(root, file)
	# 				with open(temp, "r") as lf:
	# 					jsonStr = lf.read()
	# 					if jsonStr == None:
		
	# def initDate()

        











