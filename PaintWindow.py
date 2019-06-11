import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from PaintWindowUi import Ui_PaintWindow
from Material import Production


pro_ = Production()
width_ = 300
class MyPaintWindow(QWidget, Ui_PaintWindow):
	def __init__(self):
		super(MyPaintWindow,self).__init__()
		self.setupUi(self)

	def chooseImage(self):
		fileName, fileType = QFileDialog.getOpenFileName(self,
				"File System", './', "Image Files(*.png *.jpg *.ico )")

		if len(fileName) == 0:
			QMessageBox.information(self, "Tips", "No file selected!")
		else:
			self.lineEdit.setText(fileName)

	def ratio_4_3(self):
		#放置底层图片
		height_ = (width_/3)*4
		scene = pro_.getBgScene(self.lineEdit.text(), width_, height_)
		self.graphicsView.setScene(scene)
		scene.setSceneRect(0, 0, width_, height_)
		#添加cell
		#get table's value in MainWindow

		#添加文字
		


	def ratio_16_9(self):
		#放置底层图片
		height_ = (width_/9)*16
		scene = pro_.getBgScene(self.lineEdit.text(), width_, height_)
		self.graphicsView.setScene(scene)
		scene.setSceneRect(0, 0, width_, height_)
		#添加cell

		#添加文字



	def ratio_18_9(self):
		#放置底层图片
		height_ = (width_/9)*18
		scene = pro_.getBgScene(self.lineEdit.text(), width_, height_)
		self.graphicsView.setScene(scene)
		scene.setSceneRect(0, 0, width_, height_)
		







