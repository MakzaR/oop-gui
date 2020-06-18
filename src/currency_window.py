from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow,
)

from ui.currency import Ui_CurrencyWindow


class CurrencyWindow(Ui_CurrencyWindow, QMainWindow):
    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)

    def init(self):
        self.show()
