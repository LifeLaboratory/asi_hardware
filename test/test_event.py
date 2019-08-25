import unittest
import requests as req
import random
from app.config.config import HOST
import app.api.base.base_name as names
from app.api.src.authentication import auth
from app.api.helpers.service import Gis
from app.api.sql.profile_provider import Provider
import json

from app.route.route_event import EventAll
from app.api.src.event import event_get_active, event_get_all, event_set, event_put, event_add, event_get

class TestEvent(unittest.TestCase):

    def test_get_all_events(self):

        args = None
        result = event_get_all(args)

        print(result)

    def test_get_events(self):

        headers = {names.EVENT_ID: '4'}
        result = event_get(headers)

        print(result)

    def test_set_events(self):

        headers = {
            names.TITTLE: 'Рандеву наездников на мамонтах',
            names.PLACE: 'Сибирские степи',
            names.PHOTO: 'Наскальная живопись',
            names.DESCRIPTION: 'Звезды, простор, ветер и шерсть!',
            names.DATE: '2019-08-30',
            names.CREATOR: 1,
            names.MAX_PERSON: 200
        }

        result = event_set(headers)

        print(result)

    def test_put_events(self):

        max_person = int((random.random() * 100) // 1) # Получение случайного значения

        headers = {
            names.TITTLE: 'Рандеву наездников на мамонтах',
            names.PLACE: 'Сибирские степи',
            names.PHOTO: 'Наскальная живопись',
            names.DESCRIPTION: 'Звезды, простор, ветер и шерсть!',
            names.DATE: '2019-08-30',
            names.CREATOR: 1,
            names.MAX_PERSON: max_person,
            names.EVENT_ID: 5
        }


        result = event_put(headers)

        print(result)

if __name__ == '__main__':
    unittest.main()