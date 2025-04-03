"""main_app.py"""

from PySide6.QtWidgets import QMainWindow

from Page.tab1.tab1 import Tab1


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tab1 = Tab1()
        self.setCentralWidget(self.tab1)
