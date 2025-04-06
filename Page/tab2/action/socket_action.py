import socket
from PySide6.QtCore import QObject, Signal, QThread, QTimer

from Page.utils.get_time import GetTime


class SocketAction(QObject):

    is_listening = Signal(str)
    client_connected = Signal(str)
    recv_data = Signal(str)
    finished = Signal()


    def __init__(self, mode, host, port, /):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        self.client_socket = None
        self.client_ip = None
        self.client_port = None


    def start_server(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            self.is_listening.emit(f"服务端已开启 监听端口:{self.port}")
            # print(f"Server listening on {self.host}:{self.port}")
            self.running = True
            while self.running:
                try:
                    client_socket, addr = self.socket.accept()
                    self.client_ip,  self.client_port = addr
                    self.client_socket = client_socket  # 更新客户端套接字
                    self.client_connected.emit(f"已连接客户端 {self.client_ip}")
                    # print(f"Connected by {addr}")
                    self.handle_client(client_socket)
                except Exception as e:
                    self.client_connected.emit(f"Error accepting connection: {e}")
                    # print(f"Error accepting connection: {e}")
        finally:
            self.finished.emit()
            if self.socket:
                self.socket.close()

    def handle_client(self, client_socket):
        try:
            while self.running:
                try:
                    data = client_socket.recv(1024).decode('utf-8')
                    if not data:
                        break
                    self.recv_data.emit(f"[{GetTime.get_time()}] {self.client_ip}: {data}")
                    # print(f"Received from client: {data}")
                    # client_socket.sendall(f"Server received: {data}".encode('utf-8'))
                except Exception as e:
                    self.recv_data.emit(f"[{GetTime.get_time()}] 数据返回错误: {e}")
                    # print(f"Error receiving data: {e}")
                    break
        finally:
            client_socket.close()
            self.client_socket = None  # 清除客户端套接字
            self.client_addr = None

    def send_data(self, client_socket, message:str):
        try:
            client_socket.sendall(message.encode('utf-8'))
        except Exception as e:
            self.recv_data.emit(f"[{GetTime.get_time()}] 发送数据错误: {e}")

    def stop(self):
        self.running = False
        if self.socket:
            self.socket.close()
