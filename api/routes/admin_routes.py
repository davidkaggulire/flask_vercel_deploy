"""admin_routes"""

import os
from flask_restful import Resource, reqparse
from flask import jsonify, request, make_response
# from flask_jwt_extended import jwt_required
# from api.serializers.vehicle_serializer import response_serializer

# from schemas.admin_schema import SignedoutSchema
from decorators.decorators import api_key_required

from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

NEWS_KEY: str = os.environ.get("API_NEWS_KEY")

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

from api import api
# from ..models import Vehicle


BLANK = "'{}' cannot be blank"

_parser = reqparse.RequestParser()
_parser.add_argument('service', type=str,
                     help=BLANK.format("service"))
_parser.add_argument('fee', type=str,
                     help=BLANK.format("fee"))


class Materials(Resource):
    """signed out vehicles"""

    # @jwt_required()
    # @token_required
    # @required_params(SignedoutSchema())
    @api_key_required
    def get(self):
        data = supabase.table("materials").select("*").execute().data
        print(len(data))
        if data != 0: 
            print(data)
            return data
        return data


class Home(Resource):
    def get(self):
        return 'Home Page Route'

api.add_resource(Materials, "/api/v1/materials")
api.add_resource(Home, "/")