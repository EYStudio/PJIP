from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QMainWindow

from .costume_widgets.blured_background import WallpaperBlurBackground
from .main_widget import MainWidget
from .resources import SVG_COLORED_LOGO
from .utils.svg_utils import svg_to_icon
from .windows.info_overlay import InfoOverlay


class MainWindow(QMainWindow):
    close_event = Signal()

    def __init__(self, config_object):
        super().__init__()
        self.initialization_window()

        enable_blured_background = True

        self.setObjectName('MainWindow')

        if not enable_blured_background:
            self.setStyleSheet("""#MainWindow{background-color: #ffffff}""")
            # self.setStyleSheet("""#MainWindow{background-color: #070707}""")

        self.background = WallpaperBlurBackground(self, enable_blured_background)

        self.info_overlay = InfoOverlay()
        self.info_overlay.show()

        # self.adapter = None

        # Set central widget
        self.main_widget = MainWidget(config_object, self.info_overlay)
        self.setCentralWidget(self.main_widget)

    def closeEvent(self, event):
        self.close_event.emit()
        event.accept()

    def initialization_window(self):
        self.setWindowTitle("PJIP")
        self.setMinimumSize(960 - 16, 540 - 9)
        self.resize(960 - 16, 540 - 9)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowIcon(svg_to_icon(SVG_COLORED_LOGO))

    def adapter_signal_connect(self, adapter):
        # self.adapter = adapter
        self.main_widget.adapter_signal_connect(adapter)

    def paintEvent(self, event, /):
        self.background.paint_event()
        super().paintEvent(event)

    def resizeEvent(self, event, /):
        self.background.update_background()
        super().resizeEvent(event)