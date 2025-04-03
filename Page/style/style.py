from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Style():
    def __init__(self):
        pass

    def set_btn_style(self, btn, width:int=85, height:int=30):
        btn.setFixedSize(width, height)
        btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* 背景颜色 */
                color: white; /* 文字颜色 */
                border: 2px solid #4CAF50; /* 边框颜色和宽度 */
                border-radius: 5px; /* 圆角 */
                font-size: 12px; /* 字体大小 */
            }
            QPushButton:hover {
                background-color: #45a049; /* 鼠标悬停时的背景颜色 */
            }
            QPushButton:pressed {
                background-color: #398a3d; /* 按钮按下时的背景颜色 */
            }
        """)

    def set_line_edit_style(self, line_edit, width:int=200, height:int=30, text:str=""):
        line_edit.setPlaceholderText(text)  # 设置占位符文本
        line_edit.setFixedSize(width, height)
        line_edit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF; /* 背景颜色 */
                color: #333333; /* 文字颜色 */
                border: 2px solid #CCCCCC; /* 边框颜色和宽度 */
                border-radius: 3px; /* 圆角 */
                padding: 0px; /* 内边距 */
                font-size: 14px; /* 字体大小 */
            }
            QLineEdit:focus {
                border: 2px solid #4CAF50; /* 聚焦时的边框颜色 */
            }
            QLineEdit::selection {
                background-color: #4CAF50; /* 选中文本的背景颜色 */
                color: #FFFFFF; /* 选中文本的颜色 */
            }
        """)

    def set_qlabel_style(self, qlabel, width:int=80, height:int=30, font_size:int = 8, bold:bool=False, alignment:str="left"):
        qlabel.setFixedSize(width, height)  # 设置固定大小
        font = QFont()
        font.setPointSize(font_size)  # 设置文字大小
        font.setBold(bold)  # 设置是否加粗
        qlabel.setFont(font)
        if alignment == "center":
            qlabel.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        elif alignment == "left":
            qlabel.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        elif alignment == "right":
            qlabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

    def set_circle_btn_style(self, button, size: int = 30):
        button.setFixedSize(size, size)  # 设置按钮的固定大小
        button.setStyleSheet(f"""
                    QPushButton {{
                        background-color: #4CAF50; /* 背景颜色 */
                        color: white; /* 文字颜色 */
                        border: 2px solid #4CAF50; /* 边框颜色和宽度 */
                        border-radius: {size // 2}px; /* 圆角半径，使按钮呈圆形 */
                        font-size: {(size // 2) + 3}px; /* 字体大小 */
                    }}
                    QPushButton:hover {{
                        background-color: #45a049; /* 鼠标悬停时的背景颜色 */
                    }}
                    QPushButton:pressed {{
                        background-color: #398a3d; /* 按钮按下时的背景颜色 */
                    }}
                """)

    def set_slider_style(self, slider):
        slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: white; /* 滑动条底色 */
                height: 10px; /* 滑动条高度 */
                border: 1px solid #999; /* 滑动条边框 */
            }
            QSlider::handle:horizontal {
                background: #4CAF50; /* 滑动部分颜色 */
                width: 18px; /* 滑块宽度 */
                margin: -6px 0; /* 滑块边缘调整 */
                border-radius: 9px; /* 滑块圆角 */
            }
            QSlider::sub-page:horizontal {
                background: #4CAF50; /* 滑动部分颜色 */
                border: 1px solid #999; /* 滑动部分边框 */
                border-radius: 5px; /* 滑动部分两端圆角 */
            }
        """)