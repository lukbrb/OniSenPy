""" Bibliothèque Python servant d'interface Python à l'API de l'ONISEP (http://opendata.onisep.fr/3-api.htm).

    Ce script reprend les fonctions mises à dispostion par l'API :

    SÉCURITÉ :
        - login [POST] : Récupération d'un token valable 24h pour un développeur enregistré

    LICENCES :
        - licenses    [GET] : Liste des licences
        - licenses_id [GET] : Affichage d'une licence

    DONNÉES:
        - dataset_code_search  [GET] : Recherche dans un jeu de données.

    CATALOGUE:
        - dataset        [GET] : Liste des jeux de données.
        - dataset_code   [GET] : Affichage des métadonnées d'un jeu de données.

    APPLICATION:
        - application [GET] : Liste des applications.
        - application_id [GET] : Récupération d'une application.
"""

import requests
import os
from .BASE_URLs import *
from .erreurs import EchecAuthentification


def login(email, password):
    data = {"email": email, "password": password}
    r = requests.post(LOGIN, data=data)
    if r.ok:
        return r.json()["token"]
    else:
        raise EchecAuthentification(f" [ERREUR {r.status_code}] - {r.json()['message']}")


def licence(token=None):
    LICENCE_URL = f"{LICENCE}"
    r = requests.get(LICENCE_URL)
    return r


def licence_id(identifiant, token=None):
    LICENCE_URL = os.path.join(LICENCE, identifiant)
    r = requests.get(LICENCE_URL)
    return r


def dataset_code(code_dataset, token=None):
    if token:
        print("Token utilisé")
        headers = {"Authorization": token, "Application-ID": "application/json"}
        r = requests.get(DATASET, headers=headers)
    else:
        print("Sans token")
        r = requests.get(DATASET)
    return r


def data_search(code_dataset, query=str(), token=None):
    url = os.path.join(DATASET, code_dataset, "search")
    params = {"q": f"{query}"}
    if token:
        headers = {"Authorization": token, "Application-ID": "application/json"}
        r = requests.get(url, params=params, headers=headers)
    else:
        r = requests.get(url, params=params)

    return r
