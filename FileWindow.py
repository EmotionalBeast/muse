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

		if self.judgement():
			for i in range(int(self.lineEdit_2.text()), int(self.lineEdit_3.text())+1):
				tempPath = pathIn + "/" + str(i) + "/images"
				os.mkdir(tempPath)

			for path in self.ai:
				tempPath = path + "/android/text"
				for root,dirs,files in os.walk(tempPath):
					for dir in dirs:
						if dir[:4] == "text":
							tempPath1 = pathIn + "/" + path[-len(self.lineEdit_2.text()):] + "/" + dir
							os.mkdir(tempPath1)
							tempPath2 = pathIn + "/" + path[-len(self.lineEdit_2.text()):] + "/" + dir + "/images"
							os.mkdir(tempPath2)
				
	def getDirectory(self):
		with open("./resources/json/setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		return dic["directory"]

	def copyFile(self):
		count = len(self.lineEdit_2.text())
		path = self.lineEdit_4.text()
		#复制静态文件
		for root,dirs,files in os.walk(path):
			for file in files:
				if file[-3:] == "png" and len(file) == count + 4 and root[-6:] != "images":
					old = root + "/" + file
					new = self.getDirectory() + '/' + self.lineEdit_1.text() + "/in/" + file[:count] + "/" + "template_widget_" + file[:count] + ".png" 
					shutil.copyfile(old,new)
		if len(self.ai) != 0:
			#复制android文件夹下的文件
			for path in self.ai:
				for root,dirs,files in os.walk(path + "/android/image"):
					for file in files:
						if file[-4:] == "json":
							old = root + "/" + file
							new = self.getDirectory() + "/" + self.lineEdit_1.text() + "/in/" + path[-count:] + "/" + file
							shutil.copyfile(old,new)
						if file[-3:] == "png":
							old = root + "/" + file
							new = self.getDirectory() + "/" + self.lineEdit_1.text() + "/in/" + path[-count:] + "/images/" + file
							shutil.copyfile(old,new)
				for root,dirs,files in os.walk(path + "/android/text"):
					for file in files:
						if file[-4:] == "json":
							old = root + "/" + file
							new = self.getDirectory() + "/" + self.lineEdit_1.text() + "/in/" + path[-count:] + "/" + root[-5:] + "/" + file[:4] + "_a.json"
							shutil.copyfile(old,new)
				#复制ios文件夹下的文件
				for root,dirs,files in os.walk(path + "/ios/text"):
					for file in files:
						if file == "data.json":
							old = root + "/" + file
							new = self.getDirectory() + "/" + self.lineEdit_1.text() + "/in/" + path[-count:] + "/" + root[-5:] + "/" + file
							shutil.copyfile(old,new)
						if file[-3:] == "png":
							old = root + "/" + file
							new = self.getDirectory() + "/" + self.lineEdit_1.text() + "/in/" + path[-count:] + "/" + root[-12:] + "/" + file
							shutil.copyfile(old,new)

	def createJson(self):
		path = self.getDirectory() + '/' + self.lineEdit_1.text() + "/in"
		for root,dirs,files in os.walk(path):
			for dir in dirs:
				if root == path:
					tempPath = os.path.join(root,dir)
					open(tempPath + "/" + "template.json", "w")

	def judgement(self):
		self.ai = []
		path = self.lineEdit_4.text()
		for root,dirs,files in os.walk(path):
			for dir in dirs:
				if dir.lower() == "android":
					self.ai.append(root)
		if len(self.ai) != 0:
			return True
		else:
			return False












	







		