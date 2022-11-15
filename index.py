from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Flask Vercel </h2>"

