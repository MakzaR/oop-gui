from PyQt5.QtWidgets import QMessageBox


def show_error(message: str) -> None:
    msg = QMessageBox()
    msg.setWindowTitle('Ошибка')
    msg.setText(message)

    msg.exec_()