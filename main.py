import sys

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from mainGUIFile import Ui_Dialog


class mainFile(QDialog):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Setting Up GUI")
        self.firstUI = Ui_Dialog()
        self.firstUI.setupUi(self)

        self.firstUI.movie = QtGui.QMovie("E:\\CODING\\Artificial_Intelligence\\Ultimate JARVIS with GUI YT  Playlist files\\gui_tools\\Jarvis_Gui (2).gif")
        self.firstUI.mainGIF.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()

        self.firstUI.exitButton.clicked.connect(self.close)
        self.firstUI.startButton.clicked.connect(self.connectToFaceRecognition)
        self.firstUI.loginButton.clicked.connect(self.connectToLoginWindow)

    def connectToFaceRecognition(self):
        from faceRECOG import faceRECOG
        self.showFaceRecogWindow = faceRECOG()
        ui.close()
        self.showFaceRecogWindow.show()

    def connectToLoginWindow(self):
        from loginWindowMAIN import loginWindow
        self.showLoginWindow = loginWindow()
        ui.close()
        self.showLoginWindow.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())


