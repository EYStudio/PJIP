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
