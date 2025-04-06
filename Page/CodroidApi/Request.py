from typing import Optional

from Request import *
from RequestData import *
import websocket
import threading
import time
# import asyncio
# import websockets


class Request:
    # _ws = CodroidApi.WebSocketApp
    def __init__(self, host: str, port: str, queueSize: int = 100):
        self._host: str = host
        self._port: str = port
        self._queueSize: int = queueSize
        self._id = 0
        self._lock = threading.Lock()
        self._requests: dict[int, RequestData] = dict()
        self._connected_event = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self.connect()
        self._running: bool = True
        self._timeout_thread = threading.Thread(target=self._check_timeout, daemon=True)
        self._timeout_thread.start()

    def __del__(self):
        self.close()

    def connect(self):
        # 内部函数，用于启动 WebSocket
        self._ws = websocket.WebSocketApp(
            f"ws://{self._host}:{self._port}",
            on_message=self.onRead,
            on_close=self.onClose,
            on_open=self.onOpen,
        )
        self._thread = threading.Thread(target=self._ws.run_forever, daemon=True)
        self._thread.start()

        # 等待连接完成
        if not self._connected_event.wait(timeout=15):
            print("Connection timeout")
        else:
            print("Connection established")

    def onOpen(self, _ws):
        print("Connection opened")
        self._connected_event.set()  # 连接成功，通知主线程

    def onRead(self, _ws, message: str):
        with self._lock:
            try:
                data: dict = json.loads(message)
                print("recived message: {}".format(json.dumps(data, indent=4)))
                id: int = data["id"]
                if id in self._requests:
                    self._requests[id].reply(json.dumps(data, indent=4))
                    self._requests.pop(id)
                else:
                    print("request is not exist by id: {}".format(id))
                    print("message: {}".format(message))
            except Exception as e:
                print("unknown message: {}".format(message))

    def onClose(self, _ws):
        print("CodroidApi is closed")
        self._connected_event.clear()  # 连接断开，清除通知

    def close(self):
        # 关闭 WebSocket 和停止线程
        self._running = False
        if self._ws:
            self._ws.close()
        if self._thread and self._thread.is_alive():
            self._thread.join()  # 等待线程退出
        if self._timeout_thread and self._timeout_thread.is_alive():
            self._timeout_thread.join()  # 等待线程退出
        print("WebSocket client stopped")

    def send(self, type: str, action: str, data: str, timeout: int = 30) -> Future:
        with self._lock:
            requestData: RequestData = RequestData()
            if len(self._requests) >= self._queueSize:
                requestData.error(ResponseCode.QueueFull, "queue is full")
                return requestData.future()

            if self._ws.sock is None:
                self.connect()

            if self._ws.sock is None:
                requestData.error(ResponseCode.NetError,
                                  "CodroidApi is not connected")
                return requestData.future()
            else:
                self._id += 1

                msg: str = json.dumps({
                    "id": self._id,
                    "type": type,
                    "action": action,
                    "data": json.loads(data)
                })

                print("send message: {}".format(json.loads(msg)))

                requestData.set(self._id, timeout)
                self._requests[self._id] = requestData

                self._ws.send(msg)

                return self._requests[self._id].future()

    def _check_timeout(self):
        while 1:
            with self._lock:
                timeoutIds: list[int] = []
                for id,request_data in self._requests.items():
                    if request_data._checkTimeout():
                        request_data.error(ResponseCode.Timeout, "timeout")
                        timeoutIds.append(id)

                for id in timeoutIds:
                    self._requests.pop(id)
            time.sleep(0.1)
