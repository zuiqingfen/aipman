from PyQt5 import QtWidgets
import sys
import base64
import hashlib
import urllib.parse
import time,datetime

import Ui_untitled

class apiman(QtWidgets.QMainWindow,Ui_untitled.Ui_MainWindow):
    def __init__(self):
        super(apiman,self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_untitled.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    window = apiman()
    window.show()
    sys.exit(app.exec_())
