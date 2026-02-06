from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy

from ..utils.q_pixmap_utils import make_round_pixmap
from ..utils.svg_utils import svg_to_pixmap
from ..resources import SVG_COLORED_LOGO

class AboutPage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = 'About'
        self.studio_icon = None

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

        self.studio_icon = QLabel()

        img_pixmap = svg_to_pixmap(SVG_COLORED_LOGO)

        rounded = make_round_pixmap(img_pixmap, 256)

        self.studio_icon.setPixmap(rounded)
        self.studio_icon.setFixedSize(290, 270)
        self.studio_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.studio_icon.setStyleSheet("""
            border: 5px solid #dddddd;
            padding-left: 10px;
            border-radius: 20px""")

        self.studio_name = QLabel()
        self.studio_name.setText('Eystudio')
        self.studio_name.setStyleSheet("""
            border-radius: 10px;
            font-size: 24px;
            border: 3px solid #cccccc;
            color: #555555;   
            padding: 10px;
        """)
        self.studio_name.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        studio_name_font = QFont("Segoe UI")
        self.studio_name.setFont(studio_name_font)

        main_layout.addWidget(self.studio_icon, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(self.studio_name, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(main_layout)