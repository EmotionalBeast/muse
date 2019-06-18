# coding: utf-8
import sys, os, json, shutil
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from FileWindowUi import Ui_FileWindow

class MyFileWindow(QWidget, Ui_FileWindow):
	def __init__(self):
		super(MyFileWindow,self).__init__()
		self.setupUi(self)

	def chooseDir(self):
		directory = QFileDialog.getExistingDirectory(self, "选择工作路径", "./")
		self.lineEdit_4.setText(directory)

	def makeDir(self):
		self.createPj()
		self.copyFile()
		self.createJson()
		QMessageBox.information(self, "提示", "创建成功！")
		self.close()

	def createPj(self):
		path = self.getDirectory() + '/' + self.lineEdit_1.text()
		os.mkdir(path) 
		pathIn = path + "/in"
		os.mkdir(pathIn)
		PathOut = path + "/out"
		os.mkdir(PathOut)
		pathOrigin = path + "/origin"
		os.mkdir(pathOrigin)
		for i in range(int(self.lineEdit_2.text()), int(self.lineEdit_3.text())+1):
			tempPath = pathIn + "/" + str(i)
			os.mkdir(tempPath)

	def getDirectory(self):
		with open("./setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		return dic["directory"]

	def copyFile(self):
		path = self.lineEdit_4.text()
		for root,dirs,files in os.walk(path):
			for file in files:
				if len(file) == 8:
					old = root + "/" + file
					new = self.getDirectory() + '/' + self.lineEdit_1.text() + "/in/" + file[:4] + "/" + "template_widget_" + file[:4] + ".png" 
					shutil.copyfile(old,new)


	def createJson(self):
		path = self.getDirectory() + '/' + self.lineEdit_1.text() + "/in"
		for root,dirs,files in os.walk(path):
			for dir in dirs:
				tempPath = os.path.join(root,dir)
				open(tempPath + "/" + "template.json", "w")







	







		