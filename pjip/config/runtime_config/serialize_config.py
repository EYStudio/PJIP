from dataclasses import is_dataclass, asdict
from enum import Enum
import datetime

ALLOWED_SCALAR_TYPES = (
    str, int, float, bool, type(None),
    datetime.datetime, datetime.date, datetime.time
)

ALLOWED_CONTAINER_TYPES = (dict, list)


def serialize_config(obj):
    """convert dataclass / Enum / dict / list / tuple into tomllib acceptable types"""

    if isinstance(obj, Enum):
        return obj.value

    if is_dataclass(obj):
        return serialize_config(asdict(obj))

    if isinstance(obj, dict):
        return {k: serialize_config(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [serialize_config(i) for i in obj]

    if isinstance(obj, tuple):
        return [serialize_config(i) for i in obj]

    if isinstance(obj, ALLOWED_SCALAR_TYPES):
        return obj

    try:
        return str(obj)
    except Exception:
        raise TypeError(f"Unsupported type for TOML serialization: {type(obj)}")
