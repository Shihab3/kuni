import json

def serialize_data(data, serialization_format):
    if serialization_format == 'json':
        serialized_data = json.dumps(data)
    else:
        raise ValueError("Unsupported serialization format")
    return serialized_data

def deserialize_data(data, serialization_format):
    if serialization_format == 'json':
        deserialized_data = json.loads(data)
    else:
        raise ValueError("Unsupported serialization format")
    return deserialized_data
