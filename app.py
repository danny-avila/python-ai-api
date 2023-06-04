# app.py
from flask import Flask, request, jsonify
from api import api_blueprints

app = Flask(__name__)

for blueprint in api_blueprints:
    app.register_blueprint(blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)