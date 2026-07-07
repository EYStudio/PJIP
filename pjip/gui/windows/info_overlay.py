
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt


from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

class InfoOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool |
            Qt.WindowType.WindowTransparentForInput
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # 外层布局
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)

        # 容器：半透明黑底
        container = QWidget(self)
        container.setObjectName("overlay_container")
        container.setStyleSheet("""
            #overlay_container {
                background-color: rgba(0, 0, 0, 100);
                border-radius: 8px;
            }
        """)

        # 容器布局
        layout = QVBoxLayout(container)
        layout.setContentsMargins(8, 8, 8, 8)

        # A 行
        row_a = QWidget()
        row_a_layout = QHBoxLayout(row_a)
        row_a_layout.setContentsMargins(0, 0, 0, 0)
        self.label_a_prefix = QLabel("Studentmain:", row_a)
        self.label_a_prefix.setStyleSheet("color: white; font-size: 18px;")
        self.label_a_value = QLabel("Not Running", row_a)
        self.label_a_value.setStyleSheet("color: green; font-size: 18px;")
        row_a_layout.addWidget(self.label_a_prefix)
        row_a_layout.addWidget(self.label_a_value)

        # B 行
        row_b = QWidget()
        row_b_layout = QHBoxLayout(row_b)
        row_b_layout.setContentsMargins(0, 0, 0, 0)
        self.label_b_prefix = QLabel("B:", row_b)
        self.label_b_prefix.setStyleSheet("color: white; font-size: 18px;")
        self.label_b_value = QLabel("xxx", row_b)
        self.label_b_value.setStyleSheet("color: red; font-size: 18px;")
        row_b_layout.addWidget(self.label_b_prefix)
        row_b_layout.addWidget(self.label_b_value)

        layout.addWidget(row_a)
        layout.addWidget(row_b)

    def update_a(self, text, color="green"):
        self.label_a_value.setText(text)
        self.label_a_value.setStyleSheet(f"color: {color}; font-size: 18px;")

    def update_b(self, text, color="red"):
        self.label_b_value.setText(text)
        self.label_b_value.setStyleSheet(f"color: {color}; font-size: 18px;")
