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
		
		# 读取setting.json,获取workspace路径
		with open("./resources/json/setting.json") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		self.num = templatePath.rsplit("-",1)[1]
		self.path = dic["directory"] + "/" + objPath + "/in/" + self.num

		self.analyseJson()
		self.setLayout()

	# 获取已经保存的template.json
	def getJsonDic(self):
		with open(self.path + "/template.json") as lf:
			size = os.path.getsize(self.path)
			if size != 0:
				jsonStr = lf.read()
				dic = json.loads(jsonStr, strict = False)
				return dic
			else:
				return 0

	# 分解json
	def analyseJson(self):
		self.cell = []
		self.text = []
		dic = self.getJsonDic()
		if dic != 0:
			for i in range(len(dic["elements"])):
				if "mediaId" in dic["elements"][i]:
					self.cell.append(dic["elements"][i])
				if "textId" in dic["elements"][i]:
					self.text.append([dic["elements"][i]])

	def setLayout(self):	
		# 添加cell
		# for i in range(len(self.cell)):
		# 	left = self.cell[i]["constraints"]["left"]["percentage"] 
		# 	right = self.cell[i]["constraints"]["right"]["percentage"]
		# 	top = self.cell[i]["constraints"]["top"]["percentage"]
		# 	height = self.cell[i]["constraints"]["height"]["percentage"]
		# 	per = {"left":left, "right":right, "top":top, "height":height}
		# 	self.setCell(**per)

		# 添加背景
		self.setBg()
 
		# 添加文字
		

	def setCell(self, **per):
		pass
		# self.scene.addItem()

	def setText(self, **per):
		pass
		# self.scene.addItem()

	def setBg(self):
		pic = self.path + "/template_widget_" + self.num + ".png"
		image = QImage()
		image.load(pic)
		pixmap = QPixmap.fromImage(image)
		fitPixmap = pixmap.scaled(270, 480, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
		self.scene = QGraphicsScene()
		self.scene.addPixmap(fitPixmap)

		self.graphicsView.setScene(self.scene)

		



		
		


	


		







