from sys import argv

from PyQt5.QtWidgets import QApplication

from src.login_window import LoginForm


class Main:
    def __init__(self):
        self.loginForm = LoginForm()

    def launch(self):
        self.loginForm.init()


def main():
    app = QApplication(argv)
    main_ = Main()
    main_.launch()
    app.exec_()


if __name__ == '__main__':
    main()
