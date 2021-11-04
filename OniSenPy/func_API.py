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
from BASE_URLs import *


def securite(email, password):
    pass


def licence():
    LICENCE_URL = f"{BASE}/licenses"
    pass


def licence_id(identifiant):
    LICENCE_URL = f"{BASE}/licenses/{identifiant}"
    pass


def data_set_code(code_dataset):
    DATASET_URL = f""
