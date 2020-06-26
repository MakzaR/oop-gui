from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QMessageBox
from requests.exceptions import ConnectionError

from src.DAL.client import Client
from src.message import Message
from src.view.main_window import MainWindow
from ui.auth_form import Ui_AuthorizationForm


class LoginForm(Ui_AuthorizationForm, QMainWindow):
    def __init__(self):
        super().__init__(None, Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self._authorize: Client = Client()
        self.confirmButton.clicked.connect(self.auth)
        self.cancelButton.clicked.connect(lambda: self.close())

    def auth(self):
        self.close()
        try:
            text = self.login.text()
            if text:
                user = self._authorize.sign_in(text)
            else:
                QMessageBox().warning(self, 'Ошибка', 'Неверные данные')
                return
        except ConnectionError:
            QMessageBox().warning(self, 'Ошибка', Message.CONNECTION_ERROR.value)
            return
        self.mainWindow = MainWindow(user, self)
        self.mainWindow.init()

    def center(self):
        frame = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()

        frame.moveCenter(center_point)
        self.move(frame.topLeft())

    def init(self):
        self.center()
        self.show()
