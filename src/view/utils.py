from PyQt5.QtWidgets import QMessageBox


def show_error(message: str) -> None:
    QMessageBox(text=message).create(destroyOldWindow=False)
