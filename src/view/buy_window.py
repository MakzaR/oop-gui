from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from src.DAL.client import Client
from src.exceptions import DALError
from src.models.currency import UserCurrency
from src.models.operation import OperationType
from src.models.user import User
from src.view.utils import show_error
from ui.buy_window import Ui_BuyWindow
from decimal import Decimal

class BuyWindow(Ui_BuyWindow, QMainWindow):
    def __init__(self, parent, client: Client, user: User, currency: UserCurrency):
        super().__init__(parent, Qt.WindowCloseButtonHint)
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
            self._client.make_operation(OperationType.BUY, self._user, self._currency, d)
        except DALError as e:
            show_error(str(e))


    def init(self):
        self.show()
