import unittest
import requests as req
from app.config.config import HOST
import app.api.base.base_name as names
from app.api.src.authentication import auth
from app.api.helpers.service import Gis


class TestLunch(unittest.TestCase):
    def test_auth_back_client(self):
        headers = {names.ID_USER: 1}
        resp = req.get(HOST + "/lunch", headers=headers)
        print("resp = ",resp.text, "end")
        self.assertNotEqual(resp.text, {})
        return

if __name__ == '__main__':
    unittest.main()
