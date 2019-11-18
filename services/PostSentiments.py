from flask_restful import Resource, Api, abort,reqparse
from flask import jsonify, request
import json

class PostSentiments(Resource):
    def get(self):
        response = {
		  "method": "POST"
		}
        print(response)
        return response

