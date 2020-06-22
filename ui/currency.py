# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'currency.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class Ui_CurrencyWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 3, 2, 1, 1)
        self.buyAndSell = QtWidgets.QWidget(self.centralwidget)
        self.buyAndSell.setObjectName("buyAndSell")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.buyAndSell)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buyButton = QtWidgets.QPushButton(self.buyAndSell)
        self.buyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 85)")
        self.buyButton.setObjectName("buyButton")
        self.verticalLayout.addWidget(self.buyButton, 0, QtCore.Qt.AlignTop)
        self.sellButton = QtWidgets.QPushButton(self.buyAndSell)
        self.sellButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(206, 66, 66)")
        self.sellButton.setObjectName("sellButton")
        self.verticalLayout.addWidget(self.sellButton)
        self.gridLayout.addWidget(self.buyAndSell, 3, 0, 1, 1, QtCore.Qt.AlignTop)
        self.info = QtWidgets.QHBoxLayout()
        self.info.setContentsMargins(-1, 15, -1, -1)
        self.info.setObjectName("info")
        self.buyingPrice = QtWidgets.QLabel(self.centralwidget)
        self.buyingPrice.setObjectName("buyingPrice")
        self.info.addWidget(self.buyingPrice)
        self.sellingPrice = QtWidgets.QLabel(self.centralwidget)
        self.sellingPrice.setObjectName("sellingPrice")
        self.info.addWidget(self.sellingPrice)
        self.account = QtWidgets.QLabel(self.centralwidget)
        self.account.setObjectName("account")
        self.info.addWidget(self.account)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.info.addWidget(self.widget)
        self.gridLayout.addLayout(self.info, 1, 2, 1, 1)
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setObjectName("refreshButton")
        self.gridLayout.addWidget(self.refreshButton, 4, 2, 1, 1, QtCore.Qt.AlignLeft)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Валюта"))
        self.buyButton.setText(_translate("MainWindow", "Купить"))
        self.sellButton.setText(_translate("MainWindow", "Продать"))
        self.buyingPrice.setText(_translate("MainWindow", "Стоимость покупки: "))
        self.sellingPrice.setText(_translate("MainWindow", "Стоимость продажи: "))
        self.account.setText(_translate("MainWindow", "Ваш счёт: "))
        self.refreshButton.setText(_translate("MainWindow", "Обновить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CurrencyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
