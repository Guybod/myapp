"""Tab1"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit, QFrame, QHBoxLayout

from Page.tab1.action.btn_frame_action import BtnFrameAction
from Page.tab1.action.ip_frame_action import IpFrameAction
from Page.tab1.ui.control_frame import ControlFrame


class Tab1(QWidget):
    def __init__(self):
        super().__init__()

        self.init_tab_ui()
        self.init_tab_layout()

    def init_tab_ui(self):
        self.ip_frame = IpFrameAction()
        self.btn_frame = BtnFrameAction()
        self.control_frame = ControlFrame()
        self.log_edit = QPlainTextEdit()
        self.log_edit.setReadOnly(True)
        self.bottom_frame = QFrame()

    def init_tab_layout(self):
        # 创建底部框架
        self.bottom_frame_layout = QHBoxLayout()
        self.bottom_frame.setLayout(self.bottom_frame_layout)
        self.bottom_frame_layout.addWidget(self.log_edit)
        self.bottom_frame_layout.addWidget(self.control_frame)
        # 设置主布局
        self.tab1_frame_layout = QVBoxLayout(self)
        self.tab1_frame_layout.addWidget(self.ip_frame)
        self.tab1_frame_layout.addWidget(self.btn_frame)
        self.tab1_frame_layout.addWidget(self.bottom_frame)

