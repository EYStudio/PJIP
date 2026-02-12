import sys

from PySide6.QtWidgets import QApplication

from pjip.config.runtime_config import RuntimeConfigManager
from pjip.app.logic import logic
from pjip.app.services import service
from pjip.runtime import RuntimeStatus
from pjip.adapter import AdapterManager
from pjip.gui import MainWindow
from pjip.config import build_info


class PJIPMain:
    def __init__(self):
        self.config = RuntimeConfigManager()
        self.logic = logic.PJIPLogic(build_info)
        self.runtime_status = RuntimeStatus(self.logic)

        self.app = QApplication(sys.argv)
        self.gui = MainWindow()
        self.adapters = AdapterManager(self.logic, self.gui, self.runtime_status)
        self.gui.adapter_signal_connect(self.adapters)

        self.gui.close_event.connect(self.handle_close_event)

        self.gui.show()

        self.runtime_status.ui_launched(self.gui)

        # self.logic.after_ui_launched(self.gui.winId())

        self.services = service.ServiceManager(self.logic, self.runtime_status)

        # self.app.aboutToQuit.connect(self.handle_close_event)

        sys.exit(self.app.exec())

    def handle_close_event(self):
        self.adapters.quit_all()
        self.services.stop_all()


if __name__ == "__main__":
    PJIPMain()
