from PySide6.QtCore import QThread, Signal

from Page.tab2.action.socket_action import SocketAction
from Page.tab2.ui.tab2 import Tab2


class Tab2Action(Tab2):
    def __init__(self):
        super().__init__()
        self.socket_worker = None
        self.server_thread = None
        self.bind()

    def bind(self):
        self.menu_frame.combo_mode.currentIndexChanged.connect(self.update_line_edit)
        self.menu_frame.btn_socket_connect.clicked.connect(self.on_start_server)
        if self.socket_worker:
            self.socket_worker.is_listening.connect(self.on_is_listening)
            self.socket_worker.client_connected.connect(self.on_client_connected)
            self.socket_worker.recv_data.connect(self.on_recv_data)
    
    def on_start_server(self):
        if not self.socket_worker or not self.socket_worker.running:
            self.socket_worker = SocketAction(None, self.menu_frame.line_edit_ip.text(), int(self.menu_frame.line_edit_port.text()))
            self.server_thread = QThread()
            self.socket_worker.moveToThread(self.server_thread)
            self.server_thread.started.connect(self.socket_worker.start_server)
            self.socket_worker.finished.connect(self.server_thread.quit)
            self.socket_worker.finished.connect(self.socket_worker.deleteLater)
            self.server_thread.finished.connect(self.server_thread.deleteLater)

            self.socket_worker.is_listening.connect(self.on_is_listening)
            self.socket_worker.client_connected.connect(self.on_client_connected)
            self.socket_worker.recv_data.connect(self.on_recv_data)

            self.server_thread.start()

    def on_is_listening(self, message):
        self.socket_recv_frame.edit_socket_recv.appendPlainText(message)  # 更新UI元素以显示消息

    def on_client_connected(self, message):
        self.socket_recv_frame.edit_socket_recv.appendPlainText(message)  # 更新UI元素以显示消息

    def on_recv_data(self, message):
        self.socket_recv_frame.edit_socket_recv.appendPlainText(message)  # 更新UI元素以显示消息

    def update_line_edit(self):
        if self.menu_frame.combo_mode.currentIndex() == 0:
            self.menu_frame.line_edit_ip.setPlaceholderText("127.0.0.1")
            self.menu_frame.line_edit_port.setPlaceholderText("8080")
        if self.menu_frame.combo_mode.currentIndex() == 1:
            self.menu_frame.line_edit_ip.setPlaceholderText("192.168.1.1")
            self.menu_frame.line_edit_port.setPlaceholderText("8080")