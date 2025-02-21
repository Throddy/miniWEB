from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import sys


class MiniMaps(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)

        self.find_btn.clicked.connect(self.find)

    def find(self):
        ...


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniMaps()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
