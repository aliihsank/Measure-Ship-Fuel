
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
import time
from threading import Thread
import pandas as pd
from collections import Counter
import pyodbc
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

userMeasurements = []

class Test(Resource):
    def get(self):
        return {'Test Message(GET)': 'Welcome to new API !!'}
    
    def post(self):
        return {'Test Message(POST)': 'Welcome to new API !!'}


class enterUserMeasurements(Resource):
    def post(self):
        data = request.get_json()
        userMeasurements.append(data['userMeasurements'])
        return {'Server Message': 'Data is being processed !!'}

class Measure(Resource):
    def post(self):
        data = request.get_json()
        
        return{'Server Message': 'Fuel is Measured !!'}
        






api.add_resource(Test, '/test')
api.add_resource(enterUserMeasurements, '/enterUserMeasurements')
api.add_resource(Measure, '/measure')




if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
