from pydantic import BaseModel


def convert_to_dict(obj):
    if isinstance(obj, BaseModel):
        return {k: convert_to_dict(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, list):
        return [convert_to_dict(item) for item in obj]
    else:
        return obj