#-*- coding: utf-8 -*-


from PyQt5.QtGui import  QPixmap, QImage
from PyQt5.QtWidgets import QLabel, QGraphicsScene
from PyQt5.QtCore import Qt


class Production:
	def getBgScene(self, bgName, width_, height_):
		# image = QImage()
		# image.load(bgName)
		# pixmap = QPixmap.fromImage(image)
		# width_ = label.width()
		# height_ = label.height()
		# fitPixmap = pixmap.scaled(width_, height_, Qt.IgnoreAspectRatio, Qt.SmoothTransformation) #饱满填充
		# # fitPixmap = pixmap.scaled(width_, height_, Qt.KeepAspectRatio, Qt.SmoothTransformation) #按比例缩放
		# label.setPixmap(pixmap)
		# return label
		image = QImage()
		image.load(bgName)
		pixmap = QPixmap.fromImage(image)
		fitPixmap = pixmap.scaled(width_, height_, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)#饱满填充
		scene = QGraphicsScene()
		scene.addPixmap(fitPixmap)
		return scene





	def getText(self, text):
		label = QLabel()
		label.setText(text)
		return label







