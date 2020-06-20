from datetime import date
from decimal import Decimal

import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from src.view.buy_window import BuyWindow
from src.view.sell_wndow import SellWindow
from ui.currency import Ui_CurrencyWindow

selling_prices = [1.337, 1.488, 1.556, 1.246, 1.889]
buying_prices = [2.534, 2.679, 2.365, 2.456, 2.345]
time = [
    date(2020, 5, 1),
    date(2020, 5, 2),
    date(2020, 5, 3),
    date(2020, 5, 4),
    date(2020, 5, 5),
]

time_dict = dict(enumerate(time))


class CurrencyWindow(Ui_CurrencyWindow, QMainWindow):
    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)

        self.buyButton.clicked.connect(self.buy)
        self.sellButton.clicked.connect(self.sell)

        self.buy_window = BuyWindow(self)
        self.sell_window = SellWindow(self)

        self.set_text_info(selling_prices[-1], buying_prices[-1], Decimal('3.0012'))

    def set_text_info(self, selling_price, buying_price, account):
        self.buyingPrice.setText('Cтоимость покупки: ' + str(selling_price) + ' у.е.')
        self.sellingPrice.setText('Стоимость продажи: ' + str(buying_price) + ' у.е.')
        self.account.setText('На счёте: ' + str(account) + ' у.е.')

    def draw_graphs(self):
        pg.setConfigOptions(antialias=True)

        self.graphicsView.setBackground('w')

        self.graphicsView.addLegend()

        time_axis = pg.AxisItem(orientation='bottom')
        time_axis.setTicks([time_dict.items()])
        self.graphicsView.setAxisItems(axisItems={'bottom': time_axis})

        self.graphicsView.setLabel('left', 'Цена')
        self.graphicsView.setLabel('bottom', 'Время')

        self.graphicsView.showGrid(x=True, y=True)

        self.plot(
            list(time_dict.keys()),
            buying_prices,
            'Цена покупки',
            (0, 220, 0),
            1.5,
            'o',
            5,
        )

        self.plot(
            list(time_dict.keys()),
            selling_prices,
            'Цена продажи',
            (255, 0, 0),
            1.5,
            'o',
            5,
        )

    def plot(self, x, y, plot_name, color, width, symbol, symbol_size):
        pen = pg.mkPen(color=color, width=width)
        self.graphicsView.plot(
            x,
            y,
            name=plot_name,
            pen=pen,
            symbol=symbol,
            symbolSize=symbol_size,
            symbolBrush=color,
        )

    def buy(self):
        self.buy_window.init()

    def sell(self):

        self.sell_window.init()

    def init(self):
        self.draw_graphs()
        self.show()
