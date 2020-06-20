from typing import NamedTuple

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTableWidgetItem

from src.DAL.client import Client
from src.models.user import User
from src.view.currency_window import CurrencyWindow
from ui.main import Ui_MainWindow




class OperationData(NamedTuple):
    type: str
    name: str
    amount: int
    account: str




operation_data = [
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
    OperationData('Продажа', 'Биток', 20, '+ 20 у. е.'),
]


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, user: User,parent):
        super().__init__(parent, Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)
        self.user: User = user

        self.searchButton.clicked.connect(self.search_item)
        self.refreshButton.clicked.connect(self.refresh_tables)

        self.currencyWindow = CurrencyWindow(self)
        self._client = Client()

    '''Логика кнопки поиска'''

    def search_item(self):
        pass

    '''Логика кнопки обновления'''

    def refresh_tables(self):
        pass

    '''Тут чистый треш, но я просто тестил заполнение данных'''

    def fill_all_currencies(self):
        self.allCurrenciesTable.clear()
        currencies = self._client.get_all_currencies()
        labels = ['Название', 'Цена продажи', 'Цена покупки', '']
        create_headers(self.allCurrenciesTable, labels)

        for i in currencies:
            detail_button = QPushButton('Подробнее')
            detail_button.clicked.connect(self.show_details)

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
            detail_button.clicked.connect(self.show_details)

            row = self.myCurrenciesTable.rowCount()
            self.myCurrenciesTable.setRowCount(row + 1)

            self.myCurrenciesTable.setItem(row, 0, QTableWidgetItem(i.name))
            self.myCurrenciesTable.setItem(row, 1, QTableWidgetItem(str(i.amount)))
            self.myCurrenciesTable.setItem(row, 2, QTableWidgetItem(str(i.selling_price)))
            self.myCurrenciesTable.setItem(row, 3, QTableWidgetItem(str(i.purchasing_price)))

            self.myCurrenciesTable.setCellWidget(row, 4, detail_button)

    def fill_operations(self):
        self.operationsTable.clear()
        labels = ['Операция', 'Название', 'Количество', 'Счёт']
        create_headers(self.operationsTable, labels)

        for i in operation_data:
            row = self.operationsTable.rowCount()
            self.operationsTable.setRowCount(row + 1)

            self.operationsTable.setItem(row, 0, QTableWidgetItem(i.type))
            self.operationsTable.setItem(row, 1, QTableWidgetItem(i.name))
            self.operationsTable.setItem(row, 2, QTableWidgetItem(str(i.amount)))
            self.operationsTable.setItem(row, 3, QTableWidgetItem(i.account))

    '''Логика кнопки "Подробнее"'''

    def show_details(self):
        self.currencyWindow.init()

    def init(self):
        self.fill_all_currencies()
        self.fill_my_currencies()
        self.fill_operations()
        self.show()


def create_headers(table_name, labels):
    table_name.setColumnCount(len(labels))
    table_name.setHorizontalHeaderLabels(labels)

    header = table_name.horizontalHeader()

    for i in range(len(labels)):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
