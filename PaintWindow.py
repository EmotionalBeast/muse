# coding: utf-8
import sys,json,os
from PyQt5.QtWidgets import (QWidget, QApplication, QFileDialog, QMessageBox, 
								QGraphicsScene, QGraphicsView, QLabel, QGraphicsItem, QGraphicsProxyWidget, QGraphicsSimpleTextItem, QFrame)
from PyQt5.QtGui import QPixmap, QImage, QFontDatabase, QFont
from PyQt5.QtCore import QRect, Qt, QSize
from PaintWindowUi import Ui_PaintWindow
from PIL import Image, ImageFilter
from math import sqrt
from StaticFilePath import SETTING_JSON_PATH

PROPORTION_16_9 = (450, 800)
PROPORTION_1_1 = (450, 450)
import os

class MyPaintWindow(QWidget, Ui_PaintWindow):
	def __init__(self,objPath,templatePath):
		super(MyPaintWindow,self).__init__()
		
		# 读取setting.json,获取workspace路径
		with open(SETTING_JSON_PATH) as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		self.num = templatePath.rsplit("-",1)[1]
		self.template = templatePath.rsplit("-",1)[0]
		self.path = dic["directory"] + "/" + objPath + "/in/" + self.num

		self.analyseJson()
		self.setupUi(self)
		self.setLayout()

	# 获取已经保存的template.json
	def getJsonDic(self):
		path = self.path + "/" + self.template
		with open(path) as lf:
			size = os.path.getsize(path)
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
		self.png = ""
		self.width = 0
		self.height = 0
		self.background = ""
		dic = self.getJsonDic()
		if dic != 0:
			if "background" in dic.keys():
				self.background = dic["background"]
			for i in range(len(dic["elements"])):
				if "mediaId" in dic["elements"][i]:
					self.cell.append(dic["elements"][i])
				if "textId" in dic["elements"][i]:
					self.text.append(dic["elements"][i])
				if "blur" in dic["elements"][i]:
					self.blur.append(dic["elements"][i])
				if "imageName" in dic["elements"][i]:
					self.png = dic["elements"][i]["imageName"]
					tmp = self.png.split(".", 1)[0]
					if tmp[-3:] == "1_1":
						self.width, self.height = PROPORTION_1_1
					else:
						self.width, self.height = PROPORTION_16_9

	def setLayout(self):
		# 初始化graphicScene,添加cell
		#特殊模版，背景虚化
		if self.background != "":
			self.setBgColor()
		if len(self.blur) != 0:
			for i in range(len(self.blur)):
				left = self.blur[i]["constraints"]["left"]["percentage"]
				right = self.blur[i]["constraints"]["right"]["percentage"]
				top = self.blur[i]["constraints"]["top"]["percentage"]
				bottom = self.blur[i]["constraints"]["bottom"]["percentage"]
				if "rotation" in self.blur[i].keys():
					rotation = self.blur[i]["rotation"]
				else:
					rotation = 0
				blur_dic = {"left":left, "right":right, "top":top, "bottom":bottom, "rotation":rotation}
				self.setBlur(i, **blur_dic)
		#普通cell
		for i in range(len(self.cell)):
			left = self.cell[i]["constraints"]["left"]["percentage"] 
			right = self.cell[i]["constraints"]["right"]["percentage"]
			top = self.cell[i]["constraints"]["top"]["percentage"]
			height = self.cell[i]["constraints"]["height"]["percentage"]
			if "rotation" in self.cell[i].keys():
				rotation = self.cell[i]["rotation"]
			else:
				rotation = 0
			cell_dic = {"left":left, "right":right, "top":top, "height":height, "rotation":rotation}
			self.setCell(i, **cell_dic)


		# 初始化graphicScene,添加背景
		self.setPng()

		#设置边框
		for i in range(len(self.cell)):
			left = self.cell[i]["constraints"]["left"]["percentage"] 
			right = self.cell[i]["constraints"]["right"]["percentage"]
			top = self.cell[i]["constraints"]["top"]["percentage"]
			height = self.cell[i]["constraints"]["height"]["percentage"]
			if "rotation" in self.cell[i].keys():
				rotation = self.cell[i]["rotation"]
			else:
				rotation = 0
			cell_dic = {"left":left, "right":right, "top":top, "height":height, "rotation":rotation}
			self.setCellBorder(i, **cell_dic)
 
		# 初始化graphicScene,添加文字
		for i in range(len(self.text)):
			fontName = self.text[i]["fontName"]
			size = self.text[i]["fontSize"]
			color = self.text[i]["textColor"]
			content = self.text[i]["placeHolder"]
			alignment = self.text[i]["textAlignment"]
			angle = self.text[i]["angle"]
			left = self.text[i]["constraints"]["left"]["percentage"]
			right = self.text[i]["constraints"]["right"]["percentage"]
			top = self.text[i]["constraints"]["top"]["percentage"]
			text_dic = {"fontName":fontName, "size":size, "color":color, "content":content, "alignment":alignment, "left":left, "right":right, "top":top, "angle":angle}
			self.setText(**text_dic)
		
		if len(self.blur) != 0:
			for i in range(len(self.blur)):
				left = self.blur[i]["constraints"]["left"]["percentage"]
				right = self.blur[i]["constraints"]["right"]["percentage"]
				top = self.blur[i]["constraints"]["top"]["percentage"]
				bottom = self.blur[i]["constraints"]["bottom"]["percentage"]
				if "rotation" in self.blur[i].keys():
					rotation = self.blur[i]["rotation"]
				else:
					rotation = 0
				blur_dic = {"left":left, "right":right, "top":top, "bottom":bottom, "rotation":rotation}
				self.setBlurBorder(i, **blur_dic)
		


		# 将graphicsScene放置在当前的graphicView中
		self.graphicsView.setScene(self.scene)

	def setBlur(self, count, **dic):
		x = self.width * dic["left"]
		y = self.height * dic["top"]
		w = self.width * (1-dic["left"]-dic["right"])
		h =	self.height * (1-dic["top"]-dic["bottom"])
		r = dic["rotation"]
		max = sqrt(w*w + h*h)
		color = ["#70DB93", "#5C3317", "#9F5F9F", "#B5A642", "#D9D919", "#A62AA2", "#8C7853", "#A67D3D", "#F0F8FF"]
		style = "background-color:" + color[count]
		label = QLabel()
		label.resize(w, h)
		label.setStyleSheet(style)
		scene = QGraphicsScene()
		scene.addWidget(label)
		view = QGraphicsView(scene)
		view.resize(max, max)
		view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		view.rotate(r)
		view.setStyleSheet("background-color:transparent")
		self.scene.addWidget(view).setPos(x-(max-w)/2, y-(max-h)/2)


	def setCell(self, count, **dic):
		x = self.width * dic["left"]
		y = self.height * dic["top"]
		w = self.width * (1-dic["left"]-dic["right"])
		h =	self.height * dic["height"]
		max = sqrt(w*w + h*h)
		r = dic["rotation"]
		color = ["#70DB93", "#5C3317", "#9F5F9F", "#B5A642", "#D9D919", "#A62AA2", "#8C7853", "#A67D3D", "#F0F8FF"]
		if count < 9:
			style = "background-color:" + color[count]
		else:
			style = "background-color:" + color[count-9]
		label = QLabel()
		label.resize(w, h)
		label.setStyleSheet(style)
		scene = QGraphicsScene()
		scene.addWidget(label)
		view = QGraphicsView(scene)
		view.resize(max, max)
		view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		view.rotate(r)
		view.setStyleSheet("background-color:transparent")
		self.scene.addWidget(view).setPos(x-(max-w)/2, y-(max-h)/2)
		
	
	def setCellBorder(self, count, **dic):
		x = self.width * dic["left"]
		y = self.height * dic["top"]
		w = self.width * (1-dic["left"]-dic["right"])
		h =	self.height * dic["height"]
		max = sqrt(w*w + h*h)
		r = dic["rotation"]
		label = QLabel()
		label.resize(w, h)
		label.setFrameShape(QFrame.Box)
		label.setStyleSheet("border:1px solid red;background-color:transparent") #transparent
		scene = QGraphicsScene()
		scene.addWidget(label)
		view = QGraphicsView(scene)
		view.resize(max, max)
		view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		view.rotate(r)
		view.setStyleSheet("background-color:transparent")
		self.scene.addWidget(view).setPos(x-(max-w)/2, y-(max-h)/2)
	
	def setBlurBorder(self, count, **dic):
		x = self.width * dic["left"]
		y = self.height * dic["top"]
		w = self.width * (1-dic["left"]-dic["right"])
		h =	self.height * (1-dic["top"]-dic["bottom"])
		max = sqrt(w*w + h*h)
		r = dic["rotation"]
		label = QLabel()
		label.resize(w, h)
		label.setFrameShape(QFrame.Box)
		label.setStyleSheet("border:1px solid red;background-color:transparent") #transparent
		scene = QGraphicsScene()
		scene.addWidget(label)
		view = QGraphicsView(scene)
		view.resize(max, max)
		view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		view.rotate(r)
		view.setStyleSheet("background-color:transparent")
		self.scene.addWidget(view).setPos(x-(max-w)/2, y-(max-h)/2)



	def setText(self, **dic):
		x = self.width * dic["left"]
		y = self.height * dic["top"]
		w = self.width * (1-dic["left"]-dic["right"])
		h = self.height * (1-dic["top"])
		# max = sqrt(w*w + h*h)
		# r = dic["angle"]
		label = QLabel()
		label.resize(w, h)
		label.setText(dic["content"])
		if dic["alignment"] == "right":
			label.setAlignment(Qt.AlignTop | Qt.AlignRight)
		elif dic["alignment"] == "left":
			label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		else:
			label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
		fontStyle = "color:#" + dic["color"] + ";background-color:transparent;" + "font-size:" + str(round(dic["size"]*1.2)) + "px;" #font-family
		label.setWordWrap(True)    #文本自动换行 transparent
		label.setStyleSheet(fontStyle)
		label.setFont(QFont(dic["fontName"]))
		# scene = QGraphicsScene()
		# scene.addWidget(label)
		# view = QGraphicsView(scene)
		# view.resize(max, max)
		# view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		# view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		# view.rotate(r)
		# view.setStyleSheet("background-color:transparent")
		# self.scene.addWidget(view).setPos(x-(max-w)/2, y-(max-h)/2)
		self.scene.addWidget(label).setPos(x, y)

		
	def setPng(self):
		png = self.path + "/" + self.png
		image = QImage()
		image.load(png)
		pixmap = QPixmap.fromImage(image)
		fitPixmap = pixmap.scaled(self.width, self.height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
		self.scene.addPixmap(fitPixmap)

	def setBgColor(self):
		color = "background-color:#" + self.background
		label = QLabel()
		label.resize(self.width, self.height)
		label.setStyleSheet(color)
		self.scene.addWidget(label).setPos(0, 0)







		



		
		


	


		







