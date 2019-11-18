from flask_restful import Resource, Api, abort, reqparse
from flask import jsonify, request
import json

class GetSentiments(Resource):
    def get(self):
        response = {
            "method": "GET"
		}
        print(response)
        return response
