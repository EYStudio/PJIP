from PySide6.QtWidgets import QPushButton


class SwitchButton(QPushButton):
    """A stable, extensible, Qt‑style switch button with hover/press effects."""

    def __init__(self):
        super().__init__('Off')

        self.setCheckable(True)
        self.setChecked(False)

        self.qss_checked = """
            QPushButton {
                font: 20px;
                border: 2px solid #2A2A2A; 
                border-radius: 8px;        
                background-color: #444444; 
                color: #cccccc;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #666666; 
                border: 2px solid #444444; 
            }
            QPushButton:pressed {
                background-color: #777777; 
                border: 2px solid #656565;
            }
        """

        self.qss_not_checked = """
            QPushButton {
                font: 20px;
                border: 2px solid #cccccc; 
                border-radius: 8px;        
                background-color: #eeeeee; 
                color: #444444;        
                padding: 5px;       
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

    def resizeEvent(self, event, /):
        h, w = self.height(), self.width()
        print(f"BUTTON HEIGHT: {h}, BUTTON WIDTH: {w}")
        if w / h > 1.5:
            self.setMaximumWidth(int(h * 1.5))
        super().resizeEvent(event)
