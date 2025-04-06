class SocketFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建左侧菜单栏
        self.menu_frame = QWidget()
        menu_layout = QVBoxLayout(self.menu_frame)

        # IP 地址输入框
        ip_layout = QHBoxLayout()
        self.label_ip = QLabel("IP:")
        self.line_edit_ip = QLineEdit()
        ip_layout.addWidget(self.label_ip)
        ip_layout.addWidget(self.line_edit_ip)

        # 端口输入框
        port_layout = QHBoxLayout()
        self.label_port = QLabel("Port:")
        self.line_edit_port = QLineEdit()
        port_layout.addWidget(self.label_port)
        port_layout.addWidget(self.line_edit_port)

        # 客户端/服务端选择
        self.combo_mode = QComboBox()
        self.combo_mode.addItems(["Client", "Server"])

        # 连接按钮
        self.btn_socket_connect = QPushButton("Connect")
        self.btn_socket_disconnect = QPushButton("Disconnect")

        # 将组件添加到菜单布局中
        menu_layout.addLayout(ip_layout)
        menu_layout.addLayout(port_layout)
        menu_layout.addWidget(self.combo_mode)
        menu_layout.addWidget(self.btn_socket_connect)
        menu_layout.addWidget(self.btn_socket_disconnect)

        # 创建接收数据的 Frame
        self.recv_frame = QWidget()
        recv_layout = QVBoxLayout(self.recv_frame)
        self.text_edit_recv = QTextEdit()
        self.text_edit_recv.setReadOnly(True)
        recv_layout.addWidget(self.text_edit_recv)

        # 创建发送数据的 Frame
        self.send_frame = QWidget()
        send_layout = QVBoxLayout(self.send_frame)
        self.text_edit_send = QTextEdit()
        send_layout.addWidget(self.text_edit_send)

        # 发送按钮和定时发送选项
        send_options_layout = QHBoxLayout()
        self.btn_socket_send = QPushButton("Send")
        self.checkbox_timer_send = QCheckBox("Timer Send (ms)")
        self.line_edit_timer_interval = QLineEdit("1000")
        send_options_layout.addWidget(self.btn_socket_send)
        send_options_layout.addWidget(self.checkbox_timer_send)
        send_options_layout.addWidget(self.line_edit_timer_interval)

        send_layout.addLayout(send_options_layout)

        # 主布局
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.menu_frame)
        main_layout.addWidget(self.recv_frame)
        main_layout.addWidget(self.send_frame)
