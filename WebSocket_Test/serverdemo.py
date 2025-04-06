import socket
import threading
import time

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False

    def start(self):
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

if __name__ == '__main__':
    server = Server("127.0.0.1", 8080)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # 保持服务器运行一段时间
    time.sleep(30)

    # 停止服务器
    server.stop()
    server_thread.join()