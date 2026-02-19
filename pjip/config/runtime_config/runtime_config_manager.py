from .config_structure import ConfigRoot
from .serialize_config import serialize_config_to_dict

# Todo: RuntimeConfigManager init
class RuntimeConfigManager:
    def __init__(self):
        self.config_root = ConfigRoot()
        self.serialize_config = serialize_config_to_dict

        self.config_output = self.serialize_config(self.config_root)
        print(self.config_root)
        print(self.config_output)

    def initialize_config(self):
        pass

    def read_config(self):
        pass

    def anti_serialize_config(self):
        pass