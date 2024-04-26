import json
from flask import Flask, request, jsonify
from summary import get_summary

app = Flask(__name__)


@app.route("/summarize", methods=["POST"])
def summarize():
    _input = json.loads(request.data)
    return jsonify(
        {"summary": get_summary(_input["input"], _input.get("method") or "custom")}
    )
