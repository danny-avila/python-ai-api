# api/routes/ask.py
from flask import Blueprint, request, jsonify
from api.utils import validate_request_payload, handle_ai_request, format_response
from ai_utilities.sentiment_analysis import sentiment_analysis

ask_blueprint = Blueprint("ask_blueprint", __name__)

@ask_blueprint.route("/ask", methods=["POST"])
def ask():
    # Define a dictionary of payload schemas for different AI APIs
    payload_schemas = {
        "sentiment_analysis": {
            "input": str,
            "envs": {
                "OPENAI_API_KEY": str
            }
        }
        # Add more schemas here as needed
    }

    # Get the payload from the request
    payload = request.get_json()

    # Get the api_name from the payload
    api_name = payload.get("api_name")

    # Get the payload schema for the specified AI API
    payload_schema = payload_schemas.get(api_name)

    # If the api_name is not recognized, return an error
    if payload_schema is None:
        return format_response("", f"Invalid api_name: '{api_name}'", ""), 400

    # Validate the payload against the schema
    validation_error = validate_request_payload(payload, payload_schema)
    if validation_error:
        return format_response("", validation_error, ""), 400

    # Get the input_text and envs from the payload
    input_text = payload["input"]
    envs = payload["envs"]

    # Determine which AI function to call based on the api_name
    ai_function = None
    if api_name == "sentiment_analysis":
        ai_function = sentiment_analysis
    # Add more AI functions here as needed

    # If the AI function is not recognized, return an error
    if ai_function is None:
        return format_response("", f"Invalid AI function for api_name: '{api_name}'", ""), 400

    try:
        result, stdout = handle_ai_request(payload, payload_schema, ai_function)
        return format_response(result, "", stdout), 200
    except Exception as e:
        return format_response("", str(e), ""), 500

