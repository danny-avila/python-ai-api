import json
import unittest
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_ask_endpoint(self):
        payload = {
            "input": "How many people live in canada as of 2023?",
            "envs": {
                "OPENAI_API_KEY": "test_api_key"
            }
        }
        response = self.app.post('/ask', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertIn('result', response_data)
        self.assertIn('error', response_data)
        self.assertIn('stdout', response_data)

    def test_ask_endpoint_invalid_input(self):
        payload = {
            "input": "",
            "envs": {
                "OPENAI_API_KEY": "test_api_key"
            }
        }
        response = self.app.post('/ask', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        response_data = json.loads(response.data)
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], 'Invalid input')

    def test_ask_endpoint_missing_envs(self):
        payload = {
            "input": "How many people live in canada as of 2023?"
        }
        response = self.app.post('/ask', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        response_data = json.loads(response.data)
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], 'Missing environment variables')

if __name__ == '__main__':
    unittest.main()