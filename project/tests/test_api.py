import json
import unittest
from project.tests.base import BaseTestCase


class TestAPIService(BaseTestCase):
    """ Tests for Users Service """

    def test_no_token(self):
        """ Ensure the /ping route behaves correctly with no access token """

        response = self.client.get('/api/ping')
        
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('No auth token specify.', data['error'])


    def test_success_token(self):
        """ Ensure the /ping route behaves correctly with correct access token """

        response = self.client.get('/api/ping', headers= {
            'token': 'supersecretkey'
        })
        
        data = json.loads(response.data.decode())
        self.assertEqual('pong', data['msg'])
    
    def test_bad_token(self):
        """ Ensure the /ping route behaves correctly with incorrect access token """

        response = self.client.get('/api/ping', headers= {
            'token': 'badtoken'
        })
        
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Incorrect auth token.', data['error'])


if __name__ == '__main__':
    unittest.main()
