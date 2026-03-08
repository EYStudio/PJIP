from PySide6.QtCore import QThread


class PollingManager: # QObject
    def __init__(self, signal):
        # super().__init__()
        self.adapters = []
        self.threads = []
        self.signal = signal

    def add(self, adapter):
        self.adapters.append(adapter)
        adapter.change.connect(
            lambda result, w=adapter:
            self.signal.emit(type(w).__name__, result)
        )
        thread = QThread()
        adapter.moveToThread(thread)

        thread.started.connect(adapter.start)
        self.threads.append((adapter, thread))

        thread.start()

    def start(self):
        for adapter in self.adapters:
            thread = QThread()
            adapter.moveToThread(thread)

            thread.started.connect(adapter.start)
            self.threads.append((adapter, thread))
            # self.lifelong_objects[adapter] = thread
            # self.threads[adapter] = thread
            thread.start()

    def stop(self):
        for adapter, thread in self.threads:
            adapter.deleteLater()
            adapter.stop()
            thread.quit()
            thread.wait()
            thread.deleteLater()

    def stop_specific(self, adapter_need_to_stop):
        for adapter, thread in self.threads:
            if adapter is adapter_need_to_stop:
                self.threads.remove((adapter, thread))

                adapter.deleteLater()
                adapter.stop()
                thread.quit()
                thread.wait()
                thread.deleteLater()

    def get_adapter(self, cls):
        for a in self.adapters:
            if isinstance(a, cls):
                return a
        return None