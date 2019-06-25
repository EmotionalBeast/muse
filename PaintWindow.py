# coding: utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from PaintWindowUi import Ui_PaintWindow

width = 360
class MyPaintWindow(QWidget, Ui_PaintWindow):
	def __init__(self,dic):
		super(MyPaintWindow,self).__init__()
		self.setupUi(self)
		self.dic = dic
	

	def getScene(self, bgName, width, height):
		#添加背景图片
		image = QImage()
		image.load(bgName)
		pixmap = QPixmap.fromImage(image)
		fitPixmap = pixmap.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)  # 饱满填充
		scene = QGraphicsScene()
		scene.addPixmap(fitPixmap)

		#添加cell


		#添加文字
		for i in range(len(self.text_list)):
			label = QLabel()
			label.setText(self.text_list[i]["placeHolder"])
			scene.addItem(label)

		return scene

	


		







