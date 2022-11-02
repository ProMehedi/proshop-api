from pydantic import root_validator


def is_unique(field):
    def validator(cls, values):
        root_values = values.get("__root__")
        value_set = set()
        for value in root_values:
            if value[field] in value_set:
                raise ValueError(f"Duplicate {field}")
            else:
                value_set.add(value[field])
        return values

    return root_validator(pre=True, allow_reuse=True)(validator)
