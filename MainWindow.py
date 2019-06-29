from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


mainWindow = MainWindow()
mainWindow.show()
mainApplication = QApplication([])
mainApplication.exec_()



