from PySide6.QtGui import QGuiApplication

from pjip.app.constants import E_CLASSROOM_PROGRAM_NAME
from pjip.config.runtime_config.config_structure import ConfigRoot
from pjip.core.enums import KillMethod


class StartStudentmainAdapter:
    def __init__(self, logic, runtime_status):
        super().__init__()
        self.logic = logic
        self.studentmain_path = runtime_status.studentmain_path

    def start(self):
        return self.logic.start_file(self.studentmain_path)


class SuspendStudentmainAdapter:
    def __init__(self, logic):
        super().__init__()
        self.logic = logic

    def start(self):
        pids = self.logic.get_pid_from_process_name(E_CLASSROOM_PROGRAM_NAME)

        if pids is None:
            print(f'{E_CLASSROOM_PROGRAM_NAME} not found')

        for pid in pids:
            suspend_state = self.logic.is_suspended(pid)
            if suspend_state:
                self.resume(pid)
            else:
                self.suspend(pid)

    def suspend(self, pid):
        self.logic.suspend_process(pid)

    def resume(self, pid):
        self.logic.resume_process(pid)


class CleanIFEODebuggersAdapter:
    def __init__(self, logic):
        super().__init__()
        self.logic = logic

    def start(self):
        self.logic.clean_ifeo_debuggers()


class CopyToClipboardAdapter:
    def __init__(self):
        self.clipboard = QGuiApplication.clipboard()

    def copy_to_clipboard(self, content: str):
        self.clipboard.setText(content)

# class ConfigEditorAdapter:
class EditKillMethodAdapter:
    def __init__(self, config_object: ConfigRoot):
        self.config_object: ConfigRoot = config_object

    def edit_kill_method(self, kill_method):
        try:
            self.config_object.process.kill_method = kill_method
        except ValueError:
            self.config_object.process.kill_method = KillMethod.DEFAULT
        finally:
            print(self.config_object.process.kill_method)

# class ConfigEditorAdapter:
class EditAutoUpdateAdapter:
    def __init__(self, config_object: ConfigRoot):
        self.config_object: ConfigRoot = config_object

    def edit_kill_method(self, kill_method):
        try:
            self.config_object.process.kill_method = kill_method
        except ValueError:
            self.config_object.process.kill_method = KillMethod.DEFAULT
        finally:
            print(self.config_object.process.kill_method)