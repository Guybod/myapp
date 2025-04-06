"""MainApp"""

from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout

from Page.tab1.action.tab1_action import Tab1Action
from Page.tab2.action.tab2_action import Tab2Action


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tab1 = Tab1Action()
        self.tab2 = Tab2Action()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.center_layout = QVBoxLayout(self.central_widget)

        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(self.tab1, "基础")
        self.tab_widget.addTab(self.tab2, "socket")

        self.center_layout.addWidget(self.tab_widget)
