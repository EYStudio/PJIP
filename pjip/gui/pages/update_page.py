from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout, QSizePolicy

from pjip.core.enums import UpdateState
from ..costume_widgets.switch_button import SwitchWidget
from ...config.runtime_config.config_structure import ConfigRoot


class UpdatePage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self, config_object: ConfigRoot):
        super().__init__()
        self.page_name = 'Updates'
        self.config_object = config_object

        self.studentmain_state = None
        self.update_state_label = None
        self.current_version_display_label = None
        self.get_update_btn = None
        self.adapter = None
        self.current_version = None

        self.init_ui()

        self.signal_connect()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

        version_display = QWidget()
        version_display.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        version_display.setObjectName("version_display_frame")

        version_display.setStyleSheet("""
                    #version_display_frame {
                        background-color: #eeeeee; 
                        border-radius: 10px;
                        font-size: 24px;
                        border: 2px solid #cccccc;
                        color: #455A64;   
                    }
                """)

        version_display_frame_layout = QVBoxLayout(version_display)
        version_display_frame_layout.setContentsMargins(12, 5, 10, 5)
        version_display_frame_layout.setSpacing(3)

        switch_widget_auto_download_update = SwitchWidget('Auto download update')
        switch_widget_auto_download_update.setFixedHeight(55)

        self.current_version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_version_label.setStyleSheet("""
                                    background-color: rgba(238, 238, 238, 120); 
                                    border-radius: 10px;
                                    font-size: 24px;
                                    border: 1px solid rgba(255, 255, 255, 150);
                                    color: #455A64;   
                                    margin-left: 5px;
                                    """)
        self.current_version_display_label.setText(f'Current version: N / a')
        self.current_version_display_label.setFixedHeight(40)


        self.latest_version_display_label = QLabel()
        self.latest_version_display_label.setStyleSheet("""
                                    background-color: #eeeeee; 
                                    border-radius: 10px;
                                    font-size: 18px;
                                    /* border: 2px solid #cccccc; */
                                    color: #455A64;   
                                    margin-left: 5px;
                                    """)
        self.latest_version_display_label.setText(f'Latest version: N/a')
        self.latest_version_display_label.setFixedHeight(40)

        self.update_state_label = QLabel()
        self.update_state_label.setWordWrap(True)

        # self.update_state_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_state_label.setStyleSheet("""
                                    background-color: rgba(238, 238, 238, 120); 
                                    border-radius: 10px;
                                    font-size: 24px;
                                    border: 1px solid rgba(255, 255, 255, 150);
                                    color: #455A64;   
                                    margin-left: 5px;
                                    """)
        self.update_state_label.setText(f'Getting updates')
        # self.update_state_label.setFixedHeight(100)

        version_display_frame_layout.addWidget(switch_widget_auto_download_update)
        version_display_frame_layout.addWidget(self.current_version_display_label)
        version_display_frame_layout.addWidget(self.latest_version_display_label)
        version_display_frame_layout.addWidget(self.update_state_label)

        button_layout = QGridLayout()

        self.get_update_btn = QPushButton("Get updates Manually")
        self.get_update_btn.clicked.connect(self.get_update)

        for i, btn in enumerate([self.get_update_btn]):
            btn.setMinimumHeight(50)
            button_layout.addWidget(btn, i // 2, i % 2)
            btn.setStyleSheet("""
                QPushButton {
                    font: 20px;
                    border: 1px solid rgba(255, 255, 255, 150); 
                    border-radius: 8px;        
                    background-color: rgba(238, 238, 238, 100); 
                    color: #455A64;               
                }
                QPushButton:hover {
                    background-color: rgba(226, 226, 226, 100); 
                    border: 1px solid rgba(255, 255, 255, 200); 
                }
                QPushButton:pressed {
                    background-color: rgba(217, 217, 217, 100); 
                    border: 1px solid rgba(255, 255, 255, 240);
                }
            """)

        main_layout.addWidget(version_display)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def signal_connect(self):
        self.ui_change.connect(self.signal_handler)

    def signal_handler(self, name, value):
        # print(f'Signal in toolkit page: {name}, {value}')
        match name:
            case 'UpdateAdapter':
                self.update_update_label(value)

    def set_adapter(self, adapter):
        self.adapter = adapter

        self.current_version = self.adapter.get_current_version()
        self.current_version_display_label.setText(f'Current version: {self.current_version}')

    def get_update(self):
        # deprecated
        self.update_state_label.setText(f'Getting updates in process...')

        self.adapter.get_update()

    def update_update_label(self, state_package):
        state, content = state_package

        if state == UpdateState.UPDATE_AVAILABLE:
            self.update_state_label.setText(f'A new version is available: {content}')
            self.latest_version_display_label.setText(f'Latest version: {content}')
        elif state == UpdateState.IS_LATEST:
            self.update_state_label.setText('You are already using the latest version')
            self.latest_version_display_label.setText(f'Latest version: {self.current_version}')
        elif state == UpdateState.LOCAL_NEWER:
            self.update_state_label.setText(
                'You are using a development version newer than the latest release.')
            self.latest_version_display_label.setText(f'Latest version: {content}')
        elif state == UpdateState.NOT_FOUND:
            self.update_state_label.setText('No updates found')
        elif state == UpdateState.ERROR:
            self.update_state_label.setText('An error has occurred while checking for updates.')
        elif state == UpdateState.IDLE:
            self.update_state_label.setText('Update check has not started yet.')
            self.latest_version_display_label.setText('Latest version: N/A')
        elif state == UpdateState.CHECKING or state == UpdateState.NORMAL:
            self.update_state_label.setText('Checking for updates, please wait...')
            self.latest_version_display_label.setText('Latest version: querying...')
        else:
            self.update_state_label.setText("Unexpected state. Please contact the developers.")
