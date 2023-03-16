import unittest
import requests
from onisenpy.urls import *


class TestApi(unittest.TestCase):
    """ Vérifie si les requêtes avec les url de base sont valides."""
    def test_check_base_url(self):
        r = requests.get(BASE_URL)
        self.assertTrue(r.ok)

    def test_check_application(self):
        r = requests.get(APPLICATION)
        self.assertTrue(r.ok)

    def test_check_licence(self):
        r = requests.get(LICENCE)
        self.assertTrue(r.ok)

    def test_check_dataset(self):
        r = requests.get(CATALOGUE)
        self.assertTrue(r.ok)

    def test_check_login(self):
        r = requests.post(LOGIN)
        self.assertTrue(r.status_code == 401)  # Code quand non-authentifié


if __name__ == "__main__":
    unittest.main()
