import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from PaintWindowUi import Ui_PaintWindow
from Material import Production

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
		pro = Production()
		width_ = 300
		height_ = 400
		scene = pro.getBgScene(self.lineEdit.text(), width_, height_)
		self.graphicsView.setScene(scene)
		scene.setSceneRect(200, 100, 300, 400)










	# def ratio_16_9(self):




	# def ratio_18_9(self):
		







