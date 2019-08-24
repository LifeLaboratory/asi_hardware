# coding=utf-8
from app.api.base import base_name as names
from app.api.src.event import event_get_active, event_get_all, event_set, event_put, event_add, event_get
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
            answer = event_get_all(self.data)
        except:
            pass
        return answer or {}


class Event(BaseEvent):

    def get(self):

        self.data.update({'event_id': self.headers[names.front_event_id]})
        self._read_args()
        answer = {}
        try:
            answer = event_get(self.data)
        except:
            pass
        return answer or {}

    def post(self):

        self._read_args()
        answer = {}
        try:
            answer = event_set(self.data)
        except:
            pass
        return answer or {}

    def put(self):

        self._read_args()
        answer = {}
        try:
            answer = event_put(self.data)
        except:
            pass
        return answer or {}


class EventAdd(BaseEvent):

    def put(self):

        self._read_args()
        answer = {}
        try:
            answer = event_add(self.data)
        except:
            pass
        return answer or {}


class EventActive(BaseEvent):

    def get(self):

        self._read_args()
        answer = {}
        try:
            answer = event_get_active(self.data)
        except:
            pass
        return answer or {}