# coding: utf-8
import sys,json,os
from PyQt5.QtWidgets import (QWidget, QApplication, QFileDialog, QMessageBox, 
								QGraphicsScene, QLabel, QGraphicsItem, QGraphicsProxyWidget, QGraphicsSimpleTextItem)
from PyQt5.QtGui import QPixmap, QImage, QFontDatabase
from PyQt5.QtCore import QRect, Qt
from PaintWindowUi import Ui_PaintWindow
from PIL import Image, ImageFilter

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

		# self.loadFont()
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
		self.blur = []
		dic = self.getJsonDic()
		if dic != 0:
			for i in range(len(dic["elements"])):
				if "mediaId" in dic["elements"][i]:
					self.cell.append(dic["elements"][i])
				if "textId" in dic["elements"][i]:
					self.text.append(dic["elements"][i])
				if "blur" in dic["elements"][i]:
					self.blur.append(dic["elements"][i])
	def setLayout(self):
		# 初始化graphicScene,添加cell
		#特殊模版，背景虚化
		if len(self.blur) != 0:
			self.setBlur()
		#普通cell
		for i in range(len(self.cell)):
			left = self.cell[i]["constraints"]["left"]["percentage"] 
			right = self.cell[i]["constraints"]["right"]["percentage"]
			top = self.cell[i]["constraints"]["top"]["percentage"]
			height = self.cell[i]["constraints"]["height"]["percentage"]
			cell_dic = {"left":left, "right":right, "top":top, "height":height}
			self.setCell(i, **cell_dic)

		# 初始化graphicScene,添加背景
		self.setBg()
 
		# 初始化graphicScene,添加文字
		for i in range(len(self.text)):
			font = self.text[i]["fontName"]
			size = self.text[i]["fontSize"]
			color = self.text[i]["textColor"]
			content = self.text[i]["placeHolder"]
			alignment = self.text[i]["textAlignment"]
			left = self.text[i]["constraints"]["left"]["percentage"]
			right = self.text[i]["constraints"]["right"]["percentage"]
			top = self.text[i]["constraints"]["top"]["percentage"]
			text_dic = {"font":font, "size":size, "color":color, "content":content, "alignment":alignment, "left":left, "right":right, "top":top}
			self.setText(**text_dic)

		# 将graphicsScene放置在当前的graphicView中
		self.graphicsView.setScene(self.scene)

	def setBlur(self):
		pic = "./resources/pictures/img_1.jpeg"
		image = QImage()
		image.load(pic)
		pixmap = QPixmap.fromImage(image)
		fitPixmap = pixmap.scaled(270, 480)
		self.scene.addPixmap(fitPixmap).setPos(0,0)

	def setCell(self, count, **dic):
		x = 270*dic["left"]
		y = 480*dic["top"]
		w = 270*(1-dic["left"]-dic["right"])
		h =	480*dic["height"]
		pic = "./resources/pictures/img_" + str(count+1) +".jpeg"
		image = QImage()
		image.load(pic)
		pixmap = QPixmap.fromImage(image)
		fitPixmap = pixmap.scaled(w, h)
		self.scene.addPixmap(fitPixmap).setPos(x,y)

	def setText(self, **dic):
		x = 270*dic["left"]
		y = 480*dic["top"]
		w = 270*(1-dic["left"]-dic["right"])
		h = 480*(1-dic["top"])
		label = QLabel()
		label.resize(w, h)
		label.setText(dic["content"])
		if dic["alignment"] == "right":
			label.setAlignment(Qt.AlignTop | Qt.AlignRight)
		elif dic["alignment"] == "left":
			label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		else:
			label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
		fontNum = int(dic["size"]*0.48)
		font = "color: #" + dic["color"] + ";background-color: transparent" + ";font-size:" + str(fontNum) + "px" 
		label.setStyleSheet(font)
		label.setWordWrap(True)
		self.scene.addWidget(label).setPos(x, y)

	def setBg(self):
		pic = self.path + "/template_widget_" + self.num + ".png"
		image = QImage()
		image.load(pic)
		pixmap = QPixmap.fromImage(image)
		fitPixmap = pixmap.scaled(270, 480, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
		self.scene.addPixmap(fitPixmap)

	# def loadFont(self):
	# 	self.fonts = []
	# 	for root,dirs,files in os.walk("./resources/fonts"):
	# 		for file in files:
	# 			if file[-3:] == "tty":
	# 				num = QFontDatabase.addApplicationFont(root + "/" + file)
	# 				self.fonts.append(num)




		



		
		


	


		







