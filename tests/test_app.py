import os
import unittest
from unittest.mock import patch
from app import app

class GhostShellTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"GhostShell AI", response.data)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_empty_input(self):
        response = self.client.post("/api/analyze", json={"text": " "})
        self.assertEqual(response.status_code, 400)

    def test_missing_key(self):
        with patch.dict(os.environ, {"GEMINI_API_KEY": ""}, clear=False):
            response = self.client.post("/api/analyze", json={"text": "ModuleNotFoundError"})
        self.assertEqual(response.status_code, 503)

if __name__ == "__main__":
    unittest.main()
