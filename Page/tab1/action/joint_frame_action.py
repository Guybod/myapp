"""JointFrameAction"""

from Page.tab1.ui.joint_frame import JointFrame


class JointFrameAction(JointFrame):
    def __init__(self, name:str="", sub:str="", add:str="", min:int=0, max:int=0):
        super().__init__(name, sub, add, min, max)
        self.bind()

    def bind(self):
        self.sub_btn.clicked.connect(self.sub_val)
        self.add_btn.clicked.connect(self.add_val)
        self.slider.valueChanged.connect(self.slider_value_update)  # 滑块值改变时更新文本框
        self.lineEdit_value.editingFinished.connect(self.line_edit_changed_val)  # 文本框值改变时更新滑块

    def sub_val(self):
        current_value = self.slider.value()
        if current_value > self.min:
            self.slider.setValue(current_value - 1)

    def add_val(self):
        current_value = self.slider.value()
        if current_value < self.max:
            self.slider.setValue(current_value + 1)

    def slider_value_update(self):
        # 滑块值改变时更新文本框
        # print(self.slider.value())
        # 滑块值改变时更新文本框
        self.lineEdit_value.setText(f"{(float(self.slider.value() / 100)):.2f}")

    def line_edit_changed_val(self):
        # 文本框值改变时更新滑块
        try:
            value = float(self.lineEdit_value.text()) * 100
            if self.min <= value <= self.max:
                self.slider.setValue(int(value))
            else:
                self.lineEdit_value.setText(f"{(float(self.slider.value() / 100)):.2f}")
        except ValueError:
            # 如果输入无效，恢复到滑块的当前值
            self.lineEdit_value.setText(f"{(float(self.slider.value() / 100)):.2f}")
