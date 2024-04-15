# test_app.py
import unittest
from flask_testing import TestCase
from your_flask_app_file import app  # Remplacez `your_flask_app_file` par le nom de votre fichier contenant le code Flask.

class TestFlaskApi(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print('Contenu de la réponse :', response.data.decode('utf-8'))
        self.assertIn(b'<h1> Deploy flask api</h1>', response.data)

# Autres tests...

if __name__ == '__main__':
    unittest.main()