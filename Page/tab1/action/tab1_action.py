"""Tab1Action"""

from Page.tab1.ui.tab1 import Tab1
from datetime import datetime


class Tab1Action(Tab1):
    def __init__(self):
        super().__init__()
        self.bind()

    def get_time(self) -> str :
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def bind(self):
        self.btn_frame.robot_on_clicked.connect(self.on_robot_on_clicked)
        self.btn_frame.robot_off_clicked.connect(self.on_robot_off_clicked)
        self.btn_frame.robot_manual_clicked.connect(self.on_robot_manual_clicked)
        self.btn_frame.robot_auto_clicked.connect(self.on_robot_auto_clicked)
        self.btn_frame.robot_safety_clicked.connect(self.on_robot_safety_clicked)
        self.btn_frame.robot_on1_clicked.connect(self.on_robot_on1_clicked)
        self.btn_frame.robot_on2_clicked.connect(self.on_robot_on2_clicked)
        self.ip_frame.btn_robot_connect_clicked.connect(self.on_robot_connect_clicked)

    def on_robot_on_clicked(self, data: str):
        # 将时间戳和日志消息一起追加到 log_edit 中
        self.log_edit.appendPlainText(f"[{self.get_time()}] {data}")

    def on_robot_off_clicked(self, data: str):
        # 将时间戳和日志消息一起追加到 log_edit 中
        self.log_edit.appendPlainText(f"[{self.get_time()}] {data}")

    def on_robot_manual_clicked(self, data: str):
        # 将时间戳和日志消息一起追加到 log_edit 中
        self.log_edit.appendPlainText(f"[{self.get_time()}] {data}")

    def on_robot_auto_clicked(self, data: str):
        # 将时间戳和日志消息一起追加到 log_edit 中
        self.log_edit.appendPlainText(f"[{self.get_time()}] {data}")

    def on_robot_safety_clicked(self, data: str):
        # 将时间戳和日志消息一起追加到 log_edit 中
        self.log_edit.appendPlainText(f"[{self.get_time()}] {data}")

    def on_robot_on1_clicked(self, data: str):
        # 将时间戳和日志消息一起追加到 log_edit 中
        self.log_edit.appendPlainText(f"[{self.get_time()}] {data}")

    def on_robot_on2_clicked(self, data: str):
        # 将时间戳和日志消息一起追加到 log_edit 中
        self.log_edit.appendPlainText(f"[{self.get_time()}] {data}")

    def on_robot_connect_clicked(self, data: str):
        # 将时间戳和日志消息一起追加到 log_edit 中
        self.log_edit.appendPlainText(f"[{self.get_time()}] {data}")
