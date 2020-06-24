import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt

class WindowApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WindowApp, self).__init__(*args, **kwargs)
        self.label = Labels()
        self.mainWidget()
        self.setWidget()

    def mainWidget(self):
        self.get_name = requests.get("https://randomuser.me/api/?results=10")
        self.get_name = self.get_name.json()
        self.get_data = self.get_name['results']
        self.result = list(map(lambda i: "{} {} {}".format(i['name']['title'], i['name']['first'], i['name']['last']), self.get_data))

        count = 0
        self.layout = QVBoxLayout()
        for i in self.result:
            count +=1
            self.check = "check_{}".format(count)
            self.check = QCheckBox(i)
            self.layout.addWidget(self.check)

    def setWidget(self):
        # object widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

class checkBoxs():
    def __init__(self, text):
        self.addCheckBox = QCheckBox(text)

class Labels():
    def addLabel(self, text):
        self.label = QLabel(text)
        return self.label

if __name__ == "__main__":
    app = QApplication([])
    window = WindowApp()
    window.show()
    app.exec_()