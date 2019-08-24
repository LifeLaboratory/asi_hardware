# coding=utf-8
from app.api.base import base_name as names
from app.api.src.event import event_get_active_id, event_get_all_id
from app.api.base.base_router import BaseRouter


class BaseEvent(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER]


class EventAll(BaseEvent):

    def get(self):

        self._read_args()
        answer = {}
        try:
            answer = event_get_all_id(self.data)
        except:
            pass
        return answer or {}


class Event(BaseEvent):

    def get(self):

        self._read_args()
        answer = {}
        try:
            answer = event_get_active_id(self.data)
        except:
            pass
        return answer or {}