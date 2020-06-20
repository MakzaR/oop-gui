from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from ui.sell_window import Ui_SellWindow


class SellWindow(Ui_SellWindow, QMainWindow):
    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint)
        self.setupUi(self)

        self.buyButton.clicked.connect(self.sell)
        self.cancelButton.clicked.connect(lambda: self.close())

    def sell(self):
        pass

    def init(self):
        self.show()
