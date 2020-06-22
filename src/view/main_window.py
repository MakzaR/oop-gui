from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTableWidgetItem
from requests.exceptions import ConnectionError

from src.DAL.client import Client
from src.message import Message
from src.models.currency import UserCurrency
from src.models.operation import OperationType
from src.models.user import User
from src.view.currency_window import CurrencyWindow
from src.view.utils import show_error
from ui.main import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, user: User, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)
        self.user: User = user

        self.searchButton.clicked.connect(self.search_item)
        self.refreshButton.clicked.connect(self.refresh_tables)
        self._client = Client()

    '''Логика кнопки поиска'''

    def search_item(self):
        pass

    '''Логика кнопки обновления'''

    def refresh_tables(self):
        self.init()

    '''Тут чистый треш, но я просто тестил заполнение данных'''

    def fill_all_currencies(self):
        self.allCurrenciesTable.clear()
        currencies = self._client.get_all_currencies()
        labels = ['Название', 'Цена продажи', 'Цена покупки', '']
        create_headers(self.allCurrenciesTable, labels)
        for i in currencies:
            detail_button = QPushButton('Подробнее')
            detail_button.clicked.connect(lambda a,i=i: self.show_details(self.user, UserCurrency(**i.dict())))
            row = self.allCurrenciesTable.rowCount()
            self.allCurrenciesTable.setRowCount(row + 1)

            self.allCurrenciesTable.setItem(row, 0, QTableWidgetItem(i.name))
            self.allCurrenciesTable.setItem(
                row, 1, QTableWidgetItem(str(i.selling_price))
            )
            self.allCurrenciesTable.setItem(
                row, 2, QTableWidgetItem(str(i.purchasing_price))
            )

            self.allCurrenciesTable.setCellWidget(row, 3, detail_button)

    def fill_my_currencies(self):
        self.myCurrenciesTable.clear()

        labels = ['Название', 'Колличество', 'Цена продажи', 'Цена покупки', '']
        create_headers(self.myCurrenciesTable, labels)
        currencies = self._client.get_user_currencies(self.user.id)
        for i in currencies:
            detail_button = QPushButton('Подробнее')
            detail_button.clicked.connect(lambda: self.show_details(self.user, i))
            row = self.myCurrenciesTable.rowCount()
            self.myCurrenciesTable.setRowCount(row + 1)

            self.myCurrenciesTable.setItem(row, 0, QTableWidgetItem(i.name))
            self.myCurrenciesTable.setItem(row, 1, QTableWidgetItem(str(i.amount)))
            self.myCurrenciesTable.setItem(
                row, 2, QTableWidgetItem(str(i.selling_price))
            )
            self.myCurrenciesTable.setItem(
                row, 3, QTableWidgetItem(str(i.purchasing_price))
            )

            self.myCurrenciesTable.setCellWidget(row, 4, detail_button)

    def fill_operations(self):
        self.operationsTable.clear()
        labels = ['Операция', 'Название', 'Количество']
        create_headers(self.operationsTable, labels)
        operations = self._client.get_operations(self.user.id)
        for i in operations:
            row = self.operationsTable.rowCount()
            self.operationsTable.setRowCount(row + 1)
            self.operationsTable.setItem(
                row,
                0,
                QTableWidgetItem(
                    'Покупка' if i.operation_type == OperationType.BUY else 'Продажа'
                ),
            )
            self.operationsTable.setItem(row, 1, QTableWidgetItem(i.currency_name))
            self.operationsTable.setItem(row, 2, QTableWidgetItem((str(i.amount))))

    '''Логика кнопки "Подробнее"'''

    def show_details(self, user: User, currency: UserCurrency):
        CurrencyWindow(self, user, currency).init()

    def init(self):
        self.operationsTable.setRowCount(0)
        self.allCurrenciesTable.setRowCount(0)
        self.myCurrenciesTable.setRowCount(0)
        self.user = self._client.sign_in(self.user.login)
        try:
            self.fill_all_currencies()
            self.fill_my_currencies()
            self.fill_operations()
        except ConnectionError:
            show_error(Message.CONNECTION_ERROR.value)
            return
        self.show()


def create_headers(table_name, labels):
    table_name.setColumnCount(len(labels))
    table_name.setHorizontalHeaderLabels(labels)

    header = table_name.horizontalHeader()

    for i in range(len(labels)):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
