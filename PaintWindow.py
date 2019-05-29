import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PaintWindowUi import Ui_PaintWindow

class MyPaintWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.paintWindow = Ui_PaintWindow()
        self.paintWindow.setupUi(self)
    # def 




