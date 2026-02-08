from PySide6.QtCore import Signal, QTimer
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QSizePolicy, QLineEdit


class FunctionPage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = 'Function'
        self.adapter = None
        self.custom_terminate_btn = None
        self.custom_process_input = None

        self.signal_connect()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

        custom_terminate_frame = QWidget()
        custom_terminate_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        custom_terminate_frame.setObjectName("custom_terminate_frame")

        custom_terminate_frame.setStyleSheet("""
            #custom_terminate_frame {
                background-color: #eeeeee; 
                border-radius: 10px;
                font-size: 24px;
                /* border: 2px solid #bbbbbb; */
                color: #455A64;   
            }
        """)

        custom_terminate_layout = QVBoxLayout(custom_terminate_frame)
        custom_terminate_layout.setContentsMargins(10, 5, 10, 5)
        custom_terminate_layout.setSpacing(3)

        custom_terminate_title_label = QLabel("Terminate Process")
        custom_terminate_title_label.setStyleSheet("""
            background-color: #eeeeee; 
            border-radius: 10px;
            font-size: 20px;
            color: #455A64;   
        """)

        custom_terminate_box_layout = QHBoxLayout()

        self.custom_process_input = QLineEdit()
        self.custom_process_input.setPlaceholderText("Enter PID or process name")
        self.custom_process_input.setFixedHeight(42)
        self.custom_process_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.custom_process_input.setStyleSheet("""
            QLineEdit {
                font: 16px;
                padding: 2px;
                border: 2px solid #bbbbbb;
                border-radius: 8px;
                background-color: #F0F0F0;
                color: #666666;
            }
            QLineEdit:focus {
                border: 2px solid #A0A0A0;
                background-color: #FDF6FA;
            }
        """)

        # self.custom_terminate_btn = QPushButton(" Kill ")
        self.custom_terminate_btn = QPushButton("Kill Process")
        self.custom_terminate_btn.setFixedHeight(42)
        self.custom_terminate_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                padding: 4px;
                border: 2px solid #cccccc; 
                border-radius: 8px;        
                background-color: #eeeeee; 
                color: #455A64;               
            }
            QPushButton:hover {
                background-color: #dedede; 
            }
            QPushButton:pressed {
                background-color: #cdcdcd; 
            }
        """)
        self.custom_terminate_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.custom_terminate_btn.clicked.connect(self.custom_terminate)

        custom_terminate_box_layout.addWidget(self.custom_process_input)
        custom_terminate_box_layout.addWidget(self.custom_terminate_btn)

        custom_terminate_layout.addWidget(custom_terminate_title_label)
        custom_terminate_layout.addLayout(custom_terminate_box_layout)

        studentmain_pwd_frame = QWidget()
        studentmain_pwd_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        studentmain_pwd_frame.setObjectName("studentmain_pwd_frame")

        studentmain_pwd_frame.setStyleSheet("""
            #studentmain_pwd_frame {
                background-color: #eeeeee; 
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
            background-color: #eeeeee; 
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
                border: 2px solid #bbbbbb;
                border-radius: 8px;
                background-color: #F0F0F0;
                color: #666666;
            }
            QLineEdit:focus {
                border: 2px solid #A0A0A0;
                background-color: #FDF6FA;
            }
        """)

        self.studentmain_pwd_label.setReadOnly(True)

        # self.studentmain_pwd_btn = QPushButton(" Kill ")
        self.studentmain_pwd_btn = QPushButton(" Copy ")
        self.studentmain_pwd_btn.setFixedHeight(42)
        self.studentmain_pwd_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                padding: 4px;
                border: 2px solid #cccccc; 
                border-radius: 8px;        
                background-color: #eeeeee; 
                color: #455A64;               
            }
            QPushButton:hover {
                background-color: #dedede; 
            }
            QPushButton:pressed {
                background-color: #cdcdcd; 
            }
        """)
        self.studentmain_pwd_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.studentmain_pwd_btn.clicked.connect(self.copy_studentmain_password_to_clipboard)

        studentmain_pwd_box_layout.addWidget(self.studentmain_pwd_label)
        studentmain_pwd_box_layout.addWidget(self.studentmain_pwd_btn)

        studentmain_pwd_layout.addWidget(studentmain_pwd_title_label)
        studentmain_pwd_layout.addLayout(studentmain_pwd_box_layout)

        main_layout.addWidget(custom_terminate_frame)
        main_layout.addWidget(studentmain_pwd_frame)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

    def signal_connect(self):
        self.ui_change.connect(self.signal_handler)

    def signal_handler(self, name, value):
        # print(f'Signal in toolkit page: {name}, {value}')
        match name:
            case 'GetStudentmainPasswordAdapter':
                self.display_password(value)

    def set_adapter(self, adapter):
        self.adapter = adapter

    def custom_terminate(self):
        process_info = self.custom_process_input.text().strip()
        if process_info:
            self.adapter.terminate_custom_process(process_info)
            self.custom_process_input.setText('')

    def display_password(self, pwd):
        if pwd is None:
            self.studentmain_pwd_label.setText('Password not found')
        else:
            self.studentmain_pwd_label.setText(pwd)

    def copy_studentmain_password_to_clipboard(self):
        self.adapter.copy_studentmain_password_to_clipboard()
        self.studentmain_pwd_btn.setText('Copied')

        QTimer.singleShot(5000, lambda: self.studentmain_pwd_btn.setText(' Copy '))
