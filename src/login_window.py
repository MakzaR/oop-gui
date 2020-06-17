from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMainWindow

from src.main_window import MainWindow
from ui.auth_form import Ui_AuthorizationForm


class LoginForm(Ui_AuthorizationForm, QMainWindow):
    def __init__(self):
        super().__init__(None, Qt.WindowCloseButtonHint)
        self.setupUi(self)

        self.confirmButton.clicked.connect(self.auth)
        self.cancelButton.clicked.connect(lambda: self.close())

        self.mainWindow = MainWindow(self)

    def init(self):
        self.show()

    def auth(self):
        self.close()
        self.mainWindow.show()