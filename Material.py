#-*- coding: utf-8 -*-


from PyQt5.QtGui import  QPixmap, QImage
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class Production:
	def getBg(self, bgName,label):
		image = QImage()
		image.load(bgName)
		pixmap = QPixmap.fromImage(image)
		width_ = label.width()
		height_ = label.height()
		fitPixmap = pixmap.scaled(width_, height_, Qt.IgnoreAspectRatio, Qt.SmoothTransformation) #饱满填充
		# fitPixmap = pixmap.scaled(width_, height_, Qt.KeepAspectRatio, Qt.SmoothTransformation) #按比例缩放
		label.setPixmap(pixmap)
		return label


	def getText(self, text):
		label = QLabel()
		label.setText(text)
		return label







