from PyQt6.QtWidgets import QMainWindow

from layout_parser import QtComponent


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lottery Machine")
        self.resize(1000, 600)
        self.component = QtComponent(self, "./assets/layout")
        self.show()
