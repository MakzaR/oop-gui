from datetime import datetime
from typing import List, Dict, Optional

import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from src.DAL.client import Client
from src.models.currency import CurrencyHistory, UserCurrency
from src.models.user import User
from src.view.buy_window import BuyWindow
from src.view.sell_wndow import SellWindow
from ui.currency import Ui_CurrencyWindow


# selling_prices = [1.337, 1.488, 1.556, 1.246, 1.889, 1.337, 1.488, 1.556, 1.246, 1.889, 1.556, 1.246, 1.889]
# purchasing_prices = [2.534, 2.679, 2.365, 2.456, 2.345, 2.534, 2.679, 2.365, 2.456, 2.345, 2.365, 2.456, 2.345]
# time = [
#     datetime(2020, 5, 1, 0, 0, 0, 111),
#     datetime(2020, 5, 2, 0, 0, 0),
#     datetime(2020, 5, 3, 0, 0, 0),
#     datetime(2020, 5, 4, 0, 0, 0),
#     datetime(2020, 5, 5, 0, 0, 0),
#     datetime(2020, 5, 7, 0, 0, 0),
#     datetime(2020, 5, 8, 0, 0, 0),
#     datetime(2020, 5, 9, 0, 0, 0),
#     datetime(2020, 5, 10, 0, 0, 0),
#     datetime(2020, 5, 11, 0, 0, 0),
#     datetime(2020, 5, 12, 0, 0, 0),
#     datetime(2020, 5, 13, 0, 0, 0),
#     datetime(2020, 5, 14, 0, 0, 0),
# ]
#
# time = dict(enumerate(time))


class CurrencyWindow(Ui_CurrencyWindow, QMainWindow):
    def __init__(self, parent, user: User, currency: UserCurrency):
        super().__init__(parent, Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)
        self.buyButton.clicked.connect(self.buy)
        self.sellButton.clicked.connect(self.sell)
        self._user: User = user
        self._currency: UserCurrency = currency
        self._client = Client()

    def set_text_info(self, selling_price, buying_price, account):
        self.buyingPrice.setText('Cтоимость покупки: ' + str(buying_price) + ' у.е.')
        self.sellingPrice.setText('Стоимость продажи: ' + str(selling_price) + ' у.е.')
        self.account.setText('На счёте: ' + str(account) + ' у.е.')

    def draw_graphs(self):
        pg.setConfigOptions(antialias=True)
        history_items: List[CurrencyHistory] = self._client.get_currency_history(self._currency.id)
        selling_prices = list(map(lambda item: float(item.selling_price), history_items))
        purchasing_prices = list(map(lambda item: float(item.purchasing_price), history_items))
        time = {}
        for i in range(len(history_items)):
            if i == 0 or i == len(history_items) - 1:
                time[i] = datetime.strftime(history_items[i].time, '%Y-%m-%d %H:%M:%S')
            else:
                time[i] = ''
        self.set_text_info(selling_prices[-1], purchasing_prices[-1], str(self._user.money))
        self.graphicsView.setBackground('w')

        self.graphicsView.addLegend()

        time_axis = pg.AxisItem(orientation='bottom')
        time_axis.setTicks([time.items()])
        self.graphicsView.setAxisItems(axisItems={'bottom': time_axis})

        self.graphicsView.setLabel('left', 'Цена')
        self.graphicsView.setLabel('bottom', 'Время')

        self.graphicsView.showGrid(x=True, y=True)

        self.plot(
            list(time.keys()),
            purchasing_prices,
            'Цена покупки',
            (0, 220, 0),
            1.5,
            'o',
            5,
        )

        self.plot(
            list(time.keys()),
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
        self.buy_window = BuyWindow(self,self._client, self._user, self._currency)
        self.buy_window.init()

    def sell(self):
        self.sell_window = SellWindow(self, self._client, self._user, self._currency)
        self.sell_window.init()

    def init(self):
        self.draw_graphs()
        self.show()
