from PySide6.QtCore import QRunnable


class BaseRunnable(QRunnable):
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


class AdvanceRunnable(QRunnable):
    def __init__(self, fn, *args):
        super().__init__()
        self.fn = fn
        self.args = args

        self.callback = None
        self.error_callback = None
        # self.middle_callback = None
        # self.external_callback = None
        self.finished_callback = None

    def run(self):
        try:
            result = self.fn(*self.args)
            if self.callback:
                self.callback(result)
        except Exception as err:
            if self.error_callback:
                self.error_callback(err)
        finally:
            if self.finished_callback:
                self.finished_callback(None)


# task = BaseRunnable(
#     self.logic.terminate_process,
#     pid,
#     callback=lambda r: print("done"),
#     error_callback=lambda e: print("error:", e)
# )
#
# self.dispatcher.submit(task, priority=10)


class TerminatePIDTask(QRunnable):
    def __init__(self, logic, pids):
        super().__init__()
        self.logic = logic
        self.pids = pids

    def run(self):
        if not self.pids:
            print("PID not found")
            return
        for pid in self.pids:
            try:
                self.logic.terminate_process(pid)
            except RuntimeError as err:
                print(err)


class TerminatePIDTaskTest(AdvanceRunnable):

    def __init__(self, logic, pids):
        super().__init__(fn=self.run)
        self.logic = logic
        self.middle_callback = None
        self.external_callback = None
        self.logic = logic
        self.pids = pids

    def run(self):
        if not self.pids:
            print("PID not found")
            return
        for pid in self.pids:
            try:
                self.logic.terminate_process(pid)
            except RuntimeError as err:
                print(err)
