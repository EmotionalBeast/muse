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
				"File System", './', "Image Files(*.png *.jpg )")

		if len(fileName) == 0:
			QMessageBox.information(self, "Tips", "No file selected!")
		else:
			self.lineEdit.setText(fileName)

	def ratio_4_3(self):
		label_4_3 = QLabel(self)
		label_4_3.setObjectName("label_4_3")
		pro = Production()
		label_4_3 = pro.getBg(self.lineEdit.text(), label_4_3)
		label_4_3.setGeometry(QRect(315, 120, 300, 400))







	# def ratio_16_9(self):




	# def ratio_18_9(self):
		







