from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class TestResource(Resource):
    def get(self):
        status = request.args.get('status')
        switch_number = request.args.get('switch_number')
        duration = request.args.get('duration')
        return "Hello"

api.add_resource(TestResource, "/test")

app.run(host='0.0.0.0', port=5005, debug=True)
