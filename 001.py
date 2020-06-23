import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt

class WindowApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WindowApp, self).__init__(*args, **kwargs)
        self.datalist = ["orange", "apple", "mango", "grape", "peach","watermelon"]
        self.dataRand = random.sample(self.datalist,len(self.datalist))
        self.mainWidget()
        self.setLayout()
        self.setWidget()

    def mainWidget(self):
        # object combobox
        self.comboBox = QComboBox()
        for i in self.dataRand:
            self.comboBox.addItem(i)

    def setLayout(self):
        # object layout 
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.comboBox)

    def setWidget(self):
        # object widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    app = QApplication([])
    window = WindowApp()
    window.show()
    app.exec_()
