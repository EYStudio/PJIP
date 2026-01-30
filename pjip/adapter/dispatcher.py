from PySide6.QtCore import QObject, QThreadPool, QRunnable, Signal

class TaskDispatcher(QObject):
    task_error = Signal(Exception)
    task_finished = Signal(object)
    task_return = Signal(object)
    task_middle = Signal(object)
    task_external_action = Signal(object)

    def __init__(self, max_threads=4):
        super().__init__()
        self.pool = QThreadPool()
        self.pool.setMaxThreadCount(max_threads)

        self.daemon_pool = QThreadPool()
        self.daemon_pool.setMaxThreadCount(max_threads)

    def submit(self, runnable, priority=0):
        """
        runnable: QRunnable
        priority: int (higher = more important)
        """
        self.pool.start(runnable, priority)

    def submit_daemon(self, runnable, priority=0):
        """
        runnable: QRunnable
        priority: int (higher = more important)
        """
        self.daemon_pool.start(runnable, priority)

    def wait(self):
        self.pool.waitForDone()


class FutureRunnable(QRunnable):
    def __init__(self, fn, *args, callback=None, error_callback=None):
        super().__init__()
        self.fn = fn
        self.args = args
        self.callback = callback
        self.error_callback = error_callback

    def run(self):
        try:
            result = self.fn(*self.args)
            if self.callback:
                self.callback(result)
        except Exception as e:
            if self.error_callback:
                self.error_callback(e)
