import socket
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

    def send_message(self, message):
        self.socket.sendall(message.encode('utf-8'))
        response = self.socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

    def close(self):
        if self.socket:
            self.socket.close()

if __name__ == '__main__':
    client = Client("127.0.0.1", 8080)
    client.connect()
    time.sleep(1)
    # 模拟发送消息
    client.send_message("Hello, Server!")
    client.send_message("This is a test message.")
    time.sleep(5)

    # 关闭客户端
    client.close()