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

    def set_img(self, cord1=2.312896, cord2=48.858631, Ddelta='0', delta='0.08'):
        self.cur_cords = [cord1, cord2]

        self.cur_delta = str(float(delta) + float(Ddelta))
        if float(self.cur_delta) < 0:
            self.cur_delta = str(float(self.cur_delta) - float(Ddelta))
        elif float(self.cur_delta) > 1:
            self.cur_delta = str(float(self.cur_delta) - float(Ddelta))

        show_find(cords=self.cur_cords, delta=self.cur_delta)
        self.pixmap = QPixmap.fromImage(QImage('pick_me.png'))
        self.map.setPixmap(self.pixmap)
        self.map.resize(500, 500)

    def find(self):
        self.set_img(cord1=self.cord_1.text(), cord2=self.cord_2.text(), delta=self.cur_delta)

    def resize_pict(self, Ddelta):
        print(Ddelta, 'Ddelta resize')
        self.set_img(cord1=self.cur_cords[0], cord2=self.cur_cords[1], delta=self.cur_delta, Ddelta=Ddelta)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_PageUp:
            self.resize_pict('-0.05')
        elif event.key() == Qt.Key.Key_PageDown:
            self.resize_pict('0.05')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniMaps()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
