import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import interface
from pygame import mixer
from currency_converter import CurrencyConverter
from converter import Ui_MainWindow


# class CurrencyConv(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(CurrencyConv, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.init_UI()
#         self.ui.inputCur.setPlaceholderText('Из валюты')
#         self.ui.inputSum.setPlaceholderText('Сколько')
#         self.ui.outputCur.setPlaceholderText('В валюту')
#         self.ui.outputSum.setPlaceholderText('Итого')
#
#     def converter(self):
#         c = CurrencyConverter()
#         inputCur = self.ui.inputCur.text()
#         outputCur = self.ui.outputCur.text()
#         inputSum = int(self.ui.inputSum.text())
#         outputSum = round(c.convert(inputSum, '%s' %  (inputCur), '%s' %(outputCur)), 2)
#         self.ui.outputSum.setText(str(outputSum))
#         self.ui.Convert.clicked.connect(self.converter)
#
#     def init_UI(self):
#         self.setWindowTitle('Конвертер валют')
#         self.ui.Convert.clicked.connect(self.converter)
#
#
# app = QtWidgets.QApplication([])
# application = CurrencyConv()
# application.show()
#
# sys.exit(app.exec())

class Player(QWidget, interface.Ui_Form):

    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Player')
        self.setFixedSize(self.size())

        self.play_sound_btn.clicked.connect(self.play_sound)
        self.prev_sound_btn.clicked.connect(self.prev_sound)
        self.next_sound_btn.clicked.connect(self.next_sound)
        self.add_sound_btn.clicked.connect(self.add_sound)
        self.remove_sound_btn.clicked.connect(self.remove_sound)

        self.listWidget.doubleClicked.connect(self.play_sound)

        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.volume_reg)

        self.dir = ""
        self.sound_mixer = mixer
        self.sound_mixer.init()

    def play_sound(self):
        item = self.listWidget.currentItem()

        if item:
            filename = os.path.join(self.dir, item.text())
            self.sound_mixer.music.load(filename)
        else:
            self.listWidget.currentRow(0)
        self.sound_mixer.music.play()

    def remove_sound(self):
        self.listWidget.clear()
        self.sound_mixer.music.stop()

    def prev_sound(self):
        try:
            row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(row - 1)
            self.play_sound()
        except TypeError:
            pass

    def next_sound(self):
        try:
            row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(row + 1)
            self.play_sound()
        except TypeError:
            pass

    def add_sound(self):
        self.listWidget.clear()

        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if dir:
            for filename in os.listdir(dir):
                if filename.endswith(".wav"):
                    self.listWidget.addItem(os.path.join(filename))
            self.dir = dir

    def volume_reg(self):
        self.sound_mixer.music.set_volume(self.volume_slider.value() / 100)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()