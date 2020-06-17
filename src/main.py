from sys import argv

from PyQt5.QtWidgets import QApplication

from src.login_window import LoginForm
from src.main_window import MainWindow


class Main:
    def __init__(self):
        self.loginForm = LoginForm()

    def launch(self):
        self.loginForm.init()


if __name__ == '__main__':
    app = QApplication(argv)
    main = Main()
    main.launch()
    app.exec_()
