# coding: utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from FileWindowUi import Ui_FileWindow

class MyFileWindow(QWidget, Ui_FileWindow):
	def __init__(self):
		super(MyFileWindow,self).__init__()
		self.setupUi(self)

	# def getContent(self):
		