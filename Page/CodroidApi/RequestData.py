from Define import *
from concurrent.futures import Future
from datetime import datetime


class RequestData:
    def __init__(self) -> None:
        self._timeout: int = 0
        self._startTime: int = 0
        self._promise = Future()
        self._callBack = None
        self._sharedFuture = self._promise

    def set(self, id: int, timeout: int) -> None:
        self._id = id
        self._timeout = timeout
        self._startTime = datetime.now().timestamp()

    def _checkTimeout(self) -> bool:
        now = datetime.now().timestamp()

        if now > self._startTime + self._timeout:
            print("id:{} timeout".format(self._id))
            print("_startTime:{}".format(self._startTime))
            print("_timeout:{}".format(self._timeout))
            print("now:{}".format(now))
            return True
        return False

    def error(self, code: ResponseCode, msg: str) -> None:
        print("error:{}".format(msg))
        self._promise.set_result(Response(code, msg))

    def reply(self, data: str) -> None:
        dataJson = json.loads(data)
        print("reply:{}".format(json.dumps(dataJson, indent=4)))
        code: int = dataJson["code"]
        if code == 200:
            self._promise.set_result(
                Response(ResponseCode.OK, "ok", dataJson["data"]))
        else:
            self.error(ResponseCode.RequestFailed,
                       "request failed by code: {}".format(code))

    def future(self) -> Future:
        return self._sharedFuture
