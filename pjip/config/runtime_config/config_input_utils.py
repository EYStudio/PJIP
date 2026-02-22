from dataclasses import is_dataclass, fields
from enum import Enum


def deserialize_dataclass(cls, data: dict):
    kwargs = {}

    for f in fields(cls):
        name = f.name
        type_ = f.type

        if name not in data:
            kwargs[name] = f.default
            continue

        raw_value = data[name]

        # handle Enum
        if isinstance(type_, type) and issubclass(type_, Enum):
            try:
                kwargs[name] = type_(raw_value)
            except Exception:
                if hasattr(type_, "DEFAULT"):
                    kwargs[name] = type_.DEFAULT
                else:
                    raise ValueError(f"{cls.__name__}.{name} invalid enum value: {raw_value}")
            continue

        # handle dataclass
        if is_dataclass(type_):
            kwargs[name] = deserialize_dataclass(type_, raw_value)
            continue

        # handle list
        if type_ is list and isinstance(raw_value, list):
            kwargs[name] = raw_value
            continue

        # handle basic types
        kwargs[name] = raw_value

    return cls(**kwargs)

