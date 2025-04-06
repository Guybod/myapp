"""SocketRecvFrame"""

from PySide6.QtWidgets import QPlainTextEdit, QHBoxLayout

from Page.base_ui.base_frame import BaseFrame


class SocketRecvFrame(BaseFrame):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def init_ui(self):
        self.edit_socket_recv = QPlainTextEdit()
        self.edit_socket_recv.setReadOnly(True)

    def init_layout(self):
        self.socket_recv_layout = QHBoxLayout(self)
        self.socket_recv_layout.addWidget(self.edit_socket_recv)
