from dataclasses import is_dataclass, asdict
from enum import Enum
import datetime

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
