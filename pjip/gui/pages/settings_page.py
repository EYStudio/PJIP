from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy, QButtonGroup, QRadioButton

from pjip.core.enums import KillMethod


class SettingsPage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self, config_object):
        super().__init__()
        self.page_name = 'Settings'
        self.config_object = config_object
        self.adapter = None

        self.init_ui()

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

        # opt_terminate_process = QRadioButton("TerminateProcess")
        # opt_terminate_process.toggled.connect(lambda checked: print("Btn 1 State:", checked))
        # opt_terminate_process.setDisabled(True)
        opt_terminate_process = ValueRadioButton("TerminateProcess", KillMethod.TERMINATE_PROCESS)
        opt_nt_terminate_process = ValueRadioButton("NtTerminateProcess", KillMethod.NT_TERMINATE_PROCESS)

        match self.config_object.process.kill_method:
            case KillMethod.TERMINATE_PROCESS:
                opt_terminate_process.setChecked(True)
            case KillMethod.NT_TERMINATE_PROCESS:
                opt_nt_terminate_process.setChecked(True)
            case _:
                opt_terminate_process.setChecked(True)

        opt_terminate_process.selected.connect(self.set_kill_method)
        opt_nt_terminate_process.selected.connect(self.set_kill_method)

        for opt in [opt_terminate_process, opt_nt_terminate_process]:
            opt.setStyleSheet("""
                font: 20px;
                background-color: #eeeeee; 
                color: #444444;
            """
            )


        terminate_options_group.addButton(opt_terminate_process)
        terminate_options_group.addButton(opt_nt_terminate_process)

        terminate_options_frame_layout.addWidget(label_terminate_options)
        terminate_options_frame_layout.addWidget(opt_terminate_process)
        terminate_options_frame_layout.addWidget(opt_nt_terminate_process)

        main_layout.addWidget(terminate_options)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

        # terminate_options_group = QButtonGroup()
        # terminate_options_group.setExclusive(True)
        #
        # method_to_id = {}
        # id_to_button = {}
        #
        # for i, method in enumerate(KillMethod):
        #     btn = ValueRadioButton(method.name, method)
        #     btn.selected.connect(self.set_kill_method)
        #
        #     terminate_options_group.addButton(btn, i)
        #     method_to_id[method] = i
        #     id_to_button[i] = btn
        #
        #     terminate_options_frame_layout.addWidget(btn)
        #
        # btn = terminate_options_group.button(method_to_id.get(self.config_object.process.kill_method))
        # (btn or id_to_button[0]).setChecked(True)

    def set_adapter(self, adapter):
        self.adapter = adapter

    def set_kill_method(self, kill_method):
        self.adapter.set_kill_method(kill_method)


class CostumeRadioButton(QRadioButton):
    def __init__(self, text):
        super().__init__(text)
        self.text = text
        self.toggled.connect(self.checked)

    def checked(self, checked):
        if checked:
            self.run_task()

    def run_task(self):
        print(f"Btn {self.text} selected")


class ValueRadioButton(QRadioButton):
    selected = Signal(object)

    def __init__(self, text, value):
        super().__init__(text)
        self.value = value
        self.toggled.connect(self.on_toggled)

    def on_toggled(self, checked):
        if checked:
            self.selected.emit(self.value)
