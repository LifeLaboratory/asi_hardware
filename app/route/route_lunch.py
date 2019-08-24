# coding=utf-8
from app.api.base import base_name as names
from app.api.src.lunch import lunch_get_active_id, lunch_get_all_id
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

        self._read_args()
        answer = {}
        try:
            answer = lunch_get_active_id(self.data)
        except:
            pass
        return answer or {}