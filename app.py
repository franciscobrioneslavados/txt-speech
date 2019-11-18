from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
import logging
import sys , os
import json
from services.GetSentiments import GetSentiments
from services.PostSentiments import PostSentiments

sys.path.append('../')


app = Flask(__name__)
api = Api(app)


api.add_resource(GetSentiments,'/api/v1/sentiments')
api.add_resource(PostSentiments,'/api/v1/sentiments')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("Runing on http://localhost:5000")
    app.run(host='0.0.0.0',port=port,debug=True)
