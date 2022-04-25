import sys

from PyQt5 import QtGui
from os import remove
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_qt import Ui_Form
from xz import show_image


# Создание главного стартового окна
class Main(QMainWindow, Ui_Form):
    # инициальзация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_button.clicked.connect(self.show_fun)
        self.sputnik.clicked.connect(self.s_p)
        self.radioButton_2.clicked.connect(self.s_p)
        self.type_s_p = "map"

    def show_fun(self):
        data = (str(self.x_text.toPlainText()), str(self.y_text.toPlainText()), str(self.scale_text.toPlainText()))
        show_image(data[0], data[1], (data[2], data[2]), self.type_s_p)
        self.pix = QtGui.QPixmap('out.jpg')
        self.pictureLabel.setPixmap(self.pix)
        remove("out.jpg")

    def keyPressEvent(self, event):
        if self.scale_text.toPlainText():
            if event.key() == Qt.Key_PageUp:
                self.scale_text.setPlainText(str(int(self.scale_text.toPlainText()) + 15))
            elif event.key() == Qt.Key_PageDown:
                self.scale_text.setPlainText(str(int(self.scale_text.toPlainText()) - 15))
            elif event.key() == Qt.Key_Up:
                self.y_text.setPlainText(str(float(self.y_text.toPlainText()) + 0.1))
                print(1)
            elif event.key() == Qt.Key_Down:
                self.y_text.setPlainText(str(float(self.y_text.toPlainText()) - 0.1))
            elif event.key() == Qt.Key_Up:
                self.x_text.setPlainText(str(float(self.x_text.toPlainText()) + 0.1))
                print(1)
            elif event.key() == Qt.Key_Down:
                self.x_text.setPlainText(str(float(self.x_text.toPlainText()) - 0.1))
        self.show_fun()

    def s_p(self):
        if self.sputnik.isChecked():
            self.type_s_p = "sat"
        if self.radioButton_2.isChecked():
            self.type_s_p = "map"
        self.show_fun()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# запуск
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
