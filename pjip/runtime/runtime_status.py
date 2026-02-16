import os

from pjip.app.constants import IS_E_CLASSROOM_STUDENTMAIN


class RuntimeStatus:
    def __init__(self, logic):
        self.logic = logic
        self.pid = None
        self.current_process_name = None
        self.argv = None
        self.gui = None
        self.window_handle = None
        self.studentmain_password = None

        self.get_current_pid()
        self.get_current_process_name()
        self.get_argv()
        self.get_studentmain_info()

    def get_current_pid(self):
        self.pid = self.logic.get_current_pid()
        print(f'PID: {self.pid}')

    def get_current_process_name(self):
        self.current_process_name = self.logic.get_current_process_name()
        print(self.current_process_name)

    def get_argv(self):
        self.argv = self.logic.get_argv()
        print(self.argv)

    def get_system_info(self):
        self.system_info = self.logic.get_system_info()

    def get_studentmain_info(self):
        if IS_E_CLASSROOM_STUDENTMAIN:
            key_path = r"SOFTWARE\TopDomain\e-Learning Class Standard\1.00"
            value_name = "TargetDirectory"
            self.studentmain_directory = self.logic.read_registry_value(key_path, value_name)
            self.studentmain_path = os.path.join(self.studentmain_directory, "studentmain.exe")
            print(self.studentmain_path)
        else:
            print('CLASSROOM IS NOT STUDENTMAIN')


    def ui_launched(self, gui):
        self.gui = gui
        self.get_hwnd()

    def get_hwnd(self):
        self.window_handle = self.gui.winId()

    def update_studentmain_password(self, pwd):
        self.studentmain_password = pwd