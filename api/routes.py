from flask import Blueprint, request, jsonify
from api.utils import validate_payload, handle_ai_request
from ai_utilities.sentiment_analysis import sentiment_analysis

routes = Blueprint("routes", __name__)

@routes.route("/ask", methods=["POST"])
def ask():
    payload_schema = {
        "input": str,
        "envs": {
            "OPENAI_API_KEY": str
        }
    }

    payload = request.get_json()
    validation_error = validate_payload(payload, payload_schema)

    if validation_error:
        return jsonify({"result": "", "error": validation_error, "stdout": ""}), 400

    input_text = payload["input"]
    envs = payload["envs"]

    try:
        result, stdout = handle_ai_request(input_text, envs, sentiment_analysis)
        return jsonify({"result": result, "error": "", "stdout": stdout}), 200
    except Exception as e:
        return jsonify({"result": "", "error": str(e), "stdout": ""}), 500