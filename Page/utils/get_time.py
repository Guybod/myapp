
from datetime import datetime

class GetTime():
    def __init__(self):
        pass

    @staticmethod
    def  get_time() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")