from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel


class StartApp(QMainWindow):
    def __init__(self):
        super(StartApp, self).__init__()
        self.setGeometry(200, 2000, 300, 300)
        self.setWindowTitle("Lista zadań")
        self.set_up_ui()

    def set_up_ui(self):
        self.text = QLabel(self)
        self.text.setText("Some text")
        self.text.move(50, 50)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('BUtton')
        self.btn1.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.text.setText('Clicked')
