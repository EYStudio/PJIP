from PySide6.QtCore import Signal, Qt, QTimer
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy, QPushButton

from pjip.core.enums import SuspendState


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
        main_layout.setContentsMargins(3, 3, 3, 3)
        self.label_studentmain_state = QLabel()
        self.label_studentmain_state_base_qss = """
                                            border-radius: 10px;
                                            font-size: 24px;
                                            border: 3px solid #cccccc;
                                            \n"""

        self.label_studentmain_state.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_studentmain_state.setStyleSheet(self.label_studentmain_state_base_qss + """
                                            background-color: rgba(240, 240, 240, 100); 
                                            color: #455A64;   
                                            """)
        self.label_studentmain_state.setText(f'Not detecting')
        # self.label_studentmain_state.setFixedHeight(100)





        studentmain_pwd_frame = QWidget()
        studentmain_pwd_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        studentmain_pwd_frame.setObjectName("studentmain_pwd_frame")

        studentmain_pwd_frame.setStyleSheet("""
                    #studentmain_pwd_frame {
                        background-color: rgba(255, 255, 255, 120); 
                        border: 1px solid rgba(255, 255, 255, 150); 
                        border-radius: 10px;
                        font-size: 24px;
                        /* border: 2px solid #bbbbbb; */
                        color: #455A64;   
                    }
                """)

        studentmain_pwd_layout = QVBoxLayout(studentmain_pwd_frame)
        studentmain_pwd_layout.setContentsMargins(10, 5, 10, 5)
        studentmain_pwd_layout.setSpacing(3)

        studentmain_pwd_title_label = QLabel("Studentmain Password")
        studentmain_pwd_title_label.setStyleSheet("""
                    border-radius: 10px;
                    font-size: 20px;
                    color: #455A64;   
                """)

        studentmain_pwd_box_layout = QHBoxLayout()

        self.studentmain_pwd_label = QLineEdit()
        self.studentmain_pwd_label.setPlaceholderText("Studentmain passwd not found")
        self.studentmain_pwd_label.setFixedHeight(42)
        self.studentmain_pwd_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.studentmain_pwd_label.setStyleSheet("""
                    QLineEdit {
                        font: 16px;
                        padding: 2px;
                        border: 1px solid rgba(0, 0, 0, 50);
                        border-radius: 8px;
                        background-color: rgba(240, 240, 240, 50);
                        color: #666666;
                    }
                    QLineEdit:focus {
                        border: 1px solid rgba(0, 0, 0, 70);
                        background-color: rgba(255, 255, 255, 50);
                    }
                """)

        self.studentmain_pwd_label.setReadOnly(True)

        self.studentmain_pwd_btn = QPushButton("Copy")
        self.studentmain_pwd_btn.setFixedHeight(42)
        self.studentmain_pwd_btn.setMinimumWidth(77)
        self.studentmain_pwd_btn.setStyleSheet("""
                    QPushButton {
                        font: 20px;
                        border: 1px solid rgba(0, 0, 0, 50);
                        border-radius: 8px;        
                        background-color: rgba(238, 238, 238, 100); 
                        color: #444444;               
                    }
                    QPushButton:hover {
                        background-color: rgba(226, 226, 226, 100); 
                        border: 1px solid rgba(50, 50, 50, 50);
                    }
                    QPushButton:pressed {
                        background-color: rgba(217, 217, 217, 100); 
                        border: 1px solid rgba(100, 100, 100, 70);
                    }
                """)
        self.studentmain_pwd_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.studentmain_pwd_btn.clicked.connect(self.copy_studentmain_password_to_clipboard)

        studentmain_pwd_box_layout.addWidget(self.studentmain_pwd_label)
        studentmain_pwd_box_layout.addWidget(self.studentmain_pwd_btn)

        studentmain_pwd_layout.addWidget(studentmain_pwd_title_label)
        studentmain_pwd_layout.addLayout(studentmain_pwd_box_layout)

        main_layout.addWidget(self.label_studentmain_state)
        main_layout.addWidget(studentmain_pwd_frame)

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
            self.label_studentmain_state.setStyleSheet(
                self.label_studentmain_state_base_qss + """
                    background-color: rgba(150, 150, 150, 100); 
                    color: #455A64;   
                """)

    def set_studentmain_state(self, state):
        status = "running" if state else "not running"
        self.label_studentmain_state.setText(f"Studentmain: {status}")
        self.studentmain_state = state

        if state:
            self.label_studentmain_state.setStyleSheet(self.label_studentmain_state_base_qss + """
                                        background-color: rgba(255, 229, 224, 200); 
                                        color: #E66926;   
                                        """)
        else:
            self.label_studentmain_state.setStyleSheet(self.label_studentmain_state_base_qss + """
                                        background-color: rgba(211, 253, 227, 200); 
                                        /* color: #16DC2D;   */
                                        color: green;
                                        """)

    def set_studentmain_suspend_state(self, state):
        match state:
            case SuspendState.SUSPENDED:
                self.label_studentmain_state.setStyleSheet(
                    self.label_studentmain_state_base_qss + """
                        background-color: rgba(255, 229, 224, 200); 
                        color: #FFB637;   
                    """)
                self.label_studentmain_state.setText(f"Studentmain: running (suspended)")

    def signal_handler(self, name, value):
        match name:
            case 'MonitorAdapter':
                self.set_studentmain_state(value)
            case 'SuspendMonitorAdapter':
                self.set_studentmain_suspend_state(value)
            case 'StudentmainExistAdapter':
                self.set_find_studentmain_state(value)
            case 'GetStudentmainPasswordAdapter':
                self.display_password(value)

    def display_password(self, pwd):
        if pwd is None:
            self.studentmain_pwd_label.setText('Password not found')
        elif pwd == '':
            self.studentmain_pwd_label.setText('(Empty password)')
        else:
            self.studentmain_pwd_label.setText(pwd)

    def copy_studentmain_password_to_clipboard(self):
        self.adapter.copy_studentmain_password_to_clipboard()
        self.studentmain_pwd_btn.setText('Copied')

        QTimer.singleShot(5000, lambda: self.studentmain_pwd_btn.setText(' Copy '))

