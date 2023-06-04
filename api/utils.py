# api/utils.py
from flask import jsonify

def validate_request_payload(payload, payload_schema):
    if not payload:
        return "Invalid JSON payload"

    for key, value_type in payload_schema.items():
        if isinstance(value_type, dict):
            if key not in payload or not isinstance(payload[key], dict):
                return f"Invalid payload: Missing or incorrect type for '{key}'"
            nested_error = validate_request_payload(payload[key], value_type)
            if nested_error:
                return nested_error
        else:
            if key not in payload or not isinstance(payload[key], value_type):
                return f"Invalid payload: Missing or incorrect type for '{key}'"

    # Check if input_text is empty
    if "input" in payload and not payload["input"].strip():
        return "Invalid payload: 'input' cannot be empty"

    # Check if envs contains unexpected keys
    if "envs" in payload and set(payload["envs"].keys()) != {"OPENAI_API_KEY"}:
        return "Invalid payload: 'envs' contains unexpected keys"

    return None

def format_response(result, error, stdout):
    return jsonify({
        "result": result,
        "error": error,
        "stdout": stdout
    })

def handle_ai_request(payload, payload_schema, ai_function):
    try:
        # Validate the payload against the schema
        validation_error = validate_request_payload(payload, payload_schema)
        if validation_error:
            return "", validation_error

        # Get the input_text and envs from the payload
        input_text = payload["input"]
        envs = payload["envs"]

        # Get the API key
        api_key = envs.get("OPENAI_API_KEY")

        # Call the AI function
        result = ai_function(input_text, api_key)

        # Return the result and any logs
        return result, "AI function executed successfully"
    except Exception as e:
        # Return the error message
        return "", str(e)
