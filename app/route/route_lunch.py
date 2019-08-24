# coding=utf-8
from app.api.base import base_name as names
from app.api.src.lunch import lunch_get_active_id, lunch_get_all_id, lunch_set
from app.api.base.base_router import BaseRouter


class BaseLunch(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER]


class LunchAll(BaseLunch):

    def get(self):

        self._read_args()
        answer = {}
        try:
            answer = lunch_get_all_id(self.data)
        except:
            pass
        return answer or {}


class Lunch(BaseLunch):

    def get(self):

        self.data.update({'user_id': self.headers[names.front_user_id]})
        answer = {}
        try:
            answer = lunch_get_active_id(self.data)
        except:
            pass
        return answer or {}

    def post(self):

        self._read_args()
        answer = {}
        try:
            answer = lunch_set(self.data)
        except:
            pass
        return answer or {}