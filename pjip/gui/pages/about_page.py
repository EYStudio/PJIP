from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from .page_updating import PageUpdating
from ..utils.q_pixmap_utils import make_round_pixmap
from ..utils.svg_utils import svg_to_pixmap
from ..resources import SVG_COLORED_LOGO

class AboutPage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = 'About'

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

        self.studio_icon = QLabel()

        img_pixmap = svg_to_pixmap(SVG_COLORED_LOGO)

        rounded = make_round_pixmap(img_pixmap, 256)

        self.studio_icon.setPixmap(rounded)
        self.studio_icon.setFixedSize(270, 270)
        self.studio_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.studio_icon.setStyleSheet('border: 5px solid #dddddd;')

        main_layout.addWidget(self.studio_icon)

        self.setLayout(main_layout)