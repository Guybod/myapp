import asyncio
import websockets
import json

url = "ws://192.168.101.100:9000"
json_data = {
    "id": 1,
    "type": "common",
    "action": "getparam",
    "data": [
        "Robot/Control/state"
    ]
}

class CodroidWebSocket:
    def __init__(self, url):
        self.url = url
        self.websocket = None

    async def connect(self):
        """连接到 WebSocket 服务器"""
        try:
            self.websocket = await websockets.connect(self.url)
            print(f"Connected to {self.url}")
        except Exception as e:
            print(f"Failed to connect to {self.url}: {e}")
            raise

    async def send_json(self, data):
        """发送 JSON 数据"""
        if not self.websocket:
            raise ValueError("WebSocket is not connected. Call connect() first.")
        try:
            await self.websocket.send(json.dumps(data))
            print("Sent JSON data to the server")
        except Exception as e:
            print(f"Failed to send data: {e}")
            raise

    async def receive_response(self):
        """接收服务器的响应"""
        if not self.websocket:
            raise ValueError("WebSocket is not connected. Call connect() first.")
        try:
            response = await self.websocket.recv()
            print("Received response from the server:")
            print(response)
            return response
        except Exception as e:
            print(f"Failed to receive response: {e}")
            raise

    async def close(self):
        """关闭 WebSocket 连接"""
        if self.websocket:
            await self.websocket.close()
            print("WebSocket connection closed")

    async def send_and_receive(self, data):
        """发送数据并接收响应"""
        await self.connect()
        await self.send_json(data)
        response = await self.receive_response()
        await self.close()
        return response

# 使用示例
if __name__ == "__main__":
    async def main():
        ws = CodroidWebSocket(url)
        response = await ws.send_and_receive(json_data)

    asyncio.run(main())