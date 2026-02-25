from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QPushButton, QWidget, QLabel, QHBoxLayout, QSizePolicy


class SwitchButton(QPushButton):
    """A stable, extensible, Qt‑style switch button with hover/press effects."""

    def __init__(self):
        super().__init__('Off')

        self.setCheckable(True)
        self.setChecked(False)

        self.setMinimumWidth(38)

        self.qss_checked = """
            QPushButton {
                font: 18px;
                border: 2px solid #404040; 
                border-radius: 8px;        
                background-color: #cccccc; 
                color: #444444;        
                padding: 3px;       
            }
            QPushButton:hover {
                background-color: #E2E2E2; 
                border: 2px solid #666666; 
            }
            QPushButton:pressed {
                background-color: #D9D9D9; 
                border: 2px solid #808080;
            }
        """
        # """
        #     QPushButton {
        #         font: 18px;
        #         border: 2px solid #2A2A2A;
        #         border-radius: 8px;
        #         background-color: #444444;
        #         color: #cccccc;
        #         padding: 3px;
        #     }
        #     QPushButton:hover {
        #         background-color: #666666;
        #         border: 2px solid #444444;
        #     }
        #     QPushButton:pressed {
        #         background-color: #777777;
        #         border: 2px solid #656565;
        #     }
        # """

        self.qss_not_checked = """
            QPushButton {
                font: 18px;
                border: 2px solid #cccccc; 
                border-radius: 8px;        
                background-color: #eeeeee; 
                color: #444444;        
                padding: 3px;       
            }
            QPushButton:hover {
                background-color: #E2E2E2; 
                border: 2px solid #C4C4C4; 
            }
            QPushButton:pressed {
                background-color: #D9D9D9; 
                border: 2px solid #B7B7B7;
            }
        """

        self.update_style()

    def nextCheckState(self):
        super().nextCheckState()
        self.update_style()

    def update_style(self):
        if self.isChecked():
            self.setStyleSheet(self.qss_checked)
            self.setText('On')
        else:
            self.setStyleSheet(self.qss_not_checked)
            self.setText('Off')

    def setChecked(self, checked: bool):
        """Programmatically set checked state with animation."""
        if checked == self.isChecked():
            return

        super().setChecked(checked)

        self.update_style()

    def resizeEvent(self, event, /):
        h, w = self.height(), self.width()
        print(f"BUTTON HEIGHT: {h}, BUTTON WIDTH: {w}")
        if w / h > 1.5:
            self.setMaximumWidth(int(h * 1.5))
        super().resizeEvent(event)


class SwitchWidget(QWidget):
    toggled = Signal()
    clicked = Signal()

    def __init__(self, content: str, /, checked=False):
        super().__init__()
        layout = QHBoxLayout()
        self.switch_button = SwitchButton()
        self.label = QLabel(content)
        self.switch_button.setChecked(checked)

        self.label.setStyleSheet("""
            background-color: #eeeeee; 
            border-radius: 10px;
            font-size: 18px;
            /* border: 2px solid #cccccc; */
            color: #455A64;   
        """)

        # self.setStyleSheet('''border: 5px solid black''')

        self.switch_button.clicked.connect(self.clicked)
        self.switch_button.toggled.connect(self.toggled)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.switch_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        print(self.switch_button.size())

        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(self.switch_button)
        layout.addWidget(self.label)  # , alignment=Qt.AlignmentFlag.AlignLeft

        self.setLayout(layout)

    def mouseReleaseEvent(self, event):
        self.switch_button.nextCheckState()

    # noinspection PyPep8Naming
    def isChecked(self):
        return self.switch_button.isChecked()

    # noinspection PyPep8Naming
    def setChecked(self, check):
        self.switch_button.setChecked(check)

    # noinspection PyPep8Naming
    def setDisabled(self, boolean):
        self.switch_button.setDisabled(boolean)

    # noinspection PyPep8Naming
    def setEnabled(self, boolean):
        self.switch_button.setEnabled(boolean)
