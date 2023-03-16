""" Classe Connexion qui gère la requête pour récupérer le token.
    Attributs :
    - token
    - date de création
    - date d'expiration
    - heures de validité restantes
    Indique aussi la durée de validité du token
"""
import time
import requests

from urls import Url
from .erreurs import EchecAuthentification


class Connexion:
    # time_units = {"jour": 24 * 3600, "heure": 3600, "minute": 60, "seconde": 1}

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self._created_on = time.time()
        self.token = self.login()
        self.time_units = {"jour": 24 * 3600, "heure": 3600, "minute": 60, "seconde": 1}

    def login(self):
        data = {"email": self.email, "password": self.password}
        r = requests.post(Url.SECURITE, data=data)
        if r.ok:
            return r.json()["token"]  # renvoie le token si authentification réussie
        else:
            raise EchecAuthentification(f" [ERREUR {r.status_code}] - {r.json()['message']}")

    @property
    def created_on(self):
        return time.ctime(self._created_on)  # convertit l'heure de création en date lisible

    @property
    def expire_on(self):
        return time.ctime(self._created_on + 24 * 3600)

    @property
    def remaining_time(self):
        secondes = self._created_on + 24 * 3600 - time.time()
        return secondes/self.time_units["heure"]

    def save_infos(self):
        with open("connexion_data.py", "w") as conn:
            conn.write(f"token = '{self.token}'\ncreated_at = {self._created_on}\n"
                       f"expire_on = {self._created_on + 24 * 3600}\n")
