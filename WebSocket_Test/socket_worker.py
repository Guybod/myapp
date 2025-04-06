import socket
from PySide6.QtCore import QObject, Signal, QThread

class SocketWorker(QObject):
    data_received = Signal(str)
    socket_tips_message = Signal(str)

    def __init__(self, mode, host, port):
        super().__init__()
        self.mode = None
        self.host = host
        self.port = port
        self.socket = None
        self.running = False

    def start_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")
        self.running = True
        while self.running:
            try:
                client_socket, addr = self.socket.accept()

                print(f"Connected by {addr}")
                self.handle_client(client_socket)
            except Exception as e:
                print(f"Error accepting connection: {e}")

    def handle_client(self, client_socket):
        while self.running:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"Received from client: {data}")
                client_socket.sendall(f"Server received: {data}".encode('utf-8'))
            except Exception as e:
                print(f"Error receiving data: {e}")
                break
        client_socket.close()

    def stop(self):
        self.running = False
        if self.socket:
            self.socket.close()