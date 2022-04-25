import sys
from requests import get
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
        self.radioButton_3.clicked.connect(self.s_p)
        self.search_button.clicked.connect(self.search)
        self.type_s_p = "map"

    def search(self):
        if self.search_text.toPlainText():
            response = get(
                f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={self.search_text.toPlainText()}1&format=json")
            if response:
                json_response = response.json()
                xy = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()
                print(xy)
                self.y_text.setPlainText(xy[1])
                self.x_text.setPlainText(xy[0])
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
            elif event.key() == Qt.Key_Down:
                self.y_text.setPlainText(str(float(self.y_text.toPlainText()) - 0.1))
            elif event.key() == Qt.Key_Right:
                self.x_text.setPlainText(str(float(self.x_text.toPlainText()) + 0.1))
            elif event.key() == Qt.Key_Left:
                self.x_text.setPlainText(str(float(self.x_text.toPlainText()) - 0.1))
        self.show_fun()

    def s_p(self):
        if self.sputnik.isChecked():
            self.type_s_p = "sat"
        if self.radioButton_2.isChecked():
            self.type_s_p = "map"
        if self.radioButton_3.isChecked():
            self.type_s_p = "sat,skl"
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
