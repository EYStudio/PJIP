from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout

from ..utils.q_pixmap_utils import make_round_pixmap
from ..utils.svg_utils import svg_to_pixmap
from ..resources import SVG_COLORED_LOGO

class AboutPage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = 'About'
        self.studio_icon = None
        self.studio_name = None

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 3, 10, 3)
        main_layout.setSpacing(5)

        wrapper = QWidget()
        wrapper_layout = QHBoxLayout(wrapper)
        wrapper.setObjectName('wrapper')

        self.studio_icon = QLabel()

        img_pixmap = svg_to_pixmap(SVG_COLORED_LOGO)
        rounded = make_round_pixmap(img_pixmap, 256)

        self.studio_icon.setPixmap(rounded)
        self.studio_icon.setFixedSize(290, 270)
        self.studio_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        wrapper_layout.addWidget(self.studio_icon)
        wrapper_layout.setContentsMargins(30, 0, 0, 0)
        wrapper.setStyleSheet("""
            #wrapper{
                border: 5px solid #dddddd;
                border-radius: 20px;
            }
            """)

        studio_info_widget = QWidget()
        studio_info_widget.setObjectName('studio_info_widget')
        studio_info_layout = QVBoxLayout(studio_info_widget)

        self.studio_name = QLabel()
        self.studio_name.setText('Eystudio')
        self.studio_name.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.studio_name.setStyleSheet("""
            font-size: 36px;
            color: #555555;   
        """)
        self.studio_name.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        studio_info_font = QFont("Segoe UI")
        self.studio_name.setFont(studio_info_font)

        studio_info_layout.addWidget(self.studio_name, alignment=Qt.AlignmentFlag.AlignHCenter)
        studio_info_widget.setStyleSheet("""
            #studio_info_widget{
                border-radius: 10px;
                font-size: 36px;
                border: 3px solid #cccccc;
                padding: 10px;
            }
        """)

        # slogan = None ; motto?

        main_layout.addWidget(wrapper, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(studio_info_widget)

        self.setLayout(main_layout)