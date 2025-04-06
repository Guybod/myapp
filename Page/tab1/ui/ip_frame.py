"""ip_frame.py"""
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QFrame

from Page.base_ui.base_frame import BaseFrame
from Page.style.style import Style


class IpFrame(BaseFrame):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.size = QSize()
        self.setBaseSize(self.size)
        self.set_style()


    def init_ui(self):
        self.label_ip = QLabel("ip:", self)
        self.edit_ip = QLineEdit(self)
        self.btn_robot_connect = QPushButton("连接", self)
        # self.HSpacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.label_robot_state = QLabel("未连接", self)


    def init_layout(self):
        self.ip_layout = QHBoxLayout(self)
        self.ip_layout.setSpacing(0)  # 设置 QFrame 内部布局的间距为 0
        self.ip_layout.setContentsMargins(0, 0, 0, 0)
        self.ip_layout.addWidget(self.label_ip)
        self.ip_layout.addWidget(self.edit_ip)
        self.ip_layout.addWidget(self.btn_robot_connect)
        # self.ip_layout.addItem(self.HSpacerItem)
        self.ip_layout.addWidget(self.label_robot_state)

    def set_style(self):
        self.style = Style()
        self.style.set_btn_style(self.btn_robot_connect)
        self.style.set_line_edit_style(self.edit_ip)
        self.edit_ip.setPlaceholderText("192.168.101.100")
        self.style.set_qlabel_style(self.label_ip, width=60, font_size=14, bold=True, alignment="left")
        self.style.set_qlabel_style(self.label_robot_state, font_size=14, bold=True, alignment="left")
