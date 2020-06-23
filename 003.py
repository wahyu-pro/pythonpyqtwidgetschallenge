import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt


class WindowApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WindowApp, self).__init__(*args, **kwargs)
        # self.label = Labels()
        self.mainWidget()
        self.setLayout()
        self.setWidget()

    def mainWidget(self):
        # object combobox
        self.comboBox = QComboBox()
        self.fetch = requests.get("https://randomuser.me/api/?results=10")
        self.respon = self.fetch.json()['results']
        self.respon = [self.respon[i]['gender'] for i in range(len(self.respon))]
        self.respon = list(set(self.respon))
        for x in self.respon:
            self.comboBox.addItem(x)

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