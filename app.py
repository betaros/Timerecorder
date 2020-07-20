from flask import Flask
from flask_restplus import Resource, Api, fields

from src.TimeRecording import TimeRecordingService

app = Flask(__name__)
api = Api(app)

ns_frontend = api.namespace('Frontend', description='Frontend operations')
ns_element = api.namespace('Element', description='Element operations')

day_element_model = api.model('DayElement', {
    'begin': fields.datetime,
    'lunch': fields.Integer,
    'end': fields.datetime
})


@ns_frontend.route('/')
class Frontend(Resource):

    def get(self):
        return 'Hello World!'


@ns_element.route('/day')
class DayElement(Resource):

    def post(self, day_element):
        TimeRecordingService.add_element(day_element)
        return 'Hello World!'

    def get(self, element_id):
        TimeRecordingService.show_element(element_id)
        return 'Hello World!'

    def put(self, element_id, day_element):
        TimeRecordingService.edit_element(element_id, day_element)
        return 'Hello World!'

    def delete(self, element_id):
        TimeRecordingService.delete_element(element_id)
        return 'Hello World!'


if __name__ == '__main__':
    app.run()
