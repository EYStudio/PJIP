from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout, QSizePolicy

from pjip.config.runtime_config.config_structure import ConfigRoot


class StudentmainPage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = 'Studentmain'


        self.studentmain_state = None
        self.label_studentmain_state = None

        self.init_ui()

        self.signal_connect()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.label_studentmain_state = QLabel()

        self.label_studentmain_state.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_studentmain_state.setStyleSheet("""
                                            background-color: rgba(240, 240, 240, 100); 
                                            border-radius: 10px;
                                            font-size: 24px;
                                            border: 3px solid #cccccc;
                                            color: #455A64;   
                                            """)
        self.label_studentmain_state.setText(f'Not detecting')
        # self.label_studentmain_state.setFixedHeight(100)

        main_layout.addWidget(self.label_studentmain_state)
        self.setLayout(main_layout)

    def signal_connect(self):
        self.ui_change.connect(self.signal_handler)

    def set_adapter(self, adapter):
        self.adapter = adapter


    def set_find_studentmain_state(self, state):
        if state:
            pass
        else:
            self.label_studentmain_state.setText(f"Studentmain: Not found")
            self.label_studentmain_state.setStyleSheet("""
                                                background-color: rgba(150, 150, 150, 100); 
                                                border-radius: 10px;
                                                font-size: 24px;
                                                border: 3px solid #cccccc;
                                                color: #455A64;   
                                                """)



    def set_studentmain_state(self, state):
        status = "not running" if not state else "running"
        self.label_studentmain_state.setText(f"Studentmain: {status}")
        self.studentmain_state = state

        if state:
            self.label_studentmain_state.setStyleSheet("""
                                        background-color: rgba(255, 229, 224, 200); 
                                        border-radius: 10px;
                                        font-size: 24px;
                                        border: 3px solid #cccccc;
                                        color: #E66926;   
                                        """)
        else:
            self.label_studentmain_state.setStyleSheet("""
                                        background-color: rgba(211, 253, 227, 200); 
                                        border-radius: 10px;
                                        font-size: 24px;
                                        border: 3px solid #cccccc;
                                        /* color: #16DC2D;   */
                                        color: green;
                                        """)

    def signal_handler(self, name, value):
        match name:
            case 'MonitorAdapter':
                self.set_studentmain_state(value)
            case 'StudentmainExistAdapter':
                self.set_find_studentmain_state(value)