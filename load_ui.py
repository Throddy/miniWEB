from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QImage
import sys
from funcs import ll_cords, show_find


class MiniMaps(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)

        self.find_btn.clicked.connect(self.find)
        show_find(cords1=54.9557386, cords2=20.2436099)
        self.pixmap = QPixmap.fromImage(QImage('pick_me.png'))
        self.map.setPixmap(self.pixmap)
        self.map.resize(500, 500)


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
