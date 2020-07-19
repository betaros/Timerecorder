from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

ns_frontend = api.namespace('Frontend', description='Frontend operations')
ns_begin = api.namespace('Begin', description='Begin operations')
ns_lunch = api.namespace('Lunch', description='Lunch operations')
ns_end = api.namespace('End', description='End operations')
ns_element = api.namespace('Element', description='Element operations')


@ns_frontend.route('/')
class Frontend(Resource):

    def get(self):
        return 'Hello World!'


@ns_begin.route('/begin')
class BeginElement(Resource):

    def post(self):
        return 'Hello World!'

    def get(self):
        return 'Hello World!'

    def put(self):
        return 'Hello World!'

    def delete(self):
        return 'Hello World!'


@ns_lunch.route('/lunch')
class LunchElement(Resource):

    def post(self):
        return 'Hello World!'

    def get(self):
        return 'Hello World!'

    def put(self):
        return 'Hello World!'

    def delete(self):
        return 'Hello World!'


@ns_end.route('/end')
class EndElement(Resource):

    def post(self):
        return 'Hello World!'

    def get(self):
        return 'Hello World!'

    def put(self):
        return 'Hello World!'

    def delete(self):
        return 'Hello World!'


@ns_element.route('/element')
class EndElement(Resource):

    def post(self):
        return 'Hello World!'

    def get(self):
        return 'Hello World!'

    def put(self):
        return 'Hello World!'

    def delete(self):
        return 'Hello World!'


if __name__ == '__main__':
    app.run()
