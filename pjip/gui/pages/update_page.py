from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout

from pjip.core.enums import UpdateState


class UpdatePage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = 'Updates'
        self.studentmain_state = None
        self.update_state_label = None
        self.current_version_label = None
        self.get_update_btn = None
        self.adapter = None
        self.current_version = None

        self.init_ui()

        self.signal_connect()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

        self.current_version_label = QLabel()
        self.current_version_label.setWordWrap(True)

        self.current_version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_version_label.setStyleSheet("""
                                    background-color: #eeeeee; 
                                    border-radius: 10px;
                                    font-size: 24px;
                                    border: 2px solid #cccccc;
                                    color: #455A64;   
                                    """)
        self.current_version_label.setText(f'Current version: N / a')
        self.current_version_label.setFixedHeight(50)

        self.update_state_label = QLabel()
        self.update_state_label.setWordWrap(True)

        self.update_state_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_state_label.setStyleSheet("""
                                    background-color: #eeeeee; 
                                    border-radius: 10px;
                                    font-size: 24px;
                                    border: 2px solid #cccccc;
                                    color: #455A64;   
                                    """)
        self.update_state_label.setText(f'Getting updates')
        # self.update_state_label.setFixedHeight(100)

        button_layout = QGridLayout()

        self.get_update_btn = QPushButton("Get updates")
        self.get_update_btn.clicked.connect(self.get_update)

        for i, btn in enumerate([self.get_update_btn]):
            btn.setMinimumHeight(50)
            button_layout.addWidget(btn, i // 2, i % 2)
            btn.setStyleSheet("""
                QPushButton {
                    font: 20px;
                    border: 2px solid #cccccc; 
                    border-radius: 8px;        
                    background-color: #eeeeee; 
                    color: #455A64;               
                }
                QPushButton:hover {
                    background-color: #E2E2E2; 
                    border: 2px solid #C4C4C4; 
                }
                QPushButton:pressed {
                    background-color: #D9D9D9; 
                    border: 2px solid #B7B7B7;
                }
            """)

        main_layout.addWidget(self.current_version_label)
        main_layout.addWidget(self.update_state_label)

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
        self.current_version_label.setText(f'Current version: {self.current_version}')

    def get_update(self):
        self.update_state_label.setText(f'Getting updates')

        self.adapter.get_update()

    def update_update_label(self, state_package):
        state, content = state_package

        if state == UpdateState.FIND_LATEST:
            self.update_state_label.setText(f'A new version is available: {content}')
        elif state == UpdateState.IS_LATEST:
            self.update_state_label.setText('You are already using the latest version')
        elif state == UpdateState.NOT_FOUND:
            self.update_state_label.setText('No updates found')
        elif state == UpdateState.ERROR:
            self.update_state_label.setText('An error has occurred while checking for updates.')
        else:
            self.update_state_label.setText("Unexpected state. Please contact the developers.")
