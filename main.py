from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCursor, QPixmap
import os
import vk_api
import webbrowser
from tkinter import messagebox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 120)
        MainWindow.setMinimumSize(QtCore.QSize(415, 120))
        MainWindow.setMaximumSize(QtCore.QSize(415, 120))
        MainWindow.setSizeIncrement(QtCore.QSize(415, 120))
        MainWindow.setBaseSize(QtCore.QSize(415, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ComboAcc = QtWidgets.QComboBox(self.centralwidget)
        self.ComboAcc.setGeometry(QtCore.QRect(90, 10, 321, 31))
        self.ComboAcc.setStyleSheet("color: rgb(255, 0, 0);")
        self.ComboAcc.setObjectName("ComboAcc")
        self.ComboAcc.addItem("")
        self.ComboAcc.addItem("")
        self.ComboAcc.addItem("")
        self.GithubBut = QtWidgets.QPushButton(self.centralwidget)
        self.GithubBut.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.GithubBut.setObjectName("GithubBut")

        self.GithubBut.clicked.connect(self.gitlink)

        self.AccessBut = QtWidgets.QPushButton(self.centralwidget)
        self.AccessBut.setGeometry(QtCore.QRect(90, 60, 321, 51))
        self.AccessBut.setObjectName("AccessBut")

        self.AccessBut.clicked.connect(self.Combocheck)

        self.ExitBut = QtWidgets.QPushButton(self.centralwidget)
        self.ExitBut.setGeometry(QtCore.QRect(10, 60, 75, 51))
        self.ExitBut.setObjectName("ExitBut")

        self.ExitBut.clicked.connect(self.exit)

        self.BackGFrame = QtWidgets.QFrame(self.centralwidget)
        self.BackGFrame.setGeometry(QtCore.QRect(-90, -11, 531, 261))
        self.BackGFrame.setStyleSheet("background-color: rgb(116, 116, 116);")
        self.BackGFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackGFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackGFrame.setObjectName("BackGFrame")
        self.BackGFrame.raise_()
        self.ComboAcc.raise_()
        self.GithubBut.raise_()
        self.AccessBut.raise_()
        self.ExitBut.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        pix = QPixmap(os.path.join("include", "cursor.png"))
        cursor = QCursor(pix)
        MainWindow.setCursor(cursor)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SunRiseVkAuth"))

        self.ComboAcc.setItemText(0, _translate("MainWindow", "YANES4CBS"))
        self.ComboAcc.setItemText(1, _translate("MainWindow", "YAS4CBS"))
        self.ComboAcc.setItemText(2, _translate("MainWindow", "Corro"))

        self.GithubBut.setText(_translate("MainWindow", "Github"))
        self.AccessBut.setText(_translate("MainWindow", "Подтвердить Vk"))
        self.ExitBut.setText(_translate("MainWindow", "Exit"))

    def gitlink(self):
        webbrowser.open("https://github.com/S4CBS")

    def exit(self):
        sys.exit()

    def Combocheck(self):
        import random
        cc = random.randint(0, 9999)
        token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        curr = self.ComboAcc.currentIndex()
        if curr >= 0:
            vk.messages.send(user_id="-xxxxxxxx", message="your message", random_id=cc)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())