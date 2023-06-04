import json
import unittest
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_ask_endpoint(self):
        payload = {
            "input": "How many people live in canada as of 2023?",
            "api_name": "sentiment_analysis",
            "envs": {
                "OPENAI_API_KEY": "test_api_key"
            }
        }
        response = self.app.post('/api/ask', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertIn('result', response_data)
        self.assertIn('error', response_data)
        self.assertIn('stdout', response_data)

    def test_ask_endpoint_invalid_input(self):
        payload = {
            "input": "",
            "api_name": "sentiment_analysis",
            "envs": {
                "OPENAI_API_KEY": "test_api_key"
            }
        }
        response = self.app.post('/api/ask', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        response_data = json.loads(response.data)
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], "Invalid payload: 'input' cannot be empty")

    def test_ask_endpoint_missing_envs(self):
        payload = {
            "input": "How many people live in canada as of 2023?",
            "api_name": "sentiment_analysis"
        }
        response = self.app.post('/api/ask', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        response_data = json.loads(response.data)
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], "Invalid payload: Missing or incorrect type for 'envs'")

if __name__ == '__main__':
    unittest.main()