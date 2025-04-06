"""BtnFrameAction"""
from datetime import datetime

from PySide6.QtCore import Signal, Qt

from Page.tab1.ui.btn_frame import BtnFrame


class BtnFrameAction(BtnFrame):
    # 定义信号
    robot_on_clicked = Signal(str)
    robot_off_clicked = Signal(str)
    robot_manual_clicked = Signal(str)
    robot_auto_clicked = Signal(str)
    robot_safety_clicked = Signal(str)
    robot_on1_clicked = Signal(str)
    robot_on2_clicked = Signal(str)


    def __init__(self):
        super().__init__()
        self.bind()

    def bind(self):
        self.btn_robot_on.clicked.connect(self.btn_robot_on_callback)
        self.btn_robot_off.clicked.connect(self.btn_robot_off_callback)
        self.btn_robot_manual.clicked.connect(self.btn_robot_manual_callback)
        self.btn_robot_auto.clicked.connect(self.btn_robot_auto_callback)
        self.btn_robot_safety.clicked.connect(self.btn_robot_safety_callback)
        self.btn_robot_on1.clicked.connect(self.btn_robot_on1_callback)
        self.btn_robot_on2.clicked.connect(self.btn_robot_on2_callback)

    def btn_robot_on_callback(self):
        data = "robot on 按钮被点击！"
        self.robot_on_clicked.emit(data)

    def btn_robot_off_callback(self):
        data = "robot off 按钮被点击！"
        self.robot_off_clicked.emit(data)

    def btn_robot_manual_callback(self):
        data = "robot manual 按钮被点击！"
        self.robot_manual_clicked.emit(data)

    def btn_robot_auto_callback(self):
        data = "robot auto 按钮被点击！"
        self.robot_auto_clicked.emit(data)

    def btn_robot_safety_callback(self):
        data = "robot safety 按钮被点击！"
        self.robot_safety_clicked.emit(data)

    def btn_robot_on1_callback(self):
        data ="robot on1 按钮被点击！"
        self.robot_on1_clicked.emit(data)

    def btn_robot_on2_callback(self):
        data = "robot on2 button is clicked!"
        self.robot_on2_clicked.emit(data)
