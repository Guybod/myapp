from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from Page.tab2.ui.meun_frame import MenuFrame
from Page.tab2.ui.socket_recv_frame import SocketRecvFrame
from Page.tab2.ui.socket_send_frame import SocketSendFrame


class Tab2(QWidget):
    def __init__(self):
        super().__init__()

        self.init_tab_ui()
        self.init_tab_layout()

    def init_tab_ui(self):
        self.menu_frame = MenuFrame()
        self.socket_recv_frame = SocketRecvFrame()
        self.socket_send_frame = SocketSendFrame()


    def init_tab_layout(self):
        self.tab2_frame_layout = QHBoxLayout(self)
        self.text_frame_layout = QVBoxLayout()

        self.tab2_frame_layout.addWidget(self.menu_frame)
        self.text_frame_layout.addWidget(self.socket_recv_frame)
        self.text_frame_layout.addWidget(self.socket_send_frame)

        self.tab2_frame_layout.addLayout(self.text_frame_layout)

        self.tab2_frame_layout.setStretchFactor(self.menu_frame,2)
        self.tab2_frame_layout.setStretchFactor(self.text_frame_layout,15)
