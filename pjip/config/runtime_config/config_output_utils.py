import datetime
import os.path
from dataclasses import is_dataclass, asdict
from enum import Enum

import pywintypes
import win32file

ALLOWED_SCALAR_TYPES = (
    str, int, float, bool, type(None),
    datetime.datetime, datetime.date, datetime.time
)

ALLOWED_CONTAINER_TYPES = (dict, list)


def serialize_config(obj, path="root"):
    """convert dataclass / Enum / dict / list / tuple into tomllib acceptable types"""

    if isinstance(obj, Enum):
        return obj.value

    if is_dataclass(obj):
        return serialize_config(asdict(obj), path)

    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            child_path = f"{path}.{k}"
            result[k] = serialize_config(v, child_path)
        return result

    if isinstance(obj, list):
        result = []
        for i, v in enumerate(obj):
            child_path = f"{path}[{i}]"
            result.append(serialize_config(v, child_path))
        return result

    if isinstance(obj, tuple):
        result = []
        for i, v in enumerate(obj):
            child_path = f"{path}[{i}]"
            result.append(serialize_config(v, child_path))
        return result

    if isinstance(obj, ALLOWED_SCALAR_TYPES):
        return obj

    raise TypeError(f"Unsupported type at {path}: {type(obj)}")


def serialize_config_to_dict(obj):
    result = serialize_config(obj, path="root")
    if not isinstance(result, dict):
        raise ValueError("Top-level config must be a dict")
    return result


class HiddenFile:
    def __init__(self, path, mode="w", encoding="utf-8"):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        if os.path.exists(self.path):
            # If file exists, remove hidden / system attributes
            try:
                attrs = win32file.GetFileAttributes(self.path)
                safe_attrs = attrs & ~(
                        win32file.FILE_ATTRIBUTE_HIDDEN |
                        win32file.FILE_ATTRIBUTE_SYSTEM
                )
                win32file.SetFileAttributes(self.path, safe_attrs)
            except pywintypes.error:  # type: ignore
                pass

        # Open file
        if "b" in self.mode:
            self.file = open(self.path, self.mode)
        else:
            self.file = open(self.path, self.mode, encoding=self.encoding)

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        # Restore file attributes
        try:
            win32file.SetFileAttributes(
                self.path,
                win32file.FILE_ATTRIBUTE_HIDDEN | win32file.FILE_ATTRIBUTE_SYSTEM
            )
        except pywintypes.error:  # type: ignore
            pass

        return False
