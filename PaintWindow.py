# coding: utf-8
import sys,json,os
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from PaintWindowUi import Ui_PaintWindow

width = 360
class MyPaintWindow(QWidget, Ui_PaintWindow):
	def __init__(self,objPath,templatePath):
		super(MyPaintWindow,self).__init__()
		self.setupUi(self)
		
		#读取setting.json,获取workspace路径
		with open("./resources/json/setting.json") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		temp = templatePath.rsplit("-",1)
		self.path = dic["directory"] + "/" + objPath + "/in/" + temp[1] + "/template.json"

	#获取已经保存的template.json
	def getJsonDic(self):
		with open(self.path) as lf:
			size = os.path.getsize(self.path)
			if size != 0:
				jsonStr = lf.read()
				dic = json.loads(jsonStr, strict = False)
				return dic
			else:
				return 0

	#分解json
	# def analyseJson(self):
	# 	self.cell = []
	# 	self.text = []
	# 	dic = self.getJsonDic()
	# 	for i in len(dic["elements"]):
	# 		if ""



	#
	# def getScene(self, bgName, width, height):
	# 	#添加背景图片
	# 	image = QImage()
	# 	image.load(bgName)
	# 	pixmap = QPixmap.fromImage(image)
	# 	fitPixmap = pixmap.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)  # 饱满填充
	# 	scene = QGraphicsScene()
	# 	scene.addPixmap(fitPixmap)
	#
	# 	#添加cell


		#添加文字
		for i in range(len(self.text_list)):
			label = QLabel()
			label.setText(self.text_list[i]["placeHolder"])
			scene.addItem(label)

		return scene

	


		







