import unittest
from productpage import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        # Cria um cliente de teste para não precisar subir o servidor real
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Testa se a home responde 200 OK
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_health_check(self):
        # Testa se o health check responde "OK"
        response = self.app.get('/health')
        self.assertEqual(response.data.decode('utf-8'), 'OK')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()