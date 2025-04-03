from PySide6.QtWidgets import QVBoxLayout, QFrame

from Page.base_ui.base_frame import BaseFrame
from Page.tab1.ui.joint_frame import JointFrame


class ControlFrame(BaseFrame):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def init_ui(self):
        self.joint1_frame = JointFrame()
        self.joint1_frame.set_parame("joint1", "-", "+", -36000, 36000)
        self.joint2_frame = JointFrame()
        self.joint2_frame.set_parame("joint2", "-", "+", -36000, 36000)
        self.joint3_frame = JointFrame()
        self.joint3_frame.set_parame("joint3", "-", "+", -16000, 16000)
        self.joint4_frame = JointFrame()
        self.joint4_frame.set_parame("joint4", "-", "+", -36000, 36000)
        self.joint5_frame = JointFrame()
        self.joint5_frame.set_parame("joint5", "-", "+", -36000, 36000)
        self.joint6_frame = JointFrame()
        self.joint6_frame.set_parame("joint6", "-", "+", -36000, 36000)

    def init_layout(self):
        self.joint_layout = QVBoxLayout(self)
        self.joint_layout.addWidget(self.joint1_frame)
        self.joint_layout.addWidget(self.joint2_frame)
        self.joint_layout.addWidget(self.joint3_frame)
        self.joint_layout.addWidget(self.joint4_frame)
        self.joint_layout.addWidget(self.joint5_frame)
        self.joint_layout.addWidget(self.joint6_frame)