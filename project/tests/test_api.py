import json
import unittest
from project.tests.base import BaseTestCase


class TestAPIService(BaseTestCase):
    """ Tests for Users Service """

    def test_connect(self):
        """ Ensure the /ping route behaves correctly """

        response = self.client.get('/api/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    
if __name__ == '__main__':
    unittest.main()
