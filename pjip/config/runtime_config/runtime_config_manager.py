from .config_loader import ConfigIO
from .config_structure import ConfigRoot
from ...app.constants import CONFIG_PATH


class RuntimeConfigManager:
    def __init__(self):
        # self.config_root = ConfigRoot()
        self.config_root = ConfigRoot
        self.config_dict: dict = {}

        self.config_io = ConfigIO(CONFIG_PATH, self.config_root)

        self.config_object = self.config_io.load()

        # self.config_io.write(self.config_object)

    def get_config_instance(self) -> ConfigIO:
        return self.config_io

    def get_config_object(self) -> ConfigRoot:
        return self.config_object

    def write(self):
        self.config_io.write(self.config_object)
