# -*- coding: utf-8 -*-
#author: Jhin Yao

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QAbstractItemView, QComboBox
#from PyQt5.QtGui import 
#from PyQt5.QtCore import QTextStream, QFile
import json
from mainwindow import Ui_MainWindow
from operatejson import OperateJson


class MyMainWindow(QMainWindow,Ui_MainWindow):

	def __init__(self):
		super(MyMainWindow,self).__init__()
		self.setupUi(self)
		with open("./font.json", 'r') as lf:
			jsonStr = lf.read()
			self.dict1 = json.loads(jsonStr, strict = False)
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
			dic = jsonFile.loadJson()
			self.valuedTable(dic)
		self.nonEditable()

	def valuedTable(self, dic):
		self.lineEdit_1.setText(str(dic['templateId']))
		list_ = dic['elements']
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
			self.tableWidget_2.setItem(i,0,QTableWidgetItem(cell_list[i]['id']))
			self.tableWidget_2.setItem(i,1,QTableWidgetItem(cell_list[i]['type']))
			self.tableWidget_2.setItem(i,2,QTableWidgetItem(cell_list[i]['mediaId']))
			self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(cell_list[i]['constraints']['left']['percentage'])))
			self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(cell_list[i]['constraints']['left']['constant'])))
			self.tableWidget_2.setItem(i,5,QTableWidgetItem(str(cell_list[i]['constraints']['right']['percentage'])))
			self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(cell_list[i]['constraints']['right']['constant'])))
			self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(cell_list[i]['constraints']['top']['percentage'])))
			self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(cell_list[i]['constraints']['top']['constant'])))
			self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(cell_list[i]['constraints']['height']['percentage'])))
			self.tableWidget_2.setItem(i,10,QTableWidgetItem(str(cell_list[i]['constraints']['height']['constant'])))

		
		for i in range(len(bg_list)):
			self.tableWidget_3.setItem(i,0,QTableWidgetItem(bg_list[i]['id']))
			self.tableWidget_3.setItem(i,1,QTableWidgetItem(bg_list[i]['type']))
			self.tableWidget_3.setItem(i,2,QTableWidgetItem(bg_list[i]['imageName']))
			self.tableWidget_3.setItem(i,3,QTableWidgetItem(str(bg_list[i]['constraints']['left']['percentage'])))
			self.tableWidget_3.setItem(i,4,QTableWidgetItem(str(bg_list[i]['constraints']['left']['constant'])))
			self.tableWidget_3.setItem(i,5,QTableWidgetItem(str(bg_list[i]['constraints']['right']['percentage'])))
			self.tableWidget_3.setItem(i,6,QTableWidgetItem(str(bg_list[i]['constraints']['right']['constant'])))
			self.tableWidget_3.setItem(i,7,QTableWidgetItem(str(bg_list[i]['constraints']['top']['percentage'])))
			self.tableWidget_3.setItem(i,8,QTableWidgetItem(str(bg_list[i]['constraints']['top']['constant'])))
			self.tableWidget_3.setItem(i,9,QTableWidgetItem(str(bg_list[i]['constraints']['bottom']['percentage'])))
			self.tableWidget_3.setItem(i,10,QTableWidgetItem(str(bg_list[i]['constraints']['bottom']['constant'])))

		for i in range(len(text_list)):
			self.tableWidget.setItem(i,0,QTableWidgetItem(text_list[i]['id']))
			self.tableWidget.setItem(i,1,QTableWidgetItem(text_list[i]['type']))
			self.tableWidget.setItem(i,2,QTableWidgetItem(text_list[i]['textId']))
			self.tableWidget.cellWidget(i,3).setCurrentText(self.dict2[text_list[i]["fontName"]])
			self.tableWidget.setItem(i,4,QTableWidgetItem(str(text_list[i]['fontSize'])))
			self.tableWidget.setItem(i,5,QTableWidgetItem(str(text_list[i]['canvasWidth'])))
			self.tableWidget.setItem(i,6,QTableWidgetItem(text_list[i]['textColor']))
			self.tableWidget.setItem(i,7,QTableWidgetItem(text_list[i]['placeHolder']))
			self.tableWidget.setItem(i,8,QTableWidgetItem(text_list[i]['textAlignment']))
			self.tableWidget.setItem(i,9,QTableWidgetItem(str(text_list[i]['constraints']['left']['percentage'])))
			self.tableWidget.setItem(i,10,QTableWidgetItem(str(text_list[i]['constraints']['left']['constant'])))
			self.tableWidget.setItem(i,11,QTableWidgetItem(str(text_list[i]['constraints']['right']['percentage'])))
			self.tableWidget.setItem(i,12,QTableWidgetItem(str(text_list[i]['constraints']['right']['constant'])))
			self.tableWidget.setItem(i,13,QTableWidgetItem(str(text_list[i]['constraints']['top']['percentage'])))
			self.tableWidget.setItem(i,14,QTableWidgetItem(str(text_list[i]['constraints']['top']['constant'])))



	def saveTable(self):
		self.nonEditable()
		fileName, fileType = QFileDialog.getSaveFileName(self, 'Save File', './', "Text Files(*.json)")

		if len(fileName) == 0:
			QMessageBox.information(self, "Tips", "No file selected!")
		else:	
			dic = self.getItemText()
			jsonFile = OperateJson(fileName)
			jsonFile.dumpJson(dic)



	def getItemText(self):
		dic = {}
		dic['templateId'] = int(self.lineEdit_1.text())
		dic['elements'] = []
		cell_dic = {}
		bg_dic = {}
		text_dic = {}


		for i in range(self.tableWidget_2.rowCount()):
			if self.tableWidget_2.item(i,1) != None:
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

		for i in range(self.tableWidget.rowCount()):
			if self.tableWidget.item(i, 1) != None:
				text_dic['id'] = self.tableWidget.item(i, 0).text()
				text_dic['type'] = self.tableWidget.item(i, 1).text()
				text_dic['textId'] = self.tableWidget.item(i, 2).text()
				text_dic['fontName'] = self.dict1[self.tableWidget.cellWidget(i, 3).currentText()]
				text_dic['fontSize'] = int(self.tableWidget.item(i, 4).text())
				text_dic['canvasWidth'] = int(self.tableWidget.item(i, 5).text())
				text_dic['textColor'] = self.tableWidget.item(i, 6).text()
				text_dic['placeHolder'] = self.tableWidget.item(i, 7).text()
				text_dic['textAlignment'] = self.tableWidget.item(i, 8).text()
				item_1 = self.tableWidget.item(i,9).text()
				item_2 = self.tableWidget.item(i,10).text()
				item_3 = self.tableWidget.item(i,11).text()
				item_4 = self.tableWidget.item(i,12).text()
				item_5 = self.tableWidget.item(i,13).text()
				item_6 = self.tableWidget.item(i,14).text()
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


	def createNewTable(self):
		reply = QMessageBox.question(self, 'Message', 'You sure to clear all and create new tables?',
									 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if reply == QMessageBox.Yes:
			self.cleanContents()
			
		self.editable()

	def editable(self):
		self.tableWidget_2.setEditTriggers(QAbstractItemView.CurrentChanged)
		self.tableWidget_3.setEditTriggers(QAbstractItemView.CurrentChanged)
		self.tableWidget.setEditTriggers(QAbstractItemView.CurrentChanged)
		self.statusbar.showMessage("Editable")

	def nonEditable(self):
		self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.statusbar.showMessage("Non Editable")

	def cleanContents(self):
		self.tableWidget_2.clearContents()
		self.tableWidget_3.clearContents()
		self.lineEdit_1.clear()
		self.comBox_03.clearEditText()
		self.comBox_13.clearEditText()
		self.comBox_23.clearEditText()
		self.comBox_33.clearEditText()
		self.comBox_43.clearEditText()
		for i in range(self.tableWidget.columnCount()):
			if i != 3:
				for j in range(self.tableWidget.rowCount()):
					self.tableWidget.takeItem(j,i)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	myWindow = MyMainWindow()
	myWindow.show()
	sys.exit(app.exec_())

