from PySide6.QtCore import Signal, Qt, QTimer
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy, QPushButton

from pjip.core.enums import SuspendState


class RightSidebar(QWidget):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = 'Studentmain'

        self.studentmain_state = None
        self.label_studentmain_state = None

        self.init_ui()

        self.signal_connect()

    def init_ui(self):
        self.setMaximumWidth(170)
        self.setMinimumWidth(150)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        self.label_studentmain_state_base_qss = """
                                            /* border-radius: 10px; */
                                            font-size: 20px;
                                            /* border: 3px solid #cccccc; */
                                            \n"""
        # self.test_frame = CostumeFrame()
        #
        # self.label_studentmain = self.test_frame.add_inner_widget(QLabel)
        # self.label_studentmain_state = self.test_frame.add_inner_widget(QLabel)
        #
        # self.label_studentmain_state.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # for widget in self.test_frame.inner_widgets:
        #     widget.setStyleSheet(self.label_studentmain_state_base_qss + """
        #                                     background-color: rgba(240, 240, 240, 100);
        #                                     color: #455A64;
        #                                     """)
        self.test_frame = QWidget()
        self.test_frame_layout = QVBoxLayout(self.test_frame)
        self.test_frame_widgets = []

        self.label_studentmain = QLabel()
        self.label_studentmain_state = QLabel()

        self.test_frame_widgets.append(self.label_studentmain)
        self.test_frame_widgets.append(self.label_studentmain_state)

        self.test_frame_layout.addWidget(self.label_studentmain)
        self.test_frame_layout.addWidget(self.label_studentmain_state)

        self.label_studentmain.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.label_studentmain_state.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.label_studentmain_state.setAlignment(Qt.AlignmentFlag.AlignCenter)
        for widget in self.test_frame_widgets:
            widget.setStyleSheet(self.label_studentmain_state_base_qss + """
                                            background-color: rgba(240, 240, 240, 100); 
                                            color: #455A64;   
                                            """)
        self.label_studentmain.setText(f'Studentmain')
        self.label_studentmain_state.setText(f'Not detecting')
        # self.label_studentmain_state.setFixedHeight(100)

        main_layout.addWidget(self.test_frame)

        self.setLayout(main_layout)

    def signal_connect(self):
        self.ui_change.connect(self.signal_handler)

    def set_adapter(self, adapter):
        self.adapter = adapter


    def set_find_studentmain_state(self, state):
        if state:
            pass
        else:
            self.label_studentmain_state.setText(f"Not found")
            self.label_studentmain_state.setStyleSheet(
                self.label_studentmain_state_base_qss + """
                    background-color: rgba(150, 150, 150, 100); 
                    color: #455A64;   
                """)

    def set_studentmain_state(self, state):
        status = "running" if state else "not running"
        self.label_studentmain_state.setText(f"{status}")
        self.studentmain_state = state

        if state:
            # for widget in self.test_frame.inner_widgets:
            for widget in self.test_frame_widgets:
                widget.setStyleSheet(self.label_studentmain_state_base_qss + """
                                        /* background-color: rgba(255, 229, 224, 200); */
                                        color: #E66926;   
                                        """)
        else:
            # for widget in self.test_frame.inner_widgets:
            for widget in self.test_frame_widgets:
                widget.setStyleSheet(self.label_studentmain_state_base_qss + """
                                        /* background-color: rgba(211, 253, 227, 200);  */
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
                self.label_studentmain_state.setText(f"running\n(suspended)")

    def signal_handler(self, name, value):
        match name:
            case 'MonitorAdapter':
                self.set_studentmain_state(value)
            case 'SuspendMonitorAdapter':
                self.set_studentmain_suspend_state(value)
            case 'StudentmainExistAdapter':
                self.set_find_studentmain_state(value)

class CostumeFrame(QWidget):
    def __init__(self, /):
        super().__init__()
        self.inner_widgets = []
        self.layout = QVBoxLayout(self)

    def add_inner_widget(self, obj):
        instance = obj(self)
        instance.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.inner_widgets.append(instance)
        self.layout.addWidget(instance)
        return instance

