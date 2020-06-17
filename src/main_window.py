from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMainWindow

from ui.main import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)

    def init(self):
        self.show()
