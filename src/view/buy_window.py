from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from ui.buy_window import Ui_BuyWindow


class BuyWindow(Ui_BuyWindow, QMainWindow):
    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint)
        self.setupUi(self)

        self.buyButton.clicked.connect(self.buy)
        self.cancelButton.clicked.connect(lambda: self.close())

    def buy(self):
        pass

    def init(self):
        self.show()
