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
