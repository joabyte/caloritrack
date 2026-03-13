from flask import Flask, send_from_directory, jsonify
import os
app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/api/key")
def get_key():
    return jsonify({"key": os.environ.get("ANTHROPIC_KEY", "")})

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
