# coding: utf-8
import sys, json, os
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from DirWindowUi import Ui_DirWindow
from StaticFilePath import SETTING_JSON_PATH


class MyDirWindow(QWidget, Ui_DirWindow):
	def __init__(self):
		super(MyDirWindow,self).__init__()
		self.setupUi(self)

	def chooseDir(self):
		directory = QFileDialog.getExistingDirectory(self, "选择工作路径", os.getcwd())
		self.lineEdit.setText(directory)

	def comfirmDir(self):
		dic = {}
		dic["directory"] = self.lineEdit.text()
		with open(SETTING_JSON_PATH, 'w') as dump_f:
			jsonStr = json.dumps(dic,indent = 4)
			dump_f.write(jsonStr)

		QMessageBox.information(self, "提示", "修改成功！")
		self.close()
	 
		

