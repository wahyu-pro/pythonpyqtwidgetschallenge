import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt

class WindowApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WindowApp, self).__init__(*args, **kwargs)
        self.mainWidget()
        # self.setLayout()
        self.setWidget()

    def mainWidget(self):
        # object combobox
        self.fetch = requests.get("https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json")
        self.respon = self.fetch.json()
        self.layout = QVBoxLayout()
        category = list(set(map(lambda a: a['category'],self.respon)))
        for kategori in category:
            cate = self.layout.addWidget(QLabel(kategori))
            var = kategori
            combo = QComboBox()
            self.layout.addWidget(combo)

            for i in range(len(self.respon)):
                if var == self.respon[i]['category']:
                    combo.addItem(self.respon[i]['name'])

        self.layout.addWidget(combo)

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
