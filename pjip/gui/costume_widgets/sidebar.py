from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QPushButton, QSizePolicy, QLayout


class SideBar(QWidget):
    def __init__(self, pages):
        super().__init__()
        self.pages = pages

        self.TASKBAR_BTN_HEIGHT = 32
        self.TASKBAR_BTN_WIDTH = int(self.TASKBAR_BTN_HEIGHT * 2)
        self.SPACING = 4

        self.SIDEBAR_HEIGHT = self.TASKBAR_BTN_HEIGHT + self.SPACING * 2  # Fixed height

        # Sidebar
        self.sidebar_layout = QVBoxLayout(self)
        self.sidebar_layout.setContentsMargins(self.SPACING, self.SPACING, self.SPACING, self.SPACING)
        # self.sidebar_layout.setSpacing(self.SPACING)

        self.sidebar_button_group = QButtonGroup(self)
        self.sidebar_button_group.setExclusive(True)

        base_btn_style = f"""
                   QPushButton {{
                       background-color: #e6e6e6;
                       border-radius: {self.TASKBAR_BTN_HEIGHT // 4}px; 
                       padding: 0px;
                       font-weight: bold; 
                       color: #444444;
                   }}
                   QPushButton:hover {{
                       background-color: #dcdcdc;
                   }}
                   QPushButton:pressed {{
                       background-color: #cbcbcb;
                   }}
                   QPushButton:checked {{
                       background-color: #4a90e2;
                       color: white;
                   }}
               """

        sidebar_container = QWidget()
        sidebar_container.setStyleSheet('border: 1px solid black')
        sidebar_container_layout = QVBoxLayout(sidebar_container)
        sidebar_container_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_container_layout.setSpacing(self.SPACING)

        sidebar_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sidebar_container_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        for index, widget in enumerate(self.pages):
            page_name = widget.page_name
            btn = QPushButton(page_name)
            btn.setFixedSize(self.TASKBAR_BTN_WIDTH, self.TASKBAR_BTN_HEIGHT)
            btn.setCheckable(True)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(base_btn_style)
            btn.setToolTip(page_name)
            self.sidebar_button_group.addButton(btn, index)
            print(btn.size())
            sidebar_container_layout.addWidget(btn)

        self.sidebar_button_group.buttons()[0].setChecked(True)

        self.sidebar_layout.addWidget(sidebar_container, alignment=Qt.AlignmentFlag.AlignCenter)

        # Issue in placing sidebar buttons in center
        # self.sidebar_layout.addStretch()

        # self.setFixedHeight(self.SIDEBAR_HEIGHT)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        self.setObjectName("sidebar")

    def get_button_group(self):
        return self.sidebar_button_group

