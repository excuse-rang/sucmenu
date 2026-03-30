from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ok"

@app.route("/menu")
def menu():
    return jsonify({"menu": ["test"]})
