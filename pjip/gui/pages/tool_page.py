from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout

from pjip.core.enums import SuspendState


class ToolPage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = 'Tools'
        self.studentmain_state = None
        self.kill_run_btn = self.suspend_resume_btn = self.run_taskmgr_btn = self.clean_ifeo_debuggers_btn = None
        self.label_studentmain_state = None
        self.adapter = None
        self.init_ui()

        self.signal_connect()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

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

        button_layout = QGridLayout()

        self.kill_run_btn = QPushButton("Kill studentmain")
        self.kill_run_btn.clicked.connect(self.handle_studentmain)

        self.suspend_resume_btn = QPushButton("Not detect")
        self.suspend_resume_btn.clicked.connect(self.handle_studentmain_suspend)

        self.run_taskmgr_btn = QPushButton("Run Taskmgr")
        self.run_taskmgr_btn.clicked.connect(self.run_taskmgr)

        self.clean_ifeo_debuggers_btn = QPushButton("Clean IFEO")
        self.clean_ifeo_debuggers_btn.clicked.connect(self.clean_ifeo_debuggers)

        # test_button = QPushButton("Test")
        # test_button.clicked.connect(lambda: print('Test button triggered'))

        for i, btn in enumerate(
                [self.kill_run_btn, self.suspend_resume_btn, self.run_taskmgr_btn, self.clean_ifeo_debuggers_btn]):
            btn.setMinimumHeight(50)
            button_layout.addWidget(btn, i // 2, i % 2)
            btn.setStyleSheet("""
                QPushButton {
                    font: 20px;
                    border: 1px solid rgba(255, 255, 255, 150); 
                    border-radius: 8px;        
                    background-color: rgba(238, 238, 238, 100); 
                    color: #444444;               
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
            # cec2ff - b3b3f1 - dcb6d5 - cf8ba9 - b15e6c

        main_layout.addWidget(self.label_studentmain_state)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def signal_connect(self):
        self.ui_change.connect(self.signal_handler)

    def signal_handler(self, name, value):
        match name:
            case 'MonitorAdapter':
                self.set_studentmain_state(value)
            case 'SuspendMonitorAdapter':
                self.set_studentmain_suspend_state(value)
            case 'StudentmainExistAdapter':
                self.set_find_studentmain_state(value)

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
            self.kill_run_btn.setText("Kill studentmain")
        else:
            self.label_studentmain_state.setStyleSheet("""
                                        background-color: rgba(211, 253, 227, 200); 
                                        border-radius: 10px;
                                        font-size: 24px;
                                        border: 3px solid #cccccc;
                                        /* color: #16DC2D;   */
                                        color: green;
                                        """)
            self.kill_run_btn.setText("Run studentmain")

    def handle_studentmain(self):
        if self.studentmain_state:
            self.adapter.terminate_studentmain()
        else:
            self.adapter.start_studentmain()

    def set_studentmain_suspend_state(self, state):
        match state:
            case SuspendState.NOT_FOUND:
                self.suspend_resume_btn.setText('Not found')
                self.suspend_resume_btn.setDisabled(True)
            case SuspendState.RUNNING:
                self.suspend_resume_btn.setText('Suspend')
                self.suspend_resume_btn.setEnabled(True)
            case SuspendState.SUSPENDED:
                self.suspend_resume_btn.setText('Resume')

    def handle_studentmain_suspend(self):
        self.adapter.suspend_resume_studentmain()

    def run_taskmgr(self):
        self.run_taskmgr_btn.setDisabled(True)
        self.adapter.run_taskmgr()
        self.run_taskmgr_btn.setEnabled(True)

    def clean_ifeo_debuggers(self):
        self.adapter.clean_ifeo_debuggers()
