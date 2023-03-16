""" Bibliothèque Python servant d'interface Python à l'API de l'ONISEP (http://opendata.onisep.fr/3-api.htm).

    Ce script reprend les fonctions mises à dispostion par l'API :

    SÉCURITÉ :
        - login [POST] : Récupération d'un token valable 24 h pour un développeur enregistré

    LICENCES :
        - licenses    [GET] : Liste des licences
        - licenses_id [GET] : Affichage d'une licence

    DONNÉES :
        - dataset_code_search [GET] : Recherche dans un jeu de données.

    CATALOGUE:
        - dataset        [GET] : Liste des jeux de données.
        - dataset_code   [GET] : Affichage des métadonnées d'un jeu de données.

    APPLICATION:
        - application [GET] : Liste des applications.
        - application_id [GET] : Récupération d'une application.
"""

import requests
import os
from .urls import Url
from .erreurs import EchecAuthentification


def login(email, password):
    data = {"email": email, "password": password}
    r = requests.post(Url.SECURITE, data=data)
    if r.ok:
        return r.json()["token"]
    else:
        raise EchecAuthentification(f" [ERREUR {r.status_code}] - {r.json()['message']}")


def licence():
    r = requests.get(Url.LICENCE)
    return r


def licence_id(identifiant):
    licence_url = os.path.join(Url.LICENCE, identifiant)
    r = requests.get(licence_url)
    return r


def dataset(token=None, total=100):
    params = {"size": f"{total}"}

    if token:
        headers = {"Authorization": token, "Application-ID": "application/json"}
        response = requests.get(Url.CATALOGUE, headers=headers, params=params)

    else:
        response = requests.get(Url.CATALOGUE, params=params)

    return response


def data_search(code_dataset, query=str(), token=None):
    """ Recherche les infos d'une école dans un certain jeu de données"""

    url = os.path.join(Url.CATALOGUE, code_dataset, "search")
    params = {"q": f"{query}"}
    if token:
        headers = {"Authorization": token, "Application-ID": "application/json"}
        r = requests.get(url, params=params, headers=headers)
    else:
        r = requests.get(url, params=params)

    return r


def dataset_files(dataset_id=None, token=None, total=100):
    r = dataset(token, total)
    if r.ok:
        data = r.json()['results']
        files = {datum['code']: datum['files'] for datum in data}
        if dataset_id and dataset_id in files.keys():
            return files[dataset_id]
        else:
            return files
