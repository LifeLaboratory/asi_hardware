# coding=utf-8
from app.api.base import base_name as names
from app.api.src.lunch import lunch_get_active_id, lunch_get_all_id, lunch_set, lunch_status_set
from app.api.base.base_router import BaseRouter


class BaseLunch(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.STATUS]
        self.data = {}
        try:
            self.data.update({names.ID_USER: self.headers[names.front_user_id]})
        except:
            self.data.update({names.ID_USER: 0})

    def options(self):
        return {'Allow': 'PUT'}, 200, \
               {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }


class LunchAll(BaseLunch):

    def get(self):

        self.data.update({'user_id': self.headers[names.front_user_id]})
        answer = {}
        try:
            answer = lunch_get_all_id(self.data)
        except:
            pass
        return answer or {}, 200, {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }

    def options(self):
        return {'Allow': 'PUT'}, 200, \
               names.base_cors


class Lunch(BaseLunch):

    def get(self):

        self.data.update({'user_id': self.headers[names.front_user_id]})
        answer = {}
        try:
            answer = lunch_get_active_id(self.data)
        except:
            pass
        code = 200
        if not bool(answer):
            code = 404
        else:
            answer.update({names.STATUS:names.status_to_name[answer[names.STATUS]]})
        return answer or {}, code, names.base_cors

    def post(self):


        lunch = lunch_get_active_id(self.data)
        if bool(lunch):
            return "ERROR", 200, names.base_cors
        answer = {}
        try:
            answer = lunch_set(self.data)
        except:
            pass
        return answer , 200, names.base_cors
    def put(self):
        self._read_args()
        status = names.name_to_status[self.data[names.STATUS]]
        self.data.update({names.STATUS:status})
        answer = None
        try:
            answer = lunch_status_set(self.data)
        except:
            pass
        return answer, 200, names.base_cors

    def options(self):
        return {'Allow': 'PUT'}, 200, \
               names.base_cors