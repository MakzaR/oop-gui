from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from ui.currency import Ui_CurrencyWindow


class CurrencyWindow(Ui_CurrencyWindow, QMainWindow):
    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)

        self.buyButton.clicked.connect(self.buy)
        self.sellButton.clicked.connect(self.sell)

    def buy(self):
        pass

    def sell(self):
        pass

    def init(self):
        self.show()
