# test_app.py
import unittest
from flask_testing import TestCase
from app import app, df   

class TestFlaskApi(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1> Deploy flask api</h1>', response.data)

    def test_get_ids(self):
        response = self.client.get('/get_ids')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  # Supposant que la réponse est une liste

    def test_prediction_not_found(self):
        response = self.client.post('/prediction', json={'SK_ID_CURR': 99999999})  # Un ID qui n'existe pas
        self.assertEqual(response.status_code, 404)

    def test_prediction(self):
        sk_id_curr = df['SK_ID_CURR'].values[0]  # Prenez un ID existant pour tester
        response = self.client.post('/prediction', json={'SK_ID_CURR': sk_id_curr})
        self.assertEqual(response.status_code, 200)
        self.assertIn('decision', response.json)

if __name__ == '__main__':
    unittest.main()
