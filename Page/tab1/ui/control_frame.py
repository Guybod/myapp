from PySide6.QtWidgets import QVBoxLayout, QFrame

from Page.base_ui.base_frame import BaseFrame
from Page.tab1.action.joint_frame_action import JointFrameAction

class ControlFrame(BaseFrame):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def init_ui(self):
        self.joint1_frame = JointFrameAction("joint1", "-", "+", -36000, 36000)
        self.joint2_frame = JointFrameAction("joint2", "-", "+", -36000, 36000)
        self.joint3_frame = JointFrameAction("joint3", "-", "+", -16000, 16000)
        self.joint4_frame = JointFrameAction("joint4", "-", "+", -36000, 36000)
        self.joint5_frame = JointFrameAction("joint5", "-", "+", -36000, 36000)
        self.joint6_frame = JointFrameAction("joint6", "-", "+", -36000, 36000)

    def init_layout(self):
        self.joint_layout = QVBoxLayout(self)
        self.joint_layout.addWidget(self.joint1_frame)
        self.joint_layout.addWidget(self.joint2_frame)
        self.joint_layout.addWidget(self.joint3_frame)
        self.joint_layout.addWidget(self.joint4_frame)
        self.joint_layout.addWidget(self.joint5_frame)
        self.joint_layout.addWidget(self.joint6_frame)