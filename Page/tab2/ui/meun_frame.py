"""MenuFrame"""
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QFrame, \
    QVBoxLayout, QComboBox

from Page.base_ui.base_frame import BaseFrame
from Page.style.style import Style


class MenuFrame(BaseFrame):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.set_style()

    def init_ui(self):
        # IP 地址输入框
        self.label_ip = QLabel("IP:")
        self.line_edit_ip = QLineEdit()

        # 端口输入框
        self.label_port = QLabel("Port:")
        self.line_edit_port = QLineEdit()

        # 客户端/服务端选择
        self.combo_mode = QComboBox()
        self.combo_mode.addItems(["服务端", "客户端"])

        # 连接按钮
        self.btn_socket_connect = QPushButton("连接")
        self.btn_socket_disconnect = QPushButton("断开连接")

    def init_layout(self):
        self.menu_layout = QVBoxLayout(self)

        # IP 地址输入框
        self.ip_layout = QHBoxLayout()
        self.ip_layout.addWidget(self.label_ip)
        self.ip_layout.addWidget(self.line_edit_ip)

        # 端口输入框
        self.port_layout = QHBoxLayout()
        self.port_layout.addWidget(self.label_port)
        self.port_layout.addWidget(self.line_edit_port)

        # 按钮布局
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.btn_socket_connect)
        self.button_layout.addWidget(self.btn_socket_disconnect)

        # 将组件添加到菜单布局中
        self.menu_layout.addLayout(self.ip_layout)
        self.menu_layout.addLayout(self.port_layout)
        self.menu_layout.addWidget(self.combo_mode)
        self.menu_layout.addLayout(self.button_layout)

    def set_style(self):
        self.style = Style()
        self.style.set_line_edit_style(self.line_edit_ip, 160, 30)
        self.style.set_line_edit_style(self.line_edit_port, 160, 30)
        # self.line_edit_ip.setPlaceholderText("127.0.0.1")
        # self.line_edit_port.setPlaceholderText("8080")
        self.line_edit_ip.setText("127.0.0.1")
        self.line_edit_port.setText("8080")
        self.style.set_btn_style(self.btn_socket_connect)
        self.style.set_btn_style(self.btn_socket_disconnect)
