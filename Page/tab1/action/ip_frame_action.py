from PySide6.QtCore import Signal

from Page.tab1.ui.ip_frame import IpFrame


class IpFrameAction(IpFrame):
    btn_robot_connect_clicked = Signal(str)

    def __init__(self):
        super().__init__()
        self.bind()

    def bind(self):
        self.btn_robot_connect.clicked.connect(self.btn_robot_connect_callback)

    def btn_robot_connect_callback(self):
        data = "已连接！"
        self.btn_robot_connect_clicked.emit(data)