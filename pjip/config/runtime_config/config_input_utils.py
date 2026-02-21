def deserialize_dataclass(cls, data: dict):
    kwargs = {}

    for f in fields(cls):
        name = f.name
        type_ = f.type
        if name not in data:
            kwargs[name] = f.default
            continue

        raw_value = data[name]
