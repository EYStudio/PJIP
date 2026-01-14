class RuntimeStatus:
    def __init__(self, logic):
        self.logic = logic
        self.pid = None

    def get_current_pid(self):
        self.pid = self.logic.get_current_pid()
