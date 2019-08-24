import unittest
import requests as req
from app.config.config import HOST
import app.api.base.base_name as names
from app.api.src.authentication import auth
from app.api.helpers.service import Gis
from app.api.sql.profile_provider import Provider
import json

class TestLunch(unittest.TestCase):
    def test_lunch_one_add(self):
        data = {


        }
        id_user = Provider.set_profile(args=names.base_user)
        id_user = 5
        print(id_user)
        headers = {names.ID_USER: id_user}
        resp_1 = req.post(HOST + "/lunch", headers=headers)

        resp = req.get(HOST + "/lunch", headers=headers)
        resp = json.loads(resp.text)
        print("\n\n", resp_1.text, "\n\n")
        print(resp, type(resp))
       # self.assertNotEqual(resp, {})
        return

    def test_lunch_pairs(self):
        id_user_1 = Provider.set_profile(args={'first_name': "denis"})
        id_user_2 = Provider.set_profile(args={'first_name': "ne_denis"})

        headers_1 = {names.ID_USER: id_user_1}
        headers_2 = {names.ID_USER: id_user_2}

        req.post(HOST + "/lunch", headers=headers_1)
        req.post(HOST + "/lunch", headers=headers_2)
        resp_1 = req.get(HOST + '/lunch', headers=headers_1)
        resp_2 = req.get(HOST + '/lunch', headers=headers_2)

        print(resp_1.text)
        print(resp_2.text,type(resp_2.text))


if __name__ == '__main__':
    unittest.main()
