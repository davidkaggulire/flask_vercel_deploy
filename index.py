# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "<h2>Flask Vercel </h2>"

"""run.py"""
from api import app

# app = create_app(os.environ.get('environment_variable')or 'testing')

if __name__ == '__main__':
    app.run(debug=True)
