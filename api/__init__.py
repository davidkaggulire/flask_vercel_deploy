from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import app_config


app = Flask(__name__)
api = Api(app)
app.config.from_object(app_config["testing"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)


from .routes import admin_routes

# @api_key_required
# @app.route("/", methods=['GET'])
# def home():
#     return "<h2>David Vercel </h2>"



# @app.route("/materials")
# @api_key_required
# def materials():
#     data = supabase.table("materials").select("*").execute().data
#     print(len(data))
#     if data != 0: 
#         print(data)
#         return data
#     return data
