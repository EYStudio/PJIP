from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, adapter):
        super().__init__()
        self.initialization_window()

    def closeEvent(self, event):
        event.accept()

    def initialization_window(self):
        self.setWindowTitle("Jiv test")
        self.setMinimumSize(960, 540)
        self.resize(960, 540)
