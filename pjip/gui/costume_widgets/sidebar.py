from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QButtonGroup, QSizePolicy, QPushButton, QLayout, QVBoxLayout


class SideBar(QWidget):
    def __init__(self, pages):
        super().__init__()
        self.pages = pages

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setObjectName("sidebar")

        self.TASKBAR_BTN_HEIGHT = 56
        # self.TASKBAR_BTN_WIDTH = int(self.TASKBAR_BTN_HEIGHT * 2)
        self.TASKBAR_BTN_WIDTH = 66
        self.SPACING = 4

        # Sidebar
        self.sidebar_layout = QVBoxLayout(self)
        self.sidebar_layout.setContentsMargins(self.SPACING, self.SPACING, self.SPACING, self.SPACING)

        self.sidebar_button_group = QButtonGroup()
        self.sidebar_button_group.setExclusive(True)

        base_btn_style = f"""
            QPushButton {{
               background-color: rgba(255, 255, 255, 100);
               /* border-radius: {self.TASKBAR_BTN_HEIGHT // 4}px; */
               border-radius: 0px; 
               padding: 0px;
               font-weight: bold; 
               color: #444444;
               border-left: 5px solid rgba(255, 255, 255, 0);
            }}
            QPushButton:hover {{
               background-color: rgba(220, 220, 220, 100);
               border-left: 5px solid rgba(220, 220, 220, 0); 
            }}
            QPushButton:pressed {{
               background-color: rgba(220, 220, 220, 100);
               border-left: 5px solid rgba(240, 240, 240, 50); 
            }}
            QPushButton:checked {{
               /* background-color: #4a90e2; */
               background-color: rgba(74, 144, 226, 100);
               border-left: 5px solid rgba(220, 220, 220, 75);
               color: white;
            }}
        """

        sidebar_container = QWidget()
        sidebar_container.setObjectName("iw")
        # sidebar_container.setStyleSheet('#iw{background-color: lightblue}')
        sidebar_container_layout = QVBoxLayout(sidebar_container)
        sidebar_container_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_container_layout.setSpacing(self.SPACING)

        sidebar_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
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
            sidebar_container_layout.addWidget(btn)

        self.sidebar_button_group.buttons()[0].setChecked(True)

        # self.sidebar_layout.addWidget(sidebar_container, alignment=Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(sidebar_container, alignment=Qt.AlignmentFlag.AlignTop)

        # Issue in placing sidebar buttons in center
        # self.sidebar_layout.addStretch()

        print(self.TASKBAR_BTN_WIDTH + self.SPACING * 2)
        self.setFixedWidth(self.TASKBAR_BTN_WIDTH + self.SPACING * 2)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        # self.setStyleSheet("""
        #     #sidebar {
        #         background-color: green
        #     }
        # """)

    def get_button_group(self):
        return self.sidebar_button_group