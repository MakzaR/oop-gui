from decimal import Decimal

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QMessageBox
from requests.exceptions import ConnectionError

from src.DAL.client import Client
from src.exceptions import DALError
from src.message import Message
from src.models.currency import UserCurrency
from src.models.operation import OperationType
from src.models.user import User
from ui.sell_window import Ui_SellWindow


class SellWindow(Ui_SellWindow, QMainWindow):
    def __init__(self, parent, client: Client, user: User, currency: UserCurrency):
        super().__init__(parent, Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.parent = parent
        self._user: User = user
        self._client = client
        self._currency: UserCurrency = currency
        self.sellButton.clicked.connect(self.sell)
        self.cancelButton.clicked.connect(self.close)

    def sell(self):
        try:
            try:
                d = Decimal(self.amount.text())
            except Exception:
                raise DALError('Кол-во должно быть числом')
            try:
                self._client.make_operation(
                    OperationType.SELL, self._user, self._currency, d
                )
            except ConnectionError:
                QMessageBox().warning(
                    self, 'Ошибка', str(Message.CONNECTION_ERROR.value)
                )
            self.parent.refresh()
            self.close()
        except DALError as e:
            QMessageBox().warning(self, 'Ошибка', str(e))

    def center(self):
        frame = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()

        frame.moveCenter(center_point)
        self.move(frame.topLeft())

    def init(self):
        self.center()
        self.show()
