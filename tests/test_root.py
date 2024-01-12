import unittest
from unittest import TestCase 

from api.app import create_app 

class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.app = create_app("production")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
        #return super().setUp()
    
    def tearDown(self) -> None:
        self.app_context.pop()
        #return super().tearDown()
    
    def test_root_response(self):
        response = self.client.get("/", headers={"Content-Type":"application/json"},)

        self.assertEqual(response.status_code,200)