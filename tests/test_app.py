import unittest
from app import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello from Jenkins CI/CD Pipeline!")

if __name__ == "__main__":
    unittest.main()
