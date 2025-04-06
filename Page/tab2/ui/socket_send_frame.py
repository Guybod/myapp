"""SocketSendFrame"""
from PySide6.QtWidgets import QPlainTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QLineEdit

from Page.base_ui.base_frame import BaseFrame
from Page.style.style import Style


class SocketSendFrame(BaseFrame):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.set_style()

    def init_ui(self):
        self.edit_socket_send = QPlainTextEdit()
        self.btn_socket_send = QPushButton("发送")
        self.checkbox_timer_send = QCheckBox("定时发送(ms)")
        self.line_edit_timer_interval = QLineEdit("1000")

    def init_layout(self):
        self.socket_send_layout = QVBoxLayout(self)
        self.socket_send_option_layout = QHBoxLayout()
        self.socket_send_layout.addWidget(self.edit_socket_send)

        self.socket_send_option_layout.addWidget(self.btn_socket_send)
        self.socket_send_option_layout.addWidget(self.checkbox_timer_send)
        self.socket_send_option_layout.addWidget(self.line_edit_timer_interval)

        self.socket_send_layout.addLayout(self.socket_send_option_layout)

    def set_style(self):
        pass