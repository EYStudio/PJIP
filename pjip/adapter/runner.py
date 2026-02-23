from PySide6.QtCore import QRunnable

from pjip.core.enums import KillMethod


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


# class TerminatePIDTask(QRunnable):
#     def __init__(self, logic, pids):
#         super().__init__()
#         self.logic = logic
#         self.pids = pids
#
#     def run(self):
#         if not self.pids:
#             print("PID not found")
#             return
#         for pid in self.pids:
#             try:
#                 self.logic.terminate_process(pid)
#             except RuntimeError as err:
#                 print(f"Error occurred in terminate pid task: {err}")

class TerminatePIDTask(QRunnable):
    def __init__(self, logic, pids, kill_method = KillMethod.DEFAULT):
        super().__init__()
        self.logic = logic
        self.pids = pids
        self.kill_method = kill_method

    def run(self):
        if not self.pids:
            print("PID not found")
            return
        for pid in self.pids:
            try:
                self._execute(pid)
            except RuntimeError as err:
                print(f"Error occurred in terminate pid task: {err}")

    def _execute(self, pid):
        if self.kill_method == KillMethod.TERMINATE_THREAD:
            self.logic.terminate_thread(pid)
        elif self.kill_method == KillMethod.NT_TERMINATE_PROCESS:
            self.logic.nt_terminate_process(pid)
        else:
            self.logic.terminate_process(pid)



class TerminatePIDTaskAdvance(AdvanceRunnable):

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
                self.error_callback(err)
            finally:
                self.finished_callback(None)

class TaskmgrRunner(AdvanceRunnable):
    def __init__(self, logic):
        super().__init__(fn=self.run_task)
        self.logic = logic
        self.middle_callback = None
        self.external_callback = None

    def run_task(self):
        for i in range(30):
            if self.middle_callback:
                self.middle_callback(i)

            if self.logic.get_process_state("taskmgr.exe"):
                if self.external_callback:
                    self.external_callback("top_taskmgr")
                return "success"

            # time.sleep(0.1)

        return "timeout"


