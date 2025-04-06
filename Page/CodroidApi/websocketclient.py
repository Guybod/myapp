import asyncio
import websockets


class WebSocketClient:
    def __init__(self, uri, on_open=None, on_message=None, on_close=None):
        self.uri = uri
        self.on_open = on_open
        self.on_message = on_message
        self.on_close = on_close
        self.websocket = None
        self.connected = False

    async def connect(self):
        try:
            self.websocket = await websockets.connect(self.uri)
            self.connected = True

            # Trigger the `on_open` callback
            if self.on_open:
                await self.on_open(self)

            # Start listening for messages
            await self.listen()
        except Exception as e:
            print(f"Connection error: {e}")
            self.connected = False
            if self.on_close:
                await self.on_close(self, e)

    async def listen(self):
        try:
            async for message in self.websocket:
                # Trigger the `on_message` callback
                if self.on_message:
                    await self.on_message(self, message)
        except websockets.exceptions.ConnectionClosed as e:
            print(f"Connection closed: {e}")
            self.connected = False
            if self.on_close:
                await self.on_close(self, e)

    async def send(self, message):
        if self.connected and self.websocket:
            await self.websocket.send(message)

    async def close(self):
        if self.websocket:
            await self.websocket.close()
            self.connected = False
            if self.on_close:
                await self.on_close(self, None)