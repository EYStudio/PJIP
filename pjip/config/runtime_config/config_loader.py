import os
import tomllib

from .config_input_utils import deserialize_dataclass


class ConfigIO:
    def __init__(self, config_path, config_class):
        self.config_path = config_path
        self.config_class = config_class

    def load(self):
        if not os.path.exists(self.config_path):
            return self.config_class()
        config_dict = self.read_config()
        if config_dict is not None:
            return deserialize_dataclass(self.config_class, config_dict)
        else:
            return self.config_class()

    def read_config(self):
        """read TOML config"""
        try:
            with open(self.config_path, "rb") as f:
                return tomllib.load(f)
        except Exception as e:
            print(f"Failed to read config: {e}")
            return None
    def serialize_comments(self):
        def serialize_line(comment_line):
            if comment_line.startswith('# '):
                comment_line = comment_line[2:]
            return '# ' + comment_line + '\n'

        toml_comments = ''
        if self.comments:
            for comment in self.comments:
                # lines = comment.splitlines()
                toml_comments += serialize_line(comment)


            toml_comments += '\n'

        return toml_comments
