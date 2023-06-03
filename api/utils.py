from flask import request, jsonify

def validate_request_payload(payload_schema):
    def decorator(func):
        def wrapper(*args, **kwargs):
            payload = request.get_json()
            if not payload:
                return jsonify({"result": "", "error": "Invalid JSON payload", "stdout": ""}), 400

            for key, value_type in payload_schema.items():
                if key not in payload or not isinstance(payload[key], value_type):
                    return jsonify({"result": "", "error": f"Invalid payload: Missing or incorrect type for '{key}'", "stdout": ""}), 400

            return func(*args, **kwargs)
        return wrapper
    return decorator

def format_response(result, error, stdout):
    return jsonify({
        "result": result,
        "error": error,
        "stdout": stdout
    })