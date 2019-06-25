# coding: utf-8
import sys, json
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from DirWindowUi import Ui_DirWindow


class MyDirWindow(QWidget, Ui_DirWindow):
	def __init__(self):
		super(MyDirWindow,self).__init__()
		self.setupUi(self)

	def chooseDir(self):
		directory = QFileDialog.getExistingDirectory(self, "选择工作路径", "./")
		self.lineEdit.setText(directory)

	def comfirmDir(self):
		dic = {}
		dic["directory"] = self.lineEdit.text()
		with open("./resources/json/setting.json", 'w') as dump_f:
			jsonStr = json.dumps(dic,indent = 4)
			dump_f.write(jsonStr)

		QMessageBox.information(self, "提示", "修改成功！")
		self.close()
		

