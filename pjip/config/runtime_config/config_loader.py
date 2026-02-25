import os
import tomllib
import tomli_w

from .config_input_utils import deserialize_dataclass
from .config_output_utils import serialize_config_to_dict, HiddenFile


class ConfigIO:
    warning = """Warning: Do not modify this file unless you fully understand the configuration settings."""
    def __init__(self, config_path, config_class):
        self.config_path = config_path
        self.config_class = config_class
        self.comments = [self.warning]

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

    def write(self, config_object):
        config_dict = serialize_config_to_dict(config_object)
        # print('===CONFIG DICT===')
        print(config_dict)

        toml_str = self.to_toml(config_dict)

        try:
            with HiddenFile(self.config_path, "w", encoding="utf-8") as f:
                f.write(toml_str)
        except PermissionError:
            print('Permission Error occurred in writing config')

    def to_toml(self, config_dict):
        toml_content = tomli_w.dumps(config_dict)
        toml_comments = self.serialize_comments()
        toml_str = toml_comments + toml_content

        return toml_str

    def serialize_comments(self):
        def serialize_line(comment_line):
            if comment_line.startswith('# '):
                comment_line = comment_line[2:]
            return '# ' + comment_line + '\n'

        toml_comments = ''
        if self.comments:
            for comment in self.comments:
                lines = comment.splitlines()
                for line in lines:
                    toml_comments += serialize_line(line)


            toml_comments += '\n'

        return toml_comments
