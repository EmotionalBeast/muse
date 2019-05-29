# -*- coding: utf-8 -*-
# author: Jhin Yao

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MyMainWindow



if __name__ == '__main__':
	app = QApplication(sys.argv)
	myWindow = MyMainWindow()
	myWindow.show()
	sys.exit(app.exec_())
