from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage, QKeyEvent
import sys
from funcs import ll_cords, show_find


class MiniMaps(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.set_img()
        self.find_btn.clicked.connect(self.find)

    def set_img(self, cord1=2.312896, cord2=48.858631):
        cords = [cord1, cord2]
        show_find(cords=cords)
        self.pixmap = QPixmap.fromImage(QImage('pick_me.png'))
        self.map.setPixmap(self.pixmap)
        self.map.resize(500, 500)

    def find(self):
        self.set_img(self.cord_1.text(), self.cord_2.text())

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_PageUp:
            self.label.setText("Вы нажали PgUp")
        elif event.key() == Qt.Key_PageDown:
            self.label.setText("Вы нажали PgDown")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniMaps()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
