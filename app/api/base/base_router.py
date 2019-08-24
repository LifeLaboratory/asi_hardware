# coding=utf-8
from flask_restful import Resource, reqparse


class BaseRouter(Resource):
    _args = []

    def __init__(self):
        self.args = None
        self.data = dict()
        self.headers =reqparse.request.headers
        print(self.headers)
        self._parser = reqparse.RequestParser()


    def _read_args(self):
        if not bool(self.data):
            self.data = {}
        for arg in self.args:
            self._parser.add_argument(arg)
        self.data.update(self._parser.parse_args())

    def get(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def post(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def delete(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def put(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def options(self):
        return {'Allow': 'PUT'}, 200, \
               {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': 'PUT,GET'}

