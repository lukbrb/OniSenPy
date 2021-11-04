import unittest
import requests
from ..BASE_URLs import *


class TestApi(unittest.TestCase):
    """ Vérifie si les requêtes avec les url de base sonnt valides."""
    def test_check_base_url(self):
        r = requests.get(BASE)
        self.assertTrue(r.ok)

    def test_check_application(self):
        r = requests.get(APPLICATION)
        self.assertTrue(r.ok)

    def test_check_licence(self):
        r = requests.get(LICENCE)
        self.assertTrue(r.ok)

    def test_check_dataset(self):
        r = requests.get(DATASET)
        self.assertTrue(r.ok)

    def test_check_login(self):
        r = requests.post(LOGIN)
        self.assertTrue(r.status_code == 401)  # Code quand non-authentifié


if __name__ == "__main__":
    unittest.main()
