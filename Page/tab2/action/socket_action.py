import socket
from PySide6.QtCore import QObject, Signal, QThread, QTimer

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

    def start_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.is_listening.emit(f"Server listening on {self.host}:{self.port}")
        # print(f"Server listening on {self.host}:{self.port}")
        self.running = True
        while self.running:
            try:
                client_socket, addr = self.socket.accept()
                self.client_connected.emit(f"Connected by {addr}")
                # print(f"Connected by {addr}")
                self.handle_client(client_socket)
            except Exception as e:
                self.client_connected.emit(f"Error accepting connection: {e}")
                # print(f"Error accepting connection: {e}")
        self.finished.emit()

    def handle_client(self, client_socket):
        while self.running:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                self.recv_data.emit(f"Received from client: {data}")
                # print(f"Received from client: {data}")
                client_socket.sendall(f"Server received: {data}".encode('utf-8'))
            except Exception as e:
                self.recv_data.emit(f"Error receiving data: {e}")
                # print(f"Error receiving data: {e}")
                break
        client_socket.close()

    def send_data(self, client_socket, message:str):
        client_socket.sendall(message.encode('utf-8'))


    def stop(self):
        self.running = False
        if self.socket:
            self.socket.close()
