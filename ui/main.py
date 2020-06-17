# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 523)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setObjectName("mainWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.mainWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QWidget(self.mainWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tableWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabs = QtWidgets.QTabWidget(self.tableWidget)
        self.tabs.setObjectName("tabs")
        self.allCurrenciesTab = QtWidgets.QWidget()
        self.allCurrenciesTab.setObjectName("allCurrenciesTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.allCurrenciesTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.allCurrenciesTable = QtWidgets.QTableWidget(self.allCurrenciesTab)
        self.allCurrenciesTable.setObjectName("allCurrenciesTable")
        self.allCurrenciesTable.setColumnCount(0)
        self.allCurrenciesTable.setRowCount(0)
        self.gridLayout_3.addWidget(self.allCurrenciesTable, 0, 0, 1, 1)
        self.tabs.addTab(self.allCurrenciesTab, "")
        self.myCurrenciesTab = QtWidgets.QWidget()
        self.myCurrenciesTab.setObjectName("myCurrenciesTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.myCurrenciesTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.myCurrenciesTable = QtWidgets.QTableWidget(self.myCurrenciesTab)
        self.myCurrenciesTable.setObjectName("myCurrenciesTable")
        self.myCurrenciesTable.setColumnCount(0)
        self.myCurrenciesTable.setRowCount(0)
        self.gridLayout_5.addWidget(self.myCurrenciesTable, 0, 0, 1, 1)
        self.tabs.addTab(self.myCurrenciesTab, "")
        self.operationsTab = QtWidgets.QWidget()
        self.operationsTab.setObjectName("operationsTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.operationsTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.operationsTable = QtWidgets.QTableWidget(self.operationsTab)
        self.operationsTable.setObjectName("operationsTable")
        self.operationsTable.setColumnCount(0)
        self.operationsTable.setRowCount(0)
        self.gridLayout_6.addWidget(self.operationsTable, 0, 0, 1, 1)
        self.tabs.addTab(self.operationsTab, "")
        self.gridLayout_2.addWidget(self.tabs, 1, 1, 1, 1)
        self.refreshButton = QtWidgets.QPushButton(self.tableWidget)
        self.refreshButton.setObjectName("refreshButton")
        self.gridLayout_2.addWidget(self.refreshButton, 3, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.searchWidget = QtWidgets.QWidget(self.mainWidget)
        self.searchWidget.setObjectName("searchWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.searchWidget)
        self.verticalLayout_3.setContentsMargins(-1, 45, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.search = QtWidgets.QLineEdit(self.searchWidget)
        self.search.setObjectName("search")
        self.verticalLayout_3.addWidget(self.search)
        self.searchButton = QtWidgets.QPushButton(self.searchWidget)
        self.searchButton.setObjectName("searchButton")
        self.verticalLayout_3.addWidget(self.searchButton)
        self.gridLayout.addWidget(self.searchWidget, 1, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Криптовалюты"))
        self.tabs.setTabText(self.tabs.indexOf(self.allCurrenciesTab), _translate("MainWindow", "Все валюты"))
        self.tabs.setTabText(self.tabs.indexOf(self.myCurrenciesTab), _translate("MainWindow", "Мои валюты"))
        self.tabs.setTabText(self.tabs.indexOf(self.operationsTab), _translate("MainWindow", "Операции"))
        self.refreshButton.setText(_translate("MainWindow", "Обновить"))
        self.search.setPlaceholderText(_translate("MainWindow", "Поиск..."))
        self.searchButton.setText(_translate("MainWindow", "Найти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())