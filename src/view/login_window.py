from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox
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

    def init(self):
        self.show()

    """Тут нужно добавить валидацию, возможно добавить обработку исключений сервера"""

    def auth(self):
        self.close()
        try:
            user = self._authorize.sign_in(self.login.text())
            self.mainWindow = MainWindow(user, self)
            self.mainWindow.init()
        except ConnectionError:
            QMessageBox(text=Message.CONNECTION_ERROR.value).exec()
