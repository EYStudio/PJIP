from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy, QButtonGroup, QRadioButton

from pjip.gui.pages.page_format import RequireNameMixin


class SettingsPage(QWidget, RequireNameMixin):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = None
        self.adapter = None
        self.set_page_name()
        self.init_ui()

    def set_page_name(self):
        self.page_name = 'Settings'

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

        terminate_options = QWidget()
        terminate_options.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        terminate_options.setObjectName("terminate_options_frame")

        terminate_options.setStyleSheet("""
                    #terminate_options_frame {
                        background-color: #eeeeee; 
                        border-radius: 10px;
                        font-size: 24px;
                        border: 2px solid #bbbbbb;
                        color: #455A64;   
                    }

                    QRadioButton {
                        font-size: 16px;
                    }
                    QRadioButton::indicator {
                        width: 24px;
                        height: 24px;
                    }
                """)

        terminate_options_frame_layout = QVBoxLayout(terminate_options)
        terminate_options_frame_layout.setContentsMargins(12, 5, 10, 5)
        terminate_options_frame_layout.setSpacing(3)

        label_terminate_options = QLabel()
        label_terminate_options.setStyleSheet("""
                                            background-color: #eeeeee; 
                                            border-radius: 10px;
                                            font-size: 20px;
                                            color: #455A64;   
                                            """)
        label_terminate_options.setText(f'Terminate options')
        label_terminate_options.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        terminate_options_group = QButtonGroup()
        terminate_options_group.setExclusive(True)

        opt1 = QRadioButton("TerminateProcess")
        opt1.toggled.connect(lambda checked: print("Btn 1 State:", checked))
        opt1.setChecked(True)
        opt1.setDisabled(True)
        opt2 = QRadioButton("NtTerminateProcess")
        opt2.toggled.connect(lambda checked: print("Btn 2 State:", checked))
        opt2.setDisabled(True)
        # opt3 = QRadioButton("Option C")

        terminate_options_group.addButton(opt1)
        terminate_options_group.addButton(opt2)
        # group.addButton(opt3)

        terminate_options_frame_layout.addWidget(label_terminate_options)
        terminate_options_frame_layout.addWidget(opt1)
        terminate_options_frame_layout.addWidget(opt2)
        # terminate_options_frame_layout.addWidget(opt3)

        main_layout.addWidget(terminate_options)
        main_layout.addStretch(1)

        self.setLayout(main_layout)
