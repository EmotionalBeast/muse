#coding: utf-8
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication
import sys

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     scene = QGraphicsScene()
#     scene.addText("Hello World!")
#     view = QGraphicsView()
#     view.show()

class WindowMain(QGraphicsView):
    def __init__(self):
        super(WindowMain, self).__init__()
        self.scene = QGraphicsScene()
        self.scene.addText("Hello world!")
        self.setScene(self.scene)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = WindowMain()
    mainWindow.show()
    sys.exit(app.exec_())