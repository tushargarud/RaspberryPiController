from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class TestResource(Resource):
    def get(self):
        return 'Haha'


api.add_resource(TestResource, "/test")

app.run(port=5005)
