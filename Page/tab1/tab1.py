"""tab1.py"""

from PySide6.QtWidgets import QWidget, QVBoxLayout

from Page.tab1.ui.btn_frame import BtnFrame
from Page.tab1.ui.control_frame import ControlFrame
from Page.tab1.ui.ip_frame import IpFrame


class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        self.ip_frame = IpFrame()
        self.btn_frame = BtnFrame()
        self.control_frame = ControlFrame()
        self.init_tab_layout()

    def init_tab_ui(self):
        pass

    def init_tab_layout(self):
        self.tab1_ipframe_layout = QVBoxLayout(self)
        self.tab1_ipframe_layout.addWidget(self.ip_frame)
        self.tab1_ipframe_layout.addWidget(self.btn_frame)
        self.tab1_ipframe_layout.addWidget(self.control_frame)