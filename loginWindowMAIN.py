import sys

from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from loginWindowGUI import Ui_loginWindowClass


class loginWindow(QWidget):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.loginUI = Ui_loginWindowClass()
        self.loginUI.setupUi(self)

        self.loginUI.illegalEntry.hide()
        self.loginUI.passwordEntry.setEchoMode(QLineEdit.Password)
        self.loginUI.loginButton.clicked.connect(self.validateLogin)

        self.loginUI.illegalEntryMovie = QtGui.QMovie("E:\\CODING\\Artificial_Intelligence\\Ultimate JARVIS with GUI YT  Playlist files\\illegalEntry.gif")
        self.loginUI.illegalEntry.setMovie(self.loginUI.illegalEntryMovie)

        self.loginUI.retryButton.clicked.connect(self.retryButton)
        self.loginUI.exitButton.clicked.connect(self.close)
        self.loginUI.backButton.clicked.connect(self.backButtonFun)

    def backButtonFun(self):
        from faceRECOG import faceRECOG
        self.showFaceRecogWindow = faceRECOG()
        ui.close()
        self.showFaceRecogWindow.show()

    def retryButton(self):
        self.loginUI.usernameEntry.clear()
        self.loginUI.passwordEntry.clear()
        self.stopMovie()

    def validateLogin(self):
        username = self.loginUI.usernameEntry.text()
        password = self.loginUI.passwordEntry.text()
        if username == "kartis" and password == "pass":
            print("Login Success")
        else:
            self.playMovie()

    def playMovie(self):
        self.loginUI.illegalEntry.show()
        self.loginUI.illegalEntryMovie.start()

    def stopMovie(self):
        self.loginUI.illegalEntry.hide()
        self.loginUI.illegalEntryMovie.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = loginWindow()
    ui.show()
    sys.exit(app.exec_())
