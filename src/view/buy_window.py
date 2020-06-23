from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src.DAL.client import Client
from src.exceptions import DALError
from src.message import Message
from src.models.currency import UserCurrency
from src.models.operation import OperationType
from src.models.user import User
from ui.buy_window import Ui_BuyWindow
from decimal import Decimal
from requests.exceptions import ConnectionError

class BuyWindow(Ui_BuyWindow, QMainWindow):
    def __init__(self, parent, client: Client, user: User, currency: UserCurrency):
        super().__init__(parent, Qt.WindowCloseButtonHint)
        self.parent = parent
        self.setupUi(self)
        self._user: User = user
        self._client = client
        self._currency: UserCurrency = currency
        self.buyButton.clicked.connect(self.buy)
        self.cancelButton.clicked.connect(lambda: self.close())

    def buy(self):
        try:
            try:
                d = Decimal(self.amount.text())
            except Exception:
                raise DALError('Кол-во должно быть числом')
            try:
                self._client.make_operation(OperationType.BUY, self._user, self._currency, d)
                self.parent.refresh()
                self.close()
            except ConnectionError:
                QMessageBox().warning(self, 'Ошибка', str(Message.CONNECTION_ERROR.value))

        except DALError as e:
            QMessageBox().warning(self, 'Ошибка', str(e))


    def init(self):
        self.show()
