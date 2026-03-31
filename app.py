from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"ok": True, "message": "Render API aktif"})

@app.route("/render", methods=["POST"])
def render():
    return jsonify({"ok": True, "message": "Render endpoint calisiyor"})
