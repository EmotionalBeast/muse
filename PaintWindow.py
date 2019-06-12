# coding: utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from PaintWindowUi import Ui_PaintWindow

width = 360
class MyPaintWindow(QWidget, Ui_PaintWindow):
	def __init__(self,tup):
		super(MyPaintWindow,self).__init__()
		self.setupUi(self)
		self.cell_list = tup[0]
		self.text_list = tup[1]

	def chooseImage(self):
		fileName, fileType = QFileDialog.getOpenFileName(self,
				"File System", './', "Image Files(*.png *.jpg *.ico )")

		if len(fileName) == 0:
			QMessageBox.information(self, "Tips", "No file selected!")
		else:
			self.lineEdit.setText(fileName)


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




	def ratio_4_3(self):

		height = (width/3)*4
		scene = self.getScene(self.lineEdit.text(), width, height)
		self.graphicsView.setScene(scene)






		# for i in range(len(self.text_list)):
		# 	content = self.text_list[i]["placeHolder"]
		# 	text_scene = pro_.getTextScene(content)
		# 	self.graphicsView.setScene(text_scene)



		


	def ratio_16_9(self):

		height = (width/9)*16
		scene = self.getScene(self.lineEdit.text(), width, height)
		self.graphicsView.setScene(scene)
		# scene.setSceneRect(0, 0, width, height)






	def ratio_18_9(self):

		height = (width/9)*18
		scene = self.getScene(self.lineEdit.text(), width, height)
		self.graphicsView.setScene(scene)


		







