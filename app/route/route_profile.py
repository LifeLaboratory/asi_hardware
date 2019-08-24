# coding=utf-8
from app.api.base import base_name as names
from app.api.src.profile import *
from app.api.base.base_router import BaseRouter


class Profile(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER]

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_profile(args)
        return answer or {}

    def post(self):

        self._read_args()
        answer = {}
        try:
            answer = set_profile(self.data)
        except:
            pass
        return answer or {}

    def put(self):

        self._read_args()
        answer = {}
        try:
            answer = put_profile(self.data)
        except:
            pass
        return answer or {}