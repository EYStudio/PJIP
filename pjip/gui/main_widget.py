from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget

from .pages import ToolPage, FunctionPage, SettingsPage, UpdatePage, AboutPage
from .costume_widgets import SideBar


class MainWidget(QWidget):
    def __init__(self, config_object):
        super().__init__()
        self.config_object = config_object
        self.adapter = None
        self.live_frame = None

        self.sidebar = None
        self.sidebar_tabs = self.sidebar_button_group = None

        self.pages = self.stack_pages = None
        self.tool_page = self.functions_page = self.about_page = self.settings_page = self.update_page = None

        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(5, 4, 5, 5)
        main_layout.setSpacing(2)

        self.setStyleSheet("""#QWidget{background-color: rgba(255,255,255, 0)}""")

        # Init stack_pages
        self.tool_page = ToolPage()
        self.functions_page = FunctionPage()
        self.settings_page = SettingsPage(self.config_object)
        self.update_page = UpdatePage()
        self.about_page = AboutPage()

        self.pages = [
            self.tool_page,
            self.functions_page,
            self.settings_page,
            self.update_page,
            self.about_page,
        ]

        self.sidebar = SideBar(self.pages)

        self.live_frame = QWidget()
        self.live_frame.setObjectName("live_frame")

        self.live_frame.setStyleSheet("""
            #live_frame {
                /* background-color: #eeeeee; */
                border-radius: 10px;
                font-size: 24px;
                border: 4px solid #cccccc;
                color: #455A64;   
            }
        """)

        live_frame_layout = QVBoxLayout(self.live_frame)
        live_frame_layout.setContentsMargins(5, 5, 5, 5)
        live_frame_layout.setSpacing(5)

        # Stack stack_pages
        self.stack_pages = QStackedWidget()
        for page in self.pages:
            self.stack_pages.addWidget(page)
        self.sidebar.get_button_group().idClicked.connect(self.stack_pages.setCurrentIndex)

        live_frame_layout.addWidget(self.stack_pages)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.live_frame, 1)

        self.setLayout(main_layout)

    def adapter_signal_connect(self, adapter):
        self.adapter = adapter
        self.adapter.ui_change.connect(self.signal_handler)

        self.tool_page.set_adapter(self.adapter)
        self.functions_page.set_adapter(self.adapter)
        self.settings_page.set_adapter(self.adapter)
        self.update_page.set_adapter(self.adapter)

    def signal_handler(self, name, value):
        print(f'Signal: {name}, {value}')
        match name:
            case 'MonitorAdapter':
                self.tool_page.ui_change.emit(name, value)
                self.live_frame_change(value)
            case 'SuspendMonitorAdapter':
                self.tool_page.ui_change.emit(name, value)
            case 'UpdateAdapter':
                self.update_page.ui_change.emit(name, value)
            case 'GetStudentmainPasswordAdapter':
                self.functions_page.ui_change.emit(name, value)

    def live_frame_change(self, studentmain_running_state):
        if studentmain_running_state:
            self.live_frame.setStyleSheet("""
                #live_frame {
                    /* background-color: #eeeeee; */
                    border-radius: 10px;
                    font-size: 24px;
                    /*border: 4px solid #E66926; */
                    border: 4px solid #E6A56E;
                    color: #455A64;   
                }
            """)
        else:
            self.live_frame.setStyleSheet("""
                #live_frame {
                    /* background-color: #eeeeee; */
                    border-radius: 10px;
                    font-size: 24px;
                    border: 4px solid #3DC766;
                    color: #455A64;   
                }
            """)
