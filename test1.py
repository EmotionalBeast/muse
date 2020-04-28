import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QApplication




# from View import interface

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__(None)
        self.setWindowTitle("对金属腐蚀性试验仪")
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(10)
        self.loginLabel = QLabel("用户名：")
        self.loginLabel.setAlignment(Qt.AlignRight)
        self.loginLabel.setStyleSheet("color:rgb(20,20,20,255);font-size:16px;font-weight:bold:text")
        self.loginTxt = QLineEdit()
        self.loginTxt.setText("admin")
        self.loginTxt.setPlaceholderText("User Name")
        self.loginTxt.setClearButtonEnabled(True)
        self.pwdLabel = QLabel("密码：")
        self.pwdLabel.setAlignment(Qt.AlignRight)
        self.pwdTxt = QLineEdit()
        self.pwdTxt.setContextMenuPolicy(Qt.NoContextMenu) #禁止复制粘贴
        self.pwdTxt.setPlaceholderText("Password")
        self.pwdTxt.setText("admin")
        self.pwdTxt.setEchoMode(QLineEdit.Password)
        self.pwdTxt.setClearButtonEnabled(True)
        self.registeredBtn = QPushButton("注册")
        self.loginBtn = QPushButton("登陆")

        self.headLabel = QLabel("用户登陆")
        self.headLabel.resize(300,30)
        self.headLabel.setAlignment(Qt.AlignCenter)
        self.headLabel.setStyleSheet("color:rgb(10,10,10,255);font-size:50px;font-weight:bold;font-family:Arial;")

        self.headLabel.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        layout.addWidget(self.headLabel,0,0,1,2)
        policy = self.headLabel.sizePolicy()
        print(policy.verticalPolicy())
        policy.setVerticalPolicy(1)
        print(policy.verticalPolicy())
        # policy.setVerticalPolicy(1)
        layout.addWidget(self.loginLabel,1,0)
        layout.addWidget(self.loginTxt,1,1)
        layout.addWidget(self.pwdLabel,2,0)
        layout.addWidget(self.pwdTxt,2,1)
        layout.addWidget(self.registeredBtn,3,0)
        layout.addWidget(self.loginBtn,3,1)

        frame = QFrame(self)
        frame.setLayout(layout)
        self.setCentralWidget(frame)
        self.resize(300,150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.activateWindow()
    mainWindow.raise_()
    app.exec_()
    del mainWindow
    del app