from PySide6.QtWidgets import QLabel, QPushButton, QSlider, QHBoxLayout, QLineEdit
from PySide6.QtCore import Qt
from Page.base_ui.base_frame import BaseFrame
from Page.style.style import Style

class JointFrame(BaseFrame):
    def __init__(self, name:str="", sub:str="", add:str="", min:int=0, max:int=0):
        super().__init__()
        self.setupUi()
        self.set_style()
        self.name = name
        self.add = add
        self.sub = sub
        self.min = min
        self.max = max
        self.set_parameters()

    def init_ui(self):
        self.label_name = QLabel(self)
        self.sub_btn = QPushButton(self)
        self.slider = QSlider(Qt.Horizontal, self)  # 水平滑动条
        self.lineEdit_value = QLineEdit(self)
        self.add_btn = QPushButton(self)


    def init_layout(self):
        self.joint_layout = QHBoxLayout(self)
        self.joint_layout.addWidget(self.label_name)
        self.joint_layout.addWidget(self.sub_btn)
        self.joint_layout.addWidget(self.slider)
        self.joint_layout.addWidget(self.add_btn)
        self.joint_layout.addWidget(self.lineEdit_value)

    def set_style(self):
        self.style = Style()
        self.style.set_slider_style(self.slider)
        self.style.set_circle_btn_style(self.add_btn)
        self.style.set_circle_btn_style(self.sub_btn)
        self.style.set_slider_edit_style(self.lineEdit_value)

    def set_parameters(self):
        self.label_name.setText(self.name)
        self.sub_btn.setText(self.sub)
        self.add_btn.setText(self.add)

        self.slider.setRange(self.min, self.max)  # 设置滑动条的范围
        self.slider.setValue(0)  # 设置滑动条的初始值
        self.slider.setSingleStep(1)  # 设置滑动条的单步值
        self.slider.setPageStep(10)  # 设置滑动条的页步值
        self.slider.setTickPosition(QSlider.TicksBelow)  # 设置刻度位置
        self.slider.setTickInterval(30)  # 设置刻度间隔

        self.lineEdit_value.setText("0.00")


