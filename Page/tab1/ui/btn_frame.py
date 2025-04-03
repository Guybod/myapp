"""btn_frame.py"""

from PySide6.QtWidgets import QHBoxLayout, QPushButton

from Page.base_ui.base_frame import BaseFrame
from Page.style.style import Style


class BtnFrame(BaseFrame):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.set_style()


    def init_ui(self):
        self.btn_robot_on = QPushButton("上电", self)
        self.btn_robot_off = QPushButton("下电", self)
        self.btn_robot_manual  = QPushButton("手动", self)
        self.btn_robot_auto = QPushButton("自动", self)
        self.btn_robot_safety = QPushButton("救援模式上电", self)
        self.btn_robot_on1 = QPushButton("？？", self)
        self.btn_robot_on2 = QPushButton("？？", self)


    def init_layout(self):
        self.btn_layout = QHBoxLayout(self)
        self.btn_layout.addWidget(self.btn_robot_on)
        self.btn_layout.addWidget(self.btn_robot_off)
        self.btn_layout.addWidget(self.btn_robot_manual)
        self.btn_layout.addWidget(self.btn_robot_auto)
        self.btn_layout.addWidget(self.btn_robot_safety)
        self.btn_layout.addWidget(self.btn_robot_on1)
        self.btn_layout.addWidget(self.btn_robot_on2)


    def set_style(self):
        self.style = Style()
        self.style.set_btn_style(self.btn_robot_on)
        self.style.set_btn_style(self.btn_robot_off)
        self.style.set_btn_style(self.btn_robot_manual)
        self.style.set_btn_style(self.btn_robot_auto)
        self.style.set_btn_style(self.btn_robot_safety)
        self.style.set_btn_style(self.btn_robot_on1)
        self.style.set_btn_style(self.btn_robot_on2)
