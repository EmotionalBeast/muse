# coding: utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from DirWindowUi import Ui_DirWindow

class MyDirWindow(QWidget, Ui_DirWindow):
	def __init__(self):
		super(MyDirWindow,self).__init__()
		self.setupUi(self)

	def chooseDir(self):
		dir = QFileDialog.getExistingDirectory(self, "选择工作路径", "./")
		self.lineEdit.setText(dir)


	def getDir(self):
		return self.lineEdit.text()
