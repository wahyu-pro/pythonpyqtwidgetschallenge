import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt

class WindowApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WindowApp, self).__init__(*args, **kwargs)
        self.label = Labels()
        self.mainWidget()
        self.setLayout()
        self.setWidget()

    def mainWidget(self):
        pass

    def setLayout(self):
        # object layout
        self.layout = QVBoxLayout()
        self.get = requests.get("https://jsonplaceholder.typicode.com/users")
        self.data = self.get.json()
        self.result = list(map(lambda a: "Nama : {}, alamat {}, {}, {} ".format(a['name'], a['address']['street'], a['address']['city'], a['address']['suite']), self.data))
        for i in self.result:
            self.layout.addWidget(self.label.addLabel(i))

    def setWidget(self):
        # object widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)


class Labels():
    def addLabel(self, text):
        self.label = QLabel(text)
        return self.label

if __name__ == "__main__":
    app = QApplication([])
    window = WindowApp()
    window.show()
    app.exec_()