# adapter.py
from threading import Thread

from PySide6.QtCore import QObject, Signal, QTimer


class AdapterManager(QObject):
    result = Signal()


class TimerAdapter(QObject):
    stateReady = Signal(bool)

    def __init__(self, logic):
        super().__init__()
        self.logic = logic

        # 定时器，每秒调用一次逻辑层
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(lambda: Thread(target=self.check_state))

    def start(self):
        self.timer.start()
        # 启动时立即执行一次
        QTimer.singleShot(0, self.check_state)

    def check_state(self):
        result = self.logic.get_studentmain_state()
        self.stateReady.emit(result)

    def stop(self):
        pass
