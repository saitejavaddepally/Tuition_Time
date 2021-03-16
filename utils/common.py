
from jsonschema import validate, ValidationError, SchemaError   
from utils.errors import send_validate_error


def validate_data(request_data,schema):
    try:
        validate(instance=request_data, schema=schema)
        return None
    except ValidationError as e:
        return send_validate_error(e)    