class ConfigIO:
    def __init__(self, config_path, config_class):
        self.config_path = config_path
        self.config_class = config_class

    def read_config(self):
        """read TOML config"""
        try:
            with open(self.config_path, "rb") as f:
                return tomllib.load(f)
        except Exception as e:
            print(f"Failed to read config: {e}")
            return None
