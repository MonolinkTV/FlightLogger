from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

CSSSTARTER = "background-color: rgb"
mainLayout = QVBoxLayout()

if sys.platform == "win32":
    import ctypes
    FLID = u"flightlogger.0.0.1"  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(FLID)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.show()
        self.setLayout(mainLayout)
        self.setStyleSheet(CSSSTARTER + "(33, 33, 33)")
        self.showMaximized()
        self.setWindowTitle("Flight Logger")
        self.icon = QIcon("icon.png")
        self.setWindowIcon(self.icon)
        newEntryBtn = QPushButton()
        newEntryBtn.setGeometry(200, 200, 50, 25)
        newEntryBtn.setText("New Entry")
        newEntryBtn.setStyleSheet(CSSSTARTER + "(255, 255, 255)")


mainApplication = QApplication([])

mainWindow = MainWindow()
mainApplication.setWindowIcon(mainWindow.icon)

mainApplication.exec_()



