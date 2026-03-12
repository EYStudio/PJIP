from PySide6.QtCore import Qt, Signal, QUrl
from PySide6.QtGui import QFont, QDesktopServices
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout

from pjip.config.build_info import STUDIO_NAME, STUDIO_MOTTO

from ..resources import SVG_COLORED_LOGO
from ..utils.q_pixmap_utils import make_round_pixmap
from ..utils.svg_utils import svg_to_pixmap


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
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

        package = QWidget()
        package_layout = QVBoxLayout(package)

        wrapper = ClickableWidget("https://github.com/Eystudio")
        wrapper_layout = QHBoxLayout(wrapper)
        wrapper.setObjectName('wrapper')

        self.studio_icon = QLabel()

        img_pixmap = svg_to_pixmap(SVG_COLORED_LOGO)
        rounded = make_round_pixmap(img_pixmap, 256)

        self.studio_icon.setPixmap(rounded)
        self.studio_icon.setFixedSize(290, 270)
        self.studio_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        wrapper_layout.addWidget(self.studio_icon)
        wrapper_layout.setContentsMargins(33, 0, 0, 0)
        wrapper.setStyleSheet("""
            #wrapper{
                /* border: 5px solid #dddddd; */
                border-radius: 20px;
            }
            """)

        # self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        # self.setObjectName('about_page')
        # self.setStyleSheet("""
        # #about_page{
        # background-color: rgba(250, 250, 250, 150);
        # border-radius: 5px;
        # }""")

        package.setObjectName('package')
        package.setStyleSheet("""
        #package{
            background-color: rgba(250, 250, 250, 100);
            border: 1px solid rgba(255, 255, 255, 150); 
            border-radius: 10px;
        }
        """)

        studio_info_widget = QWidget()
        studio_info_widget.setObjectName('studio_info_widget')
        studio_info_layout = QVBoxLayout(studio_info_widget)

        self.studio_name = QLabel()
        self.studio_name.setText(STUDIO_NAME)
        self.studio_name.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.studio_name.setStyleSheet("""
            font-size: 40px;
            color: #555555;   
        """)
        self.studio_name.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        studio_info_font = QFont("Segoe UI")
        self.studio_name.setFont(studio_info_font)

        studio_motto_label = QLabel(STUDIO_MOTTO)
        studio_motto_label.setStyleSheet("""
            font-size: 18px;
            color: #555555;   
            padding-right: 10px;
        """)
        studio_motto_font = QFont("Segoe UI")
        studio_motto_font.setItalic(True)
        studio_motto_label.setFont(studio_motto_font)

        studio_info_layout.addWidget(self.studio_name, alignment=Qt.AlignmentFlag.AlignHCenter)
        studio_info_layout.addWidget(studio_motto_label, alignment=Qt.AlignmentFlag.AlignRight)
        studio_info_widget.setStyleSheet("""
            #studio_info_widget{
                border-radius: 10px;
                font-size: 36px;
                /* border: 3px solid #cccccc; */
                padding: 10px;
            }
        """)

        package_layout.addWidget(wrapper)
        package_layout.addWidget(studio_info_widget)

        main_layout.addWidget(package)

        self.setLayout(main_layout)


class ClickableLabel(QLabel):
    def mousePressEvent(self, event):
        QDesktopServices.openUrl(QUrl("https://github.com/Eystudio"))


class ClickableWidget(QWidget):
    def __init__(self, url: str, /):
        super().__init__()
        self.url = url
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

    def mousePressEvent(self, event):
        QDesktopServices.openUrl(QUrl(self.url))
